import re

def remove_personal(text):
    # Remove emails
    text = re.sub(r'\S+@\S+\.\S+', '[EMAIL]', text)
    # Remove URLs
    text = re.sub(r'http\S+|www\.\S+', '[URL]', text)
    # Remove phone numbers (basic pattern)
    text = re.sub(r'\+?\d[\d\-\s]{7,}\d', '[PHONE]', text)
    return text
