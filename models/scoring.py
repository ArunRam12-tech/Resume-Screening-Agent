from utils.config import (
    SEMANTIC_WEIGHT,
    SKILL_WEIGHT,
    EXPERIENCE_WEIGHT,
    EDUCATION_WEIGHT,
    PROJECT_WEIGHT,
)


class CandidateScorer:

    @staticmethod
    def skill_score(candidate_skills, job_skills):

        if len(job_skills) == 0:
            return 0

        matched = set(candidate_skills).intersection(job_skills)

        return round((len(matched) / len(job_skills)) * 100, 2)

    @staticmethod
    def experience_score(experience):

        experience = experience.lower()

        if "year" in experience:

            years = int(experience.split()[0])

            if years >= 3:
                return 100

            elif years == 2:
                return 90

            elif years == 1:
                return 80

        elif "month" in experience:

            months = int(experience.split()[0])

            if months >= 6:
                return 80

            elif months >= 3:
                return 70

            else:
                return 60

        elif "internship" in experience:
            return 70

        elif "fresher" in experience:
            return 50

        return 50

    @staticmethod
    def education_score(education):

        education = education.lower()

        if "computer science" in education:
            return 100

        elif "engineering" in education:
            return 90

        elif "technology" in education:
            return 85

        return 60

    @staticmethod
    def project_score(text):

        text = text.lower()

        keywords = [
            "project",
            "developed",
            "implemented",
            "system",
            "application",
            "web application",
            "machine learning",
            "deep learning",
            "ai",
        ]

        score = 0

        for word in keywords:

            if word in text:
                score += 10

        return min(score, 100)

    @staticmethod
    def final_score(
        semantic,
        skill,
        experience,
        education,
        projects,
    ):

        score = (

            semantic * SEMANTIC_WEIGHT +

            skill * SKILL_WEIGHT +

            experience * EXPERIENCE_WEIGHT +

            education * EDUCATION_WEIGHT +

            projects * PROJECT_WEIGHT

        ) / 100

        return round(float(score), 2)
    