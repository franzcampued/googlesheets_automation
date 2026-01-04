#This module contains the environment variables for the business application

import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_CREDS_PATH = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")

# Validations
if not GOOGLE_CREDS_PATH:
    raise EnvironmentError(
        "GOOGLE_APPLICATION_CREDENTIALS is not set. "
        "Check your .env file or environment variables."
    )

if not SPREADSHEET_ID:
    raise EnvironmentError(
        "SPREADSHEET_ID is not set. "
        "Add it to your .env or environment variables."
    )