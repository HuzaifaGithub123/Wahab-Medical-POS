import streamlit as st
from autho import get_sheet

# Initialize sheet connection only once
if 'sheets' not in st.session_state:
    st.session_state.sheets = get_sheet()

def run():
    with st.form("Daily Sales"):
        Drug_ID = st.text_input("Drug ID")
        Drug_name = st.text_input("Drug Name")
        Drug_Quantity = st.text_input("Enter Quantity")
        
        submit = st.form_submit_button("Enter")
        
        if submit:
            data = [Drug_ID, Drug_name, Drug_Quantity]
            try:
                st.session_state.sheets.append_row(data)
                st.success("Successfully Data Entered")
                # Clear form after successful submission
                st.rerun()  # This refreshes the form
            except Exception as e:
                st.error(f"Error: {e}")
