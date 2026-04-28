# app.py
import streamlit as st
import datetime

st.title("🚀 My Simple CD Streamlit App version 909090")

st.write("If this updates after Git push, your pipeline works 😌")

# dynamic content to see refresh
st.write("Current time:")
st.success(datetime.datetime.now())

name = st.text_input("Enter your name:")

if name:
    st.write(f"Hello {name}, Jenkins CD is working!")
