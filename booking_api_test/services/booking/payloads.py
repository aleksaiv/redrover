from random import randint
import faker
from datetime import date, timedelta

class Payloads:
    def __init__(self):
        self.faker = faker.Faker()

    def booking(self) -> dict:
        d1 = self.faker.date_between_dates(date_start=date.today(), date_end=date.today() + timedelta(days=365))
        d2 = self.faker.date_between_dates(date_start=d1, date_end=date.today() + timedelta(days=365))
        first_name = self.faker.first_name()
        last_name = self.faker.last_name()
        data = {"firstname": first_name,
                "lastname": last_name,
                "totalprice": randint(0,999),
                "depositpaid": self.faker.boolean(70),
                "bookingdates": {"checkin": str(d1), "checkout": str(d2)},
                "additionalneeds": "cofee"}
        return data
