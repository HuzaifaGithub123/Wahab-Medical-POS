import streamlit as st
from oauth2client.service_account import ServiceAccountCredentials
import gspread

@st.cache_resource
def get_sheet(Sheet_name="Medicine Data"):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('gspread_credentials.json', scope)
    client = gspread.authorize(credentials)
    sheet = client.open(Sheet_name).sheet1
    return sheet
