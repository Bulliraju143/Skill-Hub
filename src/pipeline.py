import sys, os
from file_readers_txt import read_txt
from file_readers_docx import read_docx
from file_readers_pdf import read_pdf
from txt_cleaner import normalize_text
from remove_personal import remove_personal

def read_any(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext == '.txt': 
        return read_txt(file_path)
    if ext == '.docx': 
        return read_docx(file_path)
    if ext == '.pdf': 
        return read_pdf(file_path)
    print("Unsupported file type:", ext)
    return ""

if __name__ == "__main__":
    # Default file = Bulli_raju_Resume.pdf if no argument is passed
    file_path = "Bulli_raju_Resume.pdf"
    if len(sys.argv) > 1:
        file_path = sys.argv[1]

    print(f"Processing file: {file_path}")

    raw = read_any(file_path)
    if not raw.strip():
        print("No text extracted.")
        sys.exit(1)

    print("\n=== BEFORE CLEANING ===\n", raw[:500], "...\n")

    cleaned = normalize_text(remove_personal(raw))

    print("\n=== AFTER CLEANING ===\n", cleaned[:500], "...\n")

    with open("cleaned_Bulli_raju_Resume.txt", "w", encoding="utf-8") as f:
        f.write(cleaned)

    print("\n✅ Saved as cleaned_Bulli_raju_Resume.txt")
