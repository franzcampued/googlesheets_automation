# This module will serve as the way to connect to Google Sheets
import gspread
from google.oauth2.service_account import Credentials
from config import GOOGLE_CREDS_PATH

#Tells google what the app can do
SCOPES = [
    #Reads and writes data and cretes new tab/sheets
    "https://www.googleapis.com/auth/spreadsheets",
    #Opens sheets by ID or name, Creates new files and , Moves or copies files in Drive
    #Some Sheets-only operations may work without Drive scope, but it’s safer to include it for any file-level actions.
    "https://www.googleapis.com/auth/drive"
]

def get_gsheets_client():
    creds = Credentials.from_service_account_file(
        GOOGLE_CREDS_PATH,
        scopes=SCOPES
    )
    return gspread.authorize(creds)


# We don’t import SPREADSHEET_ID here, because the client doesn’t care which sheet — you pass that later in your main code.