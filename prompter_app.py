import streamlit as st

st.set_page_config(page_title="Hello Streamlit App", layout="centered")

st.title("Hello, Joey! 👋")
st.write("This is a simple Streamlit app deployed to the cloud.")

if st.button("Click me!"):
    st.write("You clicked the button! 🎉")