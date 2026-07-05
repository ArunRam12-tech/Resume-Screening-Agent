from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


class SimilarityModel:

    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def calculate_similarity(self, resume_text, job_text):

        resume_embedding = self.model.encode([resume_text])

        job_embedding = self.model.encode([job_text])

        score = cosine_similarity(
            resume_embedding,
            job_embedding
        )[0][0]

        return float(round(float(score) * 100, 2))