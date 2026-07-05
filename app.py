import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

from models.ranking import CandidateRanker

st.set_page_config(
    page_title="HireSense AI",
    page_icon="🤖",
    layout="wide"
)

# Load CSS
css = Path("assets/style.css")

if css.exists():
    st.markdown(
        f"<style>{css.read_text()}</style>",
        unsafe_allow_html=True
    )

# ---------------- Header ----------------

st.title("🤖 HireSense AI")
st.subheader("Intelligent Resume Screening System")

st.divider()

# ---------------- Sidebar ----------------

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select",
    [
        "Dashboard",
        "Candidate Details"
    ]
)

# ---------------- Load Data ----------------

job_text = Path(
    "data/jobs/software_engineer.txt"
).read_text(
    encoding="utf-8"
)

ranker = CandidateRanker()

results = ranker.rank_candidates(
    "data/resumes",
    job_text
)

df = pd.DataFrame(results)

# ---------------- Dashboard ----------------

if page == "Dashboard":

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Candidates",
        len(df)
    )

    col2.metric(
        "Shortlisted",
        len(
            df[
                df["Recommendation"] == "SHORTLIST"
            ]
        )
    )

    col3.metric(
        "Average Score",
        round(
            df["Overall Score"].mean(),
            2
        )
    )

    st.divider()

    st.subheader("Candidate Ranking")

    st.dataframe(
        df[
            [
                "Candidate",
                "Overall Score",
                "Recommendation"
            ]
        ],
        use_container_width=True
    )

    st.divider()

    fig = px.bar(

        df,

        x="Candidate",

        y="Overall Score",

        color="Recommendation",

        text="Overall Score"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    pie = px.pie(

        df,

        names="Recommendation"

    )

    st.plotly_chart(
        pie,
        use_container_width=True
    )

# ---------------- Candidate Details ----------------

else:

    candidate = st.selectbox(

        "Select Candidate",

        df["Candidate"]

    )

    row = df[
        df["Candidate"] == candidate
    ].iloc[0]

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Overall Score",
            f"{row['Overall Score']}%"
        )

        st.metric(
            "Semantic Score",
            f"{row['Semantic Score']}%"
        )

        st.metric(
            "Skill Match",
            f"{row['Skill Score']}%"
        )

    with col2:

        st.metric(
            "Experience",
            row["Experience"]
        )

        st.metric(
            "Education",
            row["Education"]
        )

        st.metric(
            "Recommendation",
            row["Recommendation"]
        )

    st.divider()

    st.subheader("Missing Skills")

    if row["Missing Skills"]:

        st.error(
            row["Missing Skills"]
        )

    else:

        st.success(
            "No Missing Skills"
        )

    st.divider()

    st.subheader("AI Recruiter Recommendation")

    if row["Recommendation"] == "SHORTLIST":

        st.success(
            """
Strong Match

The candidate satisfies
the required technical
skills and education.

Proceed to Technical Interview.
"""
        )

    elif row["Recommendation"] == "REVIEW":

        st.warning(
            """
Moderate Match

Manual review recommended
before scheduling an interview.
"""
        )

    else:

        st.error(
            """
Weak Match

The candidate does not
meet the required skills.
"""
        )