import pdfplumber

def read_pdf(file_path):
    text_pages = []
    try:
        with pdfplumber.open(file_path) as pdf:
            for p in pdf.pages:
                text_pages.append(p.extract_text() or "")
        return "\n".join(text_pages)
    except Exception as e:
        print("Error reading pdf:", e)
        return ""
