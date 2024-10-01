import datetime
from typing_extensions import TypedDict
from pydantic import BaseModel, ConfigDict, field_validator

class BookingDates(TypedDict):
    checkin: datetime.date
    checkout: datetime.date

class BookingModel(BaseModel):
    firstname: str
    lastname: str
    totalprice: float
    depositpaid: bool
    bookingdates: BookingDates
    additionalneeds: str
    model_config = ConfigDict(extra="forbid")

    @field_validator("firstname", "lastname")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

class BookingResponse(BaseModel):
    bookingid: int
    booking: BookingModel
