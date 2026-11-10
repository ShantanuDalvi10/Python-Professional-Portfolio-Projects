from pypdf import PdfReader

def extract_text(pdf_path):
    reader = PdfReader(pdf_path)

    all_text = ""

    for page in reader.pages:
        text = page.extract_text()
        all_text += text
    return all_text