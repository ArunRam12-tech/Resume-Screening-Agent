class AIExplanation:

    @staticmethod
    def generate(candidate):

        print("\n")
        print("=" * 70)
        print("🤖 AI Recruiter Recommendation")
        print("=" * 70)

        print(f"Candidate : {candidate['Candidate']}")
        print()

        print("Matched Skills")

        matched = candidate["Skill Score"]

        if matched >= 80:
            print("✔ Excellent technical skill match")

        elif matched >= 60:
            print("✔ Good technical skill match")

        else:
            print("✔ Partial technical skill match")

        print()

        print("Strengths")

        if candidate["Semantic Score"] >= 55:
            print("✔ Resume closely matches the Job Description")

        if candidate["Education Score"] >= 90:
            print("✔ Required educational qualification found")

        if candidate["Experience Score"] >= 80:
            print("✔ Relevant internship / experience")

        if candidate["Project Score"] >= 80:
            print("✔ Strong project portfolio")

        print()

        print("Missing Skills")

        if candidate["Missing Skills"]:

            for skill in candidate["Missing Skills"].split(","):

                skill = skill.strip()

                if skill:
                    print(f"✖ {skill}")

        else:

            print("None")

        print()

        print(f"Overall Score : {candidate['Overall Score']:.2f}%")

        print()

        if candidate["Recommendation"] == "SHORTLIST":

            print("⭐⭐⭐⭐⭐ Strong Match")
            print("Recommendation : Proceed to Technical Interview")

        elif candidate["Recommendation"] == "REVIEW":

            print("⭐⭐⭐ Moderate Match")
            print("Recommendation : Needs Manual Review")

        else:

            print("⭐ Weak Match")
            print("Recommendation : Not Recommended")

        print("=" * 70)