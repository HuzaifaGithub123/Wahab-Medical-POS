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

# Connect only once
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

# Show title once
if 'connection_checked' not in st.session_state:
    st.title("🔗 Google Sheets Connection Test")
    st.session_state.connection_checked = True

# Display result
if st.session_state.connection_result["success"]:
    st.success(st.session_state.connection_result["message"])
    st.dataframe(st.session_state.connection_result["data"])
else:
    st.error("❌ Failed to connect to Google Sheet.")
    st.exception(st.session_state.connection_result["error"])
