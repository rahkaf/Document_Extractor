import streamlit as st
import mimetypes
from pathlib import Path
import fitz
from docx import Document
from PIL import Image
import pytesseract

def get_mime_type(file_path):
    return mimetypes.guess_type(str(file_path))[0] or 'unknown/unknown'
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text(file_path, file_type):
    try:
        if file_type.startswith('text/'):
            return file_path.read().decode('utf-8')
        elif file_type == 'application/pdf':
            with open(file_path.name, 'wb') as f:
                f.write(file_path.getbuffer())
            doc = fitz.open(file_path.name)
            text = ""
            for page in doc:
                text += page.get_text()
            return text.strip()
        elif file_type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
            with open(file_path.name, 'wb') as f:
                f.write(file_path.getbuffer())
            doc = Document(file_path.name)
            text = []
            for para in doc.paragraphs:
                text.append(para.text)
            return '\n'.join(text).strip()
        elif file_type.startswith('image/'):
            img = Image.open(file_path)
            text = pytesseract.image_to_string(img)
            return text.strip()
        else:
            return f"Unsupported file type: {file_type}"
    except Exception as e:
        return f"Error extracting text: {e}"

st.title("DotExtract Pro - Document Text Extractor")

uploaded_file = st.file_uploader("Upload a file (.txt, .pdf, .docx, .png, .jpg, .jpeg)", type=["txt", "pdf", "docx", "png", "jpg", "jpeg"])

if uploaded_file is not None:
    mime_type = get_mime_type(uploaded_file.name)
    st.write(f"Detected file type: {mime_type}")
    text = extract_text(uploaded_file, mime_type)
    st.subheader("Extracted Text")
    st.text_area("Text", text, height=300)
    st.download_button("Download as .txt", text, file_name=f"{Path(uploaded_file.name).stem}.txt")