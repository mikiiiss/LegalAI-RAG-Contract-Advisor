import PyPDF2

class MyPDF:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path

    def get_pdf_text(self):
        with open(self.pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
        return text

# Usage
pdf_path = "data"
pdf_processor = MyPDF(pdf_path)
pdf_text = pdf_processor.get_pdf_text()