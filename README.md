# 📄 Resume Genie – AI Resume Parser + Smart Resume Chatbot  
by [@talhatahir5270](https://github.com/talhatahir5270)

**Resume Genie** is an AI-powered Streamlit web application that intelligently parses your resume and allows you to interact with a smart chatbot. It offers resume improvement suggestions, skill summaries, and resume-specific Q&A using LLaMA 3 via Groq’s blazing-fast API.

---

## 🚀 Features

- 📤 Upload PDF or DOCX resumes
- 🧠 AI-powered chatbot trained on your resume content
- 🔍 Extracted skills summary (Top 5)
- 🧾 Automated resume feedback and suggestions
- 🔒 Filters out unrelated or off-topic questions
- 🔁 Reset chat history at any time
- ⚡ Powered by **Groq**'s **LLaMA 3 model (8B)**

---

## 🧠 Tools, Techniques & Concepts Used

### 🔧 Libraries & Frameworks:
- [Streamlit](https://streamlit.io/) – Web app framework
- [OpenAI (Groq-compatible)](https://pypi.org/project/openai/) – LLM integration
- [pdfplumber](https://github.com/jsvine/pdfplumber) – PDF parsing
- [docx2txt](https://pypi.org/project/docx2txt/) – DOCX parsing

### 🤖 AI/ML Concepts:
- **LLM Prompt Engineering** – Context-aware resume Q&A
- **Skill Extraction** – Using TF-IDF-like filtering & NLP patterns
- **Contextual Filtering** – Ensures resume-relevant queries only
- **Conversational AI** – Maintains user-specific chat history

### 🧪 Techniques:
- Content chunking and prompt injection
- Controlled query flow to prevent off-topic LLM replies
- Groq LLaMA-3 fine-tuned prompting for resume-based tasks
- Chat reset using Streamlit's session state

---

## 📂 Folder Structure

📁 Resume-Genie/
├── app.py               # Main Streamlit app
├── requirements.txt     # Dependencies
└── README.md            # Project documentation

### 🔧 Installation Instructions

  **Clone Repository**
- git clone https://github.com/talhatahir5270/resume-genie.git

 cd resume-genie

**Install required libraries**

pip install -r requirements.txt

**Run the app locally**

streamlit run app.py



