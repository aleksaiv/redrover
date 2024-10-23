import os
from dotenv import load_dotenv
load_dotenv(".env")

API_URL = os.environ.get("API_URL", "http://127.0.0.1:8000")
WEB_URL = os.environ.get("WEB_URL", "http://127.0.0.1:5173")
USERNAME = os.getenv("API_USERNAME")
PASSWORD = os.getenv("API_PASSWORD")
