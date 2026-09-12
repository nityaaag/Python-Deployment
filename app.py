import streamlit as st
st.title("Student Application")
name=st.text_input("Enter Student Name")
marks=st.number_input(
    "enter marks",
    min_value=0,
    
)