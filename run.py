# python code goes here
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('FinanceMarket')

def get_sales_data():
    """
    Get Sales figures input from the user
    """
    print("Please enter sales data from the last market.")
    print("Data should be six numbers, separated by commas.")
    print("Ex: 10,34,23,12,30,12\n")

    data_str = input("Enter your data here: ")
    
    sales_data = data_str.split(",")
    validate_data(sales_data)

def validate_data(values): 
    """
    Inside the try, converts all stings values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there arent exactly 6 numbers.
    """
    try:
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
        )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
    print(values)


get_sales_data()