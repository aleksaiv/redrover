import faker
from datetime import date, timedelta
from booking_api_test.services.booking.models import BookingModel

class Payloads:
    def __init__(self):
        self.faker = faker.Faker()

    def booking(self) -> BookingModel:
        d1 = self.faker.date_between_dates(date_start=date.today(), date_end=date.today() + timedelta(days=365))
        d2 = self.faker.date_between_dates(date_start=d1, date_end=date.today() + timedelta(days=365))
        first_name = self.faker.first_name()
        last_name = self.faker.last_name()
        data = {"firstname": first_name,
                "lastname": last_name,
                "totalprice": self.faker.pyfloat(3, 2, True, min_value=0.01, max_value=999.99),
                "depositpaid": self.faker.boolean(70),
                "bookingdates": {"checkin": str(d1), "checkout": str(d2)},
                "additionalneeds": "cofee"}
        return BookingModel(**data)
