import streamlit as st
import openai
import pdfplumber
import docx
from sklearn.feature_extraction.text import TfidfVectorizer
import os

# ===================== 🔐 Set Groq API Key =====================
openai.api_key = st.secrets["GROQ_API_KEY"]
openai.api_base = "https://api.groq.com/openai/v1"

# ===================== 🔍 Extract Resume Text =====================
def extract_text_from_pdf(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def extract_text_from_docx(docx_file):
    doc = docx.Document(docx_file)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_text(file):
    if file.name.endswith(".pdf"):
        return extract_text_from_pdf(file)
    elif file.name.endswith(".docx"):
        return extract_text_from_docx(file)
    else:
        return None

# ===================== 🤖 Generate Suggestions =====================
def improve_resume_with_groq(resume_text):
    prompt = f"Analyze the following resume and give suggestions to improve it:\n\n{resume_text}"
    try:
        response = openai.ChatCompletion.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=800,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"⚠️ GPT Error: {str(e)}"

# ===================== 🧠 Chatbot =====================
def chat_with_resume(resume_text, user_question):
    prompt = f"This is a resume:\n\n{resume_text}\n\nNow answer the user's question:\n{user_question}"
    try:
        response = openai.ChatCompletion.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.6,
            max_tokens=800,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"⚠️ GPT Error: {str(e)}"

# ===================== 🌐 Streamlit UI =====================
st.set_page_config(page_title="Resume Genie", page_icon="🧞", layout="wide")

st.title("🧞‍♂️ Resume Genie: Smart Resume Parser + AI Chatbot")
uploaded_file = st.file_uploader("📄 Upload your resume (.pdf or .docx)", type=["pdf", "docx"])

if uploaded_file:
    resume_text = extract_text(uploaded_file)

    if resume_text:
        st.subheader("📄 Extracted Resume Text")
        with st.expander("View Resume Text"):
            st.text_area("Resume Content", value=resume_text, height=300)

        st.subheader("💡 Suggestions to Improve Your Resume")
        if st.button("✨ Generate Suggestions"):
            suggestions = improve_resume_with_groq(resume_text)
            st.success(suggestions)

        st.subheader("💬 Chatbot")
        user_input = st.text_input("Ask: e.g. 'What are my skills?' or 'How to improve my resume?'")
        if user_input:
            reply = chat_with_resume(resume_text, user_input)
            st.info(reply)
    else:
        st.error("❌ Unsupported file format.")
else:
    st.info("📤 Please upload your resume to get started.")
