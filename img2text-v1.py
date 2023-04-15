import sys
import os
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFileDialog,
                             QTextEdit, QProgressBar, QGroupBox, QRadioButton, QPlainTextEdit)
from PyQt5.QtGui import QImage, QPixmap, QClipboard
from PyQt5.QtCore import Qt, QBuffer, QIODevice
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class OCRApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('image2txt')
        self.setGeometry(100, 100, 800, 600)

        main_layout = QVBoxLayout()

        image_layout = QHBoxLayout()
        self.label = QLabel(self)
        self.label.setText('No image loaded.')
        image_layout.addWidget(self.label)

        button_layout = QVBoxLayout()
        self.load_button = QPushButton('Load Image', self)
        self.load_button.clicked.connect(self.load_image)
        button_layout.addWidget(self.load_button)

        self.paste_button = QPushButton('Paste Image', self)
        self.paste_button.clicked.connect(self.paste_image)
        button_layout.addWidget(self.paste_button)

        self.save_button = QPushButton('Save Text', self)
        self.save_button.clicked.connect(self.save_text)
        self.save_button.setEnabled(False)
        button_layout.addWidget(self.save_button)

        image_layout.addLayout(button_layout)
        main_layout.addLayout(image_layout)

        text_layout = QVBoxLayout()
        self.text_edit = QPlainTextEdit(self)
        self.text_edit.setReadOnly(True)
        text_layout.addWidget(self.text_edit)
        main_layout.addLayout(text_layout)

        self.setLayout(main_layout)

    def load_image(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Images (*.png *.xpm *.jpg *.bmp);;All Files (*)", options=options)
        if file_name:
            image = QImage(file_name)
            pixmap = QPixmap.fromImage(image)
            self.label.setPixmap(pixmap.scaled(300, 300, Qt.KeepAspectRatio))
            self.label.setScaledContents(True)
            self.perform_ocr(file_name)

    def paste_image(self):
        clipboard = QApplication.clipboard()
        mime_data = clipboard.mimeData()
        
        if mime_data.hasImage():
            image = clipboard.image()
            pixmap = QPixmap.fromImage(image)
            self.label.setPixmap(pixmap.scaled(300, 300, Qt.KeepAspectRatio))
            self.label.setScaledContents(True)

            temp_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "temp.png")
            buffer = QBuffer()
            buffer.open(QIODevice.WriteOnly)
            image.save(buffer, "PNG")
            with open(temp_path, "wb") as f:
                f.write(buffer.data())

            self.perform_ocr(temp_path)
        else:
            print("No image found in the clipboard.")

    def perform_ocr(self, image_path):
        extracted_text = pytesseract.image_to_string(Image.open(image_path))
        self.text_edit.setPlainText(extracted_text)
        self.save_button.setEnabled(True)

    def save_text(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Save Text", "", "Text Files (*.txt);;Word Files (*.docx);;PDF Files (*.pdf);;All Files (*)", options=options)
        if file_name:
            file_extension = os.path.splitext(file_name)[-1].lower()
            if file_extension == ".docx":
                self.save_text_to_docx(file_name)
            elif file_extension == ".pdf":
                self.save_text_to_pdf(file_name)
            else:
                with open(file_name, 'w', encoding='utf-8') as f:
                    f.write(self.text_edit.toPlainText())

    def save_text_to_docx(self, file_name):
        try:
            from docx import Document
        except ImportError:
            print("python-docx module is not installed.")
            return

        doc = Document()
        doc.add_paragraph(self.text_edit.toPlainText())
        doc.save(file_name)

    def save_text_to_pdf(self, file_name):
        try:
            from reportlab.pdfgen import canvas
        except ImportError:
            print("reportlab module is not installed.")
            return

        text = self.text_edit.toPlainText()
        pdf = canvas.Canvas(file_name)
        pdf.setFont("Helvetica", 12)
        x, y = 50, 750
        for line in text.split('\n'):
            pdf.drawString(x, y, line)
            y -= 14
        pdf.save()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ocr_app = OCRApp()
    ocr_app.show()
    sys.exit(app.exec_())
