"""
import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# Title
st.title("Google Sheets Connection Test")

# Auth function
def get_sheet(sheet_name="Testing"):
    scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
    creds = Credentials.from_service_account_info(st.secrets["gspread"], scopes=scope)
    client = gspread.authorize(creds)
    sheet = client.open(sheet_name).sheet1
    return sheet

import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

@st.cache_resource
def get_sheet(sheet_name="Testing"):
    st.write("🔗 Connecting to Google Sheets...")  # This will show only once
    scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
    creds = Credentials.from_service_account_info(st.secrets["gspread"], scopes=scope)
    client = gspread.authorize(creds)
    sheet = client.open(sheet_name).sheet1
    return sheet
"""

import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# Only show title once using session state
if 'connection_checked' not in st.session_state:
    st.title("🔗 Google Sheets Connection Test")
    st.session_state.connection_checked = True

def get_sheet(sheet_name="Testing"):
    scope = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = Credentials.from_service_account_info(st.secrets["gspread"], scopes=scope)
    client = gspread.authorize(creds)
    return client.open(sheet_name).sheet1
"""
# Connection test (runs only once)
if 'connection_result' not in st.session_state:
    try:
        sheet = get_sheet()
        data = sheet.get_all_records()
        st.session_state.connection_result = {
            "success": True,
            "message": f"✅ Google Sheet connection successful!\n🔍 Found {len(data)} rows.",
            "data": data
        }
    except Exception as e:
        st.session_state.connection_result = {
            "success": False,
            "error": e
        }
