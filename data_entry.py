import streamlit as st
from autho import get_sheet

sheet = get_sheet()
def run():

    st.title("Enter New Records Here")
    with st.form("Entry Form"):

        drug_id = st.text_input("Drug ID")
        drug_name = st.text_input("Drug Name")
        unit_price = st.text_input("Unit Price")
        stock_quantity = st.text_input("Stock Quantity")

        submit = st.form_submit_button("Submit")

        #on submit
        if submit:
            new_row = [drug_id, drug_name, unit_price, stock_quantity]

            #Append the sheet
            sheet.append_row(new_row)

            st.success(f"{drug_name} Added Successfully")





