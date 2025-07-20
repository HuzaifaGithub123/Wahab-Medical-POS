import streamlit as st
from autho import get_sheet
sheets = get_sheet()

def run():

    with st.form("Daily Sales"):
        Drug_ID = st.text_input("Drug ID")
        Drug_name = st.text_input("Drug Name")
        Drug_Quantity = st.text_input("Enter Quantity")

        data = [Drug_ID, Drug_name, Drug_Quantity]

        submit = st.form_submit_button("Enter")
        if submit:
            sheets.append_row(data)
            st.success("Successfully Data Entered")