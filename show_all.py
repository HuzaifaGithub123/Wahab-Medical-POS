from autho import get_sheet
import streamlit as st
import pandas as pd

def run():
    st.title("Show All Data")
    sheet = get_sheet()

    data = sheet.get_all_records()
    df = pd.DataFrame(data)

    st.dataframe(df)