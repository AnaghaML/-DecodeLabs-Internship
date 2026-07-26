import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# -------------------------------
# 1. DATA INGESTION
# -------------------------------

data = pd.read_csv("career_roles.csv")

print("\n" + "=" * 60)
print("              TECH STACK RECOMMENDER")
print("=" * 60)

print("\n✓ DATA INGESTED SUCCESSFULLY")
print(f"  Career paths available: {len(data)}")


# -------------------------------
# 2. USER PROFILE INGESTION
# -------------------------------

print("\n--- USER PROFILE INGESTION ---")
print("Enter at least 3 skills or interests.")
print("Example: Python, Cloud, Automation")

user_input = input("\n> ")

user_skills = [
    skill.strip().lower()
    for skill in user_input.split(",")
    if skill.strip()
]

print("\n✓ USER PROFILE CAPTURED")
print("  Skills:", " | ".join(user_skills))


# -------------------------------
# 3. VECTOR ENGINE
# -------------------------------

print("\n--- INITIALIZING VECTOR ENGINE ---")

career_skills = data["Skills"].str.lower().tolist()

all_profiles = [
    " ".join(user_skills)
] + career_skills

vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(all_profiles)

print("✓ TF-IDF vectorization complete")


# -------------------------------
# 4. COSINE SIMILARITY SCORING
# -------------------------------

print("\n--- EXECUTING COSINE SIMILARITY ---")

similarity_scores = cosine_similarity(
    vectors[0:1],
    vectors[1:]
)[0]

data["Match Score"] = similarity_scores

print("✓ Similarity scoring complete")


# -------------------------------
# 5. RANKING
# -------------------------------

data = data.sort_values(
    by="Match Score",
    ascending=False
)


# -------------------------------
# 6. TOP-3 FILTERING
# -------------------------------

print("\n--- FILTERING TOP-3 RECOMMENDATIONS ---")

top_recommendations = data.head(3)

print("\n" + "=" * 60)
print("           TOP RECOMMENDED CAREER PATHS")
print("=" * 60)

for rank, (_, row) in enumerate(
    top_recommendations.iterrows(),
    start=1
):

    print(f"\n{rank}. {row['Role']}")
    print(f"   Match Score: {row['Match Score']:.4f}")
    print(f"   Required Skills: {row['Skills']}")

    print("-" * 60)