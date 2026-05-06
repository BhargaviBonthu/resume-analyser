import streamlit as st
from PyPDF2 import PdfReader
import ollama

st.title("AI Resume Analyzer")

st.markdown("Upload your resume for AI-powered analysis")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type="pdf"
)

if uploaded_file:

    reader = PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:
        text += page.extract_text()

    st.subheader("Analysis Result")

    prompt = f"""
    You are an expert AI career advisor.

    Analyze this resume carefully.

    Provide:
    1. Technical strengths
    2. Missing industry-relevant skills
    3. Resume improvement suggestions
    4. Best matching job roles
    5. ATS optimization tips
    6. Recommended certifications

    Resume:
    {text}
    """

    try:

        with st.spinner("Analyzing Resume..."):

            response = ollama.chat(
                model='phi3',
                messages=[
                    {
                        'role': 'user',
                        'content': prompt
                    }
                ]
            )

        result = response['message']['content']

        st.write(result)

    except Exception as e:

        st.error(f"Error: {e}")