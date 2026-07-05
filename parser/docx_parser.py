from docx import Document
from pathlib import Path


class DOCXParser:
    """Extract text from DOCX resumes."""

    @staticmethod
    def extract_text(docx_path: str) -> str:

        try:

            file = Path(docx_path)

            if not file.exists():
                raise FileNotFoundError(f"{docx_path} not found.")

            document = Document(file)

            paragraphs = []

            for para in document.paragraphs:
                paragraphs.append(para.text)

            return "\n".join(paragraphs)

        except Exception as e:
            print(f"[DOCX ERROR] {e}")
            return ""