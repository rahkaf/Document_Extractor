# DotExtract Pro

DotExtract Pro is a versatile text extraction tool that supports a wide range of file formats. It can extract text from plain text files, PDFs, DOCX documents, and even images using Optical Character Recognition (OCR). The application offers both a command-line interface (CLI) for batch processing and a user-friendly web interface built with Streamlit for single-file extractions.

## Features

- **Multiple File Types Supported:** Extract text from `.txt`, `.pdf`, `.docx`, `.png`, `.jpg`, and `.jpeg` files.
- **Dual Interfaces:**
    - **Command-Line Interface (CLI):** Process all files in a specified directory and save the extracted text to an output folder.
    - **Streamlit Web App:** Upload a single file and view the extracted text in your browser.
- **OCR for Images:** Utilizes the Tesseract OCR engine to extract text from images.
- **Easy to Use:** Simple and intuitive to run either from the command line or through the web interface.

## Folder Structure

```
/
├── Docs/ # Input folder for the CLI
├── extracted_txt/ # Output folder for the CLI
├── app.py # The command-line application
├── app_streamlit.py # The Streamlit web application
├── requirements.txt # Project dependencies
└── README.md
```

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/rahkaf/Document_Extractor.git
    cd Document_Extractor
    ```

2.  **Install Tesseract OCR:**
    This project uses `pytesseract` for Optical Character Recognition. You will need to install Google's Tesseract OCR engine on your system. You can find installation instructions for your operating system here: [Tesseract Installation](https://github.com/tesseract-ocr/tesseract#installing-tesseract)

    *Note: For Windows users, you will need to add the Tesseract installation path to your system's `PATH` environment variable.*

3.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Command-Line Interface (CLI)

The CLI will process all files in the `Docs` folder and save the extracted text as `.txt` files in the `extracted_txt` folder.

1.  Place the files you want to process into the `Docs` folder.
2.  Run the `app.py` script:
    ```bash
    python app.py
    ```

### Streamlit Web App

The Streamlit app allows you to upload and process one file at a time through a web interface.

1.  Run the `app_streamlit.py` script:
    ```bash
    streamlit run app_streamlit.py
    ```
2.  Open your web browser and navigate to the local URL provided by Streamlit (usually `http://localhost:8501`).
3.  Upload a file and view the extracted text. You can also download the text as a `.txt` file.
