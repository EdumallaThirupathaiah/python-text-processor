import streamlit as st
from module.storage import init_db

st.set_page_config(page_title="Text Processor", layout="wide")

init_db()

st.title("Parallel Text Handling Processor")
st.sidebar.success("Select a page above")
