import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

# Create a page header
st.header("Welcome to my homepage! 👋")


# Create three columns 
col1, col2, col3 = st.columns([1,1,1])


