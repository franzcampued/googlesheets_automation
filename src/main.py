#This is contains the main appplication logic
from sheets_client import get_gsheets_client
from config import SPREADSHEET_ID

def main():
    client = get_gsheets_client()
    sheet = client.open_by_key(SPREADSHEET_ID)

    #test if working
    #add 'test value' in A1 cell
    # values_list = sheet.sheet1.row_values(1)
    # print(values_list)

    #Access TableConfig Tab
    worksheet = sheet.worksheet("TableConfig")

    #Get all records in form of dict
    records = worksheet.get_all_records()
    #print(records)

    for row in records:
        table_name = row["table_name"]
        if row["active"] == 1:
            print(f"Processing table: {table_name}")
            # your processing logic here

if __name__ == "__main__":
    main()