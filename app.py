import streamlit as st
import datetime

st.set_page_config(page_title="Hello Streamlit", page_icon="👋")

st.title("🚀 Simple Streamlit Test App")
st.write("If you can see this running on Railway, your deployment works!")

# Input box
name = st.text_input("Enter your name:")

# Button
if st.button("Say hello"):
    st.success(f"Hello, {name or 'stranger'}! 👋")

# Display current time
st.write("Current server time:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
