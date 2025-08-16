import streamlit as st
from hashlib import sha256

st.set_page_config(page_title="My App", layout="centered"page_icon="🔒")

def check_password():
    def password_entered():
        if "APP_PASSWORD" not in st.secrets:
            st.stop()
        hashed_input = sha256(st.session_state["password"].encode()).hexdigest()
        hashed_secret = sha256(st.secrets.APP_PASSWORD.encode()).hexdigest()
        if hashed_input == hashed_secret:
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    if st.session_state.get("password_correct"):
        return True

    st.text_input("Password", type="password", key="password", on_change=password_entered)
    if st.session_state.get("password_correct") is False:
        st.error("😕 Password incorrect")
    st.stop()

if not check_password():
    st.stop()

# ---------- your app below ----------
st.title("Hello, Joey! 👋")
st.write("This is a simple Streamlit app deployed to the cloud.")

if st.button("Click me!"):
    st.write("You clicked the button! 🎉")