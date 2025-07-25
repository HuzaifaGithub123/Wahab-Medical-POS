import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

@st.cache_resource
def get_sheet(sheet_name="Testing"):
    scope = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = Credentials.from_service_account_info(st.secrets["gspread"], scopes=scope)
    client = gspread.authorize(creds)
    return client.open(sheet_name).sheet1

# Just connect silently
try:
    sheet = get_sheet()
    data = sheet.get_all_records()
except:
    pass  # No message, no output
