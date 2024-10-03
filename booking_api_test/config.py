import os
from dotenv import load_dotenv
load_dotenv(".env")

BOOKING_URL = os.environ.get("BOOKING_API_URL", "https://restful-booker.herokuapp.com")
USERNAME = os.getenv("BOOKING_API_USERNAME")
PASSWORD = os.getenv("BOOKING_API_PASSWORD")
