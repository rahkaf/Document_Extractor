import mimetypes
from pathlib import Path
import fitz  # PyMuPDF for PDFs
from docx import Document  # for DOCX
from PIL import Image
import pytesseract #
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  

def get_mime_type(file_path):
    return mimetypes.guess_type(str(file_path))[0] or 'unknown/unknown'


def list_files(folder_path):
    folder = Path(folder_path)
    files_info = []
    for file_path in folder.iterdir():
        if file_path.is_file():
            mime_type = get_mime_type(file_path)
            files_info.append({
                "path": file_path,
                "name": file_path.stem,  # Use stem to avoid double .txt extension
                "type": mime_type
            })
    return files_info

def extract_text(file_path, file_type):
    try:
        if file_type.startswith('text/'):
            # For .txt and similar
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()

        elif file_type == 'application/pdf':
            # Use PyMuPDF to extract PDF text
            doc = fitz.open(file_path)
            text = ""
            for page in doc:
                text += page.get_text()
            return text.strip()

        elif file_type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
            # Extract DOCX text
            doc = Document(file_path)
            text = []
            for para in doc.paragraphs:
                text.append(para.text)
            return '\n'.join(text).strip()

        elif file_type.startswith('image/'):
            # Use OCR to extract text from images
            img = Image.open(file_path)
            text = pytesseract.image_to_string(img)
            return text.strip()

        else:
            return f"Unsupported file type: {file_type}"

    except Exception as e:
        return f"Error extracting text: {e}"

def save_text(filename, text, output_folder='extracted_txt'):
    output_folder = Path(output_folder)
    output_folder.mkdir(exist_ok=True)
    # Save with the same filename but .txt extension
    output_path = output_folder / (filename + ".txt")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(text)
    return output_path

def main(input_folder):
    files = list_files(input_folder)
    for file_info in files:
        print(f"Processing: {file_info['name']} ({file_info['type']})")
        text = extract_text(file_info['path'], file_info['type'])
        save_text(file_info['name'], text)
    print("Extraction complete. Text files saved in 'extracted_txt' folder.")

if __name__ == "__main__":
    input_folder = "./Docs"  # path of folder containing files to extract
    main(input_folder)