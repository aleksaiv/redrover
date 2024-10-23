import datetime
from typing_extensions import TypedDict
from pydantic import BaseModel, RootModel, field_validator


class TestCaseModel(BaseModel):
    id: int
    name: str
    description: str
    steps: list[str]
    expected_result: str
    priority: str

    @field_validator("name", "description", "expected_result")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

    @field_validator("priority", mode="before")
    def fields_enum(cls, value, ctx):
        if isinstance(value, str) and value.casefold() in ["низкий", "средний", "высокий"]:
            return value
        else:
            raise ValueError(f"Field `{ctx.field_name}` contains an invalid value: {value}")


TestCasesModel = RootModel[list[TestCaseModel]]

