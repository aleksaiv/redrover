import pytest
import logging
from ..services.testcases.models import TestCaseModel, TestCasesModel
from ..libs.utils import assert_eq_dicts
from ..services.testcases.payloads import Payloads

logger = logging.getLogger(__name__)


class TestTestCases:
    def test_get_testcases(self, api):
        response = api.get_testcases()
        TestCasesModel.model_validate(response.json())

    def test_create_testcase(self, api):
        new_testcase_payload = api.payloads.new_testcase()
        logger.info(f"{new_testcase_payload=}")
        created_testcase = api.create_testcase(new_testcase_payload).json()
        logger.info(f"{created_testcase=}")
        TestCaseModel.model_validate(created_testcase)
        assert_eq_dicts(new_testcase_payload, created_testcase, {'id'})
        api.delete_testcase(created_testcase["id"])

    def test_create_bad_testcase(self, api):
        for payload in api.payloads.bad_testcase():
            api.create_testcase(payload, 422)



