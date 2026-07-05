from pathlib import Path

from parser.pdf_parser import PDFParser
from parser.docx_parser import DOCXParser


class ResumeParser:

    @staticmethod
    def parse(file_path: str):

        extension = Path(file_path).suffix.lower()

        if extension == ".pdf":
            return PDFParser.extract_text(file_path)

        elif extension == ".docx":
            return DOCXParser.extract_text(file_path)

        else:
            raise ValueError("Unsupported file format")