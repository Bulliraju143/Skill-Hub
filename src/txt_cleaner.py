import unicodedata, re

def normalize_text(text):
    # Normalize Unicode (accents → ASCII)
    text = unicodedata.normalize('NFKD', text)
    text = text.encode('ascii', 'ignore').decode('ascii')
    # Remove tabs, carriage returns
    text = re.sub(r'[\t\r]+', ' ', text)
    # Remove multiple spaces/newlines
    text = re.sub(r'\s+', ' ', text).strip()
    return text
