"""
============================================================
Project 3 : AI Career Recommendation System

Author      : Abhinav Soni
Internship  : DecodeLabs AI Internship 2026

Description:
This project recommends the Top 3 career paths based on
the user's technical skills using TF-IDF Vectorization
and Cosine Similarity.
============================================================
"""

# ---------------------------------------------------------
# Import Libraries
# ---------------------------------------------------------

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ---------------------------------------------------------
# Load Dataset
# ---------------------------------------------------------

def load_dataset():

    df = pd.read_csv("dataset/raw_skills.csv")

    return df


# ---------------------------------------------------------
# Take User Skills
# ---------------------------------------------------------

def get_user_skills():

    print("=" * 60)
    print("AI CAREER RECOMMENDATION SYSTEM")
    print("=" * 60)

    print("\nEnter your technical skills.")
    print("Type 'done' after entering at least 3 skills.\n")

    skills = []

    while True:

        skill = input(f"Skill {len(skills)+1}: ").strip()

        if skill.lower() == "done":

            if len(skills) >= 3:
                break

            print("Please enter at least 3 skills.\n")
            continue

        if skill == "":
            print("Skill cannot be empty.\n")
            continue

        if len(skill) < 2:
            print("Please enter a valid skill.\n")
            continue

        if skill.lower() in [s.lower() for s in skills]:
            print("Skill already added.\n")
            continue

        skills.append(skill)

    return skills


# ---------------------------------------------------------
# Recommendation Logic
# ---------------------------------------------------------

def recommend_career(df, skills):

    user_skills = " ".join(skills)

    all_skills = df["Skills"].tolist()

    all_skills.append(user_skills)

    vectorizer = TfidfVectorizer()

    tfidf_matrix = vectorizer.fit_transform(all_skills)

    similarity = cosine_similarity(
        tfidf_matrix[-1],
        tfidf_matrix[:-1]
    )

    scores = similarity.flatten()

    top_indices = scores.argsort()[-3:][::-1]

    return top_indices, scores# ---------------------------------------------------------
# Display Recommendations
# ---------------------------------------------------------

def display_recommendations(df, top_indices, scores, skills):

    print("\n" + "=" * 60)
    print("YOUR SKILLS")
    print("=" * 60)

    print(", ".join(skills))

    print("\n" + "=" * 60)
    print("TOP 3 CAREER RECOMMENDATIONS")
    print("=" * 60)

    for rank, index in enumerate(top_indices, start=1):

        role = df.iloc[index]["Job_Role"]
        score = scores[index] * 100

        print("-" * 60)
        print(f"Rank        : {rank}")
        print(f"Career      : {role}")
        print(f"Match Score : {score:.2f}%")

    best_role = df.iloc[top_indices[0]]["Job_Role"]

    print("\n" + "=" * 60)
    print(f"Best Career Recommendation : {best_role}")
    print("=" * 60)

    print("\nProject Completed Successfully!")
    print("Thank you for using AI Career Recommendation System.")


# ---------------------------------------------------------
# Main Function
# ---------------------------------------------------------

def main():

    try:

        df = load_dataset()

        skills = get_user_skills()

        top_indices, scores = recommend_career(
            df,
            skills
        )

        display_recommendations(
            df,
            top_indices,
            scores,
            skills
        )

    except FileNotFoundError:

        print("\nError : Dataset file not found.")
        print("Please check dataset/raw_skills.csv")

    except Exception as error:

        print("\nUnexpected Error:")
        print(error)


# ---------------------------------------------------------
# Program Entry Point
# ---------------------------------------------------------

if __name__ == "__main__":
    main()
