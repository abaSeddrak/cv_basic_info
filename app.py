import streamlit as st
from PyPDF2 import PdfReader

st.title("Basic CV Info")

uploaded_file = st.file_uploader("Upload PDF", type="pdf")
if uploaded_file:
    pdf = PdfReader(uploaded_file)
    text = ""
    for page in pdf.pages:
        text += page.extract_text()
    st.text_area("PDF Content", text, height=300)