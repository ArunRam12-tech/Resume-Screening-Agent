import pdfplumber
from pathlib import Path


class PDFParser:
    """Extract text from PDF resumes."""

    @staticmethod
    def extract_text(pdf_path: str) -> str:
        text = ""

        try:
            pdf_file = Path(pdf_path)

            if not pdf_file.exists():
                raise FileNotFoundError(f"{pdf_path} not found.")

            with pdfplumber.open(pdf_file) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()

                    if page_text:
                        text += page_text + "\n"

            return text.strip()

        except Exception as e:
            print(f"[PDF ERROR] {e}")
            return ""