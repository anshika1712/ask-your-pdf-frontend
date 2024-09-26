import streamlit as st
import requests
import base64
import tempfile
import os

# FastAPI backend URL
BACKEND_URL = "https://ask-your-pdf-z9zi.onrender.com"

st.title("RAG System with Text-to-Speech")

# File uploader
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        tmp_file_path = tmp_file.name

    # Use the temporary file
    try:
        with open(tmp_file_path, "rb") as file:
            files = {"file": ("uploaded.pdf", file, "application/pdf")}
            response = requests.post(f"{BACKEND_URL}/upload_pdf/", files=files)

        if response.status_code == 200:
            st.success("PDF uploaded successfully!")
        else:
            st.error("Error uploading PDF.")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
    finally:
        # Close the file and attempt to remove it
        try:
            os.unlink(tmp_file_path)
        except PermissionError:
            st.warning("Unable to remove temporary file immediately. It will be removed later.")

# Question input
question = st.text_input("Ask a question about the uploaded PDF:")

if st.button("Get Answer"):
    if question:
        response = requests.post(f"{BACKEND_URL}/agent/", json={"question": question})
        
        if response.status_code == 200:
            answer = response.json()
            st.write("Answer:", answer)

            # Fetch and play audio
            audio_response = requests.get(f"{BACKEND_URL}/play_audio/")
            if audio_response.status_code == 200:
                audio_content = audio_response.content
                st.audio(audio_content, format="audio/wav")
            else:
                st.error("Error fetching audio response.")
        else:
            st.error("Error getting answer from the backend.")
    else:
        st.warning("Please enter a question.")