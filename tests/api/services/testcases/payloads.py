import random

import faker


class Payloads:
    def __init__(self):
        self.faker = faker.Faker()

    def new_testcase(self) -> dict:
        data = {"name": self.faker.catch_phrase(),
                "description": self.faker.text(100),
                "steps": [f"step #{x}" for x in range(random.randint(1, 100))],
                "expected_result": self.faker.text(10),
                "priority": random.choice(["низкий", "средний", "высокий"])}
        return data

    def bad_testcase(self) -> dict:
        bad_data = [{"name": "",
                     "description": None,
                     "steps": "no steps",
                     "expected_result": 123,
                     "priority": "unknown"},
                    {"name": None},
                    {"description": ""}]
        for bad_fields in bad_data:
            data = self.new_testcase()
            for k, v in bad_fields.items():
                data[k] = v
            yield data
