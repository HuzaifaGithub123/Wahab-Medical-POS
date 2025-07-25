import streamlit as st
import data_entry
import show_all
import daily_sales

# Display the title and Description
st.title("Wahab Medical Store")

# Sidebar Navigation
page = st.sidebar.radio("Go to", ["Daily Sales", "Data Entry", "Show All"])

# Run selected page
if page == "Data Entry":
    data_entry.run()

elif page == "Show All":
    show_all.run()

elif page == "Daily Sales":
    daily_sales.run()
