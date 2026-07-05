from pathlib import Path

from parser.resume_parser import ResumeParser
from preprocessing.feature_extractor import FeatureExtractor
from models.similarity import SimilarityModel
from models.scoring import CandidateScorer
from utils.config import (
    SHORTLIST_SCORE,
    REVIEW_SCORE
)


class CandidateRanker:

    def __init__(self):

        self.model = SimilarityModel()

    def rank_candidates(self, resume_folder, job_text):

        candidates = []

        resume_folder = Path(resume_folder)

        files = list(resume_folder.glob("*"))

        # Extract required skills from Job Description
        job_skills = FeatureExtractor.extract_skills(job_text)

        for file in files:

            resume = ResumeParser.parse(str(file))

            candidate_skills = FeatureExtractor.extract_skills(resume)

            experience = FeatureExtractor.extract_experience(resume)

            education = FeatureExtractor.extract_education(resume)

            semantic = self.model.calculate_similarity(
                resume,
                job_text
            )

            skill = CandidateScorer.skill_score(
                candidate_skills,
                job_skills
            )

            exp_score = CandidateScorer.experience_score(
                experience
            )

            edu_score = CandidateScorer.education_score(
                education
            )

            project_score = CandidateScorer.project_score(
                resume
            )

            overall = CandidateScorer.final_score(
                semantic,
                skill,
                exp_score,
                edu_score,
                project_score
            )

            # Missing Skills
            missing = sorted(
                list(
                    set(job_skills) - set(candidate_skills)
                )
            )

            if overall >= SHORTLIST_SCORE:
                recommendation = "SHORTLIST"

            elif overall >= REVIEW_SCORE:
                recommendation = "REVIEW"

            else:
                recommendation = "REJECT"

            candidates.append({

                "Candidate": file.stem,

                "Semantic Score": semantic,

                "Skill Score": skill,

                "Experience": experience,

                "Experience Score": exp_score,

                "Education": education,

                "Education Score": edu_score,

                "Project Score": project_score,

                "Overall Score": overall,

                "Missing Skills": ", ".join(missing),

                "Recommendation": recommendation

            })

        candidates.sort(
            key=lambda x: x["Overall Score"],
            reverse=True
        )

        return candidates