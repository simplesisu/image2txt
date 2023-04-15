# image2txt
Simple python image-2-text

As simple as it gets:

1. Load image from local storage 
or 
2. Paste image from your clipboard (love this function, just sniptool a picture and paste...voila!)
3. It scans and outputs any text that are in the scanned image.
4. Options to save as simple txt, word or PDF...or just copy the text right there.

![bild](https://user-images.githubusercontent.com/97090119/232156528-f2121e9b-4591-47d9-9a10-8babd267488e.png)


**Detailed installation and information:**

## Image to Text OCR Application

This repository contains a simple Optical Character Recognition (OCR) application that allows users to extract text from images. The application is built using Python, PyQt5, and Tesseract OCR. Both the Python source code and a standalone executable for Windows are provided.

**Features**
Load images from disk (supports PNG, JPG, XPM, BMP formats)
Paste images directly from the clipboard
Extract text from images using Tesseract OCR
Save extracted text as a text file, Microsoft Word file (docx), or PDF file
Installation and Usage
Python Script
Requirements
Python 3.6+
PyQt5
pytesseract
Tesseract OCR
pillow
python-docx (optional, for saving as .docx)
reportlab (optional, for saving as .pdf)

**Steps**
1. Install Python 3.6 or later, if not already installed.

2. Install the required libraries:
`pip install PyQt5 pytesseract pillow python-docx reportlab`

3. Install Tesseract OCR. Follow the instructions for your operating system from the official documentation.

4. Set the path to the Tesseract OCR executable in the Python script:
`pytesseract.pytesseract.tesseract_cmd = r'/path/to/tesseract'`
Replace /path/to/tesseract with the actual path to the Tesseract executable. On Windows, it usually looks like C:\Program Files\Tesseract-OCR\tesseract.exe.

5. Run the Python script:
`python img2text.py`

**Executable (Windows)**
1. Download the latest release from the Releases page.
2. Extract the zip file.
3. Run img2text.exe from the extracted folder.

Contributing
Contributions to this project are welcome. Please create a pull request for any bug fixes, improvements, or new features. (still learning github)

License
This project is licensed under the MIT License.
