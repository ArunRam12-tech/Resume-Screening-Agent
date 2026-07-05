from pathlib import Path

from models.ranking import CandidateRanker
from utils.export import export_results
from ai.explanation import AIExplanation


def main():

    print("\n")
    print("=" * 80)
    print("              HireSense AI - Resume Screening Agent")
    print("=" * 80)

    # Load Job Description
    job_file = Path("data/jobs/software_engineer.txt")

    if not job_file.exists():
        print("❌ Job description not found!")
        return

    job_text = job_file.read_text(encoding="utf-8")

    # Rank Candidates
    ranker = CandidateRanker()
    results = ranker.rank_candidates(
        "data/resumes",
        job_text
    )

    # ---------------- Ranking Table ----------------

    print("\nCandidate Rankings\n")

    print("=" * 110)

    print(
        "{:<5} {:<25} {:>10} {:>12} {:>10} {:>15}".format(
            "Rank",
            "Candidate",
            "Overall",
            "Semantic",
            "Skills",
            "Recommendation"
        )
    )

    print("=" * 110)

    for i, row in enumerate(results, start=1):

        print(
            "{:<5} {:<25} {:>9.2f}% {:>11.2f}% {:>9.2f}% {:>15}".format(
                i,
                row["Candidate"],
                float(row["Overall Score"]),
                float(row["Semantic Score"]),
                float(row["Skill Score"]),
                row["Recommendation"]
            )
        )

    print("=" * 110)

    # ---------------- Detailed Report ----------------

    print("\nDetailed Candidate Report")

    for row in results:

        print("\n" + "=" * 80)

        print(f"Candidate          : {row['Candidate']}")
        print(f"Overall Score      : {float(row['Overall Score']):.2f}%")
        print(f"Semantic Score     : {float(row['Semantic Score']):.2f}%")
        print(f"Skill Score        : {float(row['Skill Score']):.2f}%")
        print(f"Experience         : {row['Experience']}")
        print(f"Experience Score   : {float(row['Experience Score']):.2f}%")
        print(f"Education          : {row['Education']}")
        print(f"Education Score    : {float(row['Education Score']):.2f}%")
        print(f"Project Score      : {float(row['Project Score']):.2f}%")

        if row["Missing Skills"]:
            print(f"Missing Skills     : {row['Missing Skills']}")
        else:
            print("Missing Skills     : None")

        print(f"Recommendation     : {row['Recommendation']}")

        # AI Explanation
        print()
        AIExplanation.generate(row)

    print("\n" + "=" * 80)

    # Export Results
    export_results(results)

    print("\n✅ Candidate ranking completed successfully!")
    print("📄 Results exported to: data/output/ranked_candidates.csv")


if __name__ == "__main__":
    main()