import streamlit as st
from main import extract_text_from_pdf, process_text

st.set_page_config(page_title="AI Workflow Assistant", page_icon="🧠")

st.title("AI Workflow Assistant")

option = st.radio("Choose input type:", ["Text", "PDF"])

# -------- TEXT INPUT --------
if option == "Text":
    user_input = st.text_area("Enter your text")

    if st.button("Process"):
        if user_input:
            result = process_text(user_input)
            st.subheader("Output")
            st.markdown(result)

# -------- PDF INPUT --------
elif option == "PDF":
    uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

    if uploaded_file:
        text = extract_text_from_pdf(uploaded_file)

        if st.button("Process PDF"):
            result = process_text(text)
            st.subheader("Output")
            st.markdown(result)