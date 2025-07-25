import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# Title
st.title("🔗 Google Sheets Connection Test")

# Auth function
def get_sheet(sheet_name="Testing"):
    scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
    creds = Credentials.from_service_account_info(st.secrets["gspread"], scopes=scope)
    client = gspread.authorize(creds)
    sheet = client.open(sheet_name).sheet1
    return sheet
"""
# Try connecting and reading
try:
    sheet = get_sheet()
    data = sheet.get_all_records()
    st.success("✅ Google Sheet connection successful!")
    st.write(f"🔍 Found {len(data)} rows in the sheet.")
    st.dataframe(data if data else "Sheet is currently empty.")

except Exception as e:
    st.error("❌ Failed to connect to Google Sheets.")
    st.exception(e)
"""
