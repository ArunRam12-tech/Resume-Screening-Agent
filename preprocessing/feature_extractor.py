import re
from pathlib import Path

import pandas as pd
import spacy

# Load spaCy model (works locally and on Streamlit Cloud)
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    from spacy.cli import download

    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

# Load skills from CSV
skills_file = Path("data/skills/skills.csv")

SKILLS = (
    pd.read_csv(skills_file)["Skill"]
    .str.lower()
    .tolist()
)


class FeatureExtractor:

    @staticmethod
    def extract_name(text):

        doc = nlp(text)

        for ent in doc.ents:
            if ent.label_ == "PERSON":
                return ent.text

        return "Not Found"

    @staticmethod
    def extract_email(text):

        pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

        match = re.search(pattern, text)

        if match:
            return match.group()

        return "Not Found"

    @staticmethod
    def extract_phone(text):

        pattern = r"(\+91[- ]?)?[6-9]\d{9}"

        match = re.search(pattern, text)

        if match:
            return match.group()

        return "Not Found"

    @staticmethod
    def extract_skills(text):

        text = text.lower()

        found = []

        for skill in SKILLS:

            if skill in text:
                found.append(skill.title())

        return sorted(set(found))

    @staticmethod
    def extract_experience(text):

        text = text.lower()

        # Years
        years = re.findall(
            r'(\d+)\+?\s*(?:years?|yrs?)',
            text
        )

        if years:

            y = max(int(i) for i in years)

            return f"{y} Year{'s' if y > 1 else ''}"

        # Months
        months = re.findall(
            r'(\d+)\+?\s*(?:months?|mos?)',
            text
        )

        if months:

            m = max(int(i) for i in months)

            return f"{m} Month{'s' if m > 1 else ''}"

        if "internship" in text:
            return "Internship"

        return "Fresher"

    @staticmethod
    def extract_education(text):

        text = text.lower()

        # Computer Science Engineering
        if (
            ("computer science" in text or "cse" in text)
            and (
                "b.e" in text
                or "be" in text
                or "b.tech" in text
                or "bachelor" in text
            )
        ):
            return "Bachelor of Engineering (Computer Science)"

        # Information Science Engineering
        elif (
            "information science" in text
            and (
                "b.e" in text
                or "be" in text
                or "b.tech" in text
            )
        ):
            return "Bachelor of Engineering (Information Science)"

        elif "m.tech" in text:
            return "Master of Technology"

        elif "mca" in text:
            return "Master of Computer Applications"

        elif "msc" in text:
            return "Master of Science"

        elif "bachelor" in text:
            return "Bachelor's Degree"

        elif "engineering" in text:
            return "Engineering Graduate"

        return "Education Not Found"
    