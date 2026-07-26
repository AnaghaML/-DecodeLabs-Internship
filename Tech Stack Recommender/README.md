# Tech Stack Recommender
A content-based recommendation system built using Python and Machine Learning concepts.

## About the Project
This project recommends suitable career paths based on the skills and interests entered by the user.
The system compares the user's skills with the required skills for different technology careers and ranks the most relevant career paths.

## How It Works
The recommendation system follows a 4-step pipeline:

1. **Data Ingestion**  
   Loads career roles and their required skills from a CSV dataset.

2. **User Profile Capture**  
   Accepts skills or interests entered by the user.

3. **Similarity Analysis**  
   Converts the user profile and career skills into TF-IDF vectors and calculates similarity using Cosine Similarity.

4. **Ranking and Filtering**  
   Ranks the career paths based on their similarity scores and displays the Top 3 recommendations.

## Technologies Used
- Python
- Pandas
- Scikit-learn
- TF-IDF Vectorization
- Cosine Similarity

## Project Structure

```text
Tech Stack Recommender/
│
├── recommendation.py
├── career_roles.csv
└── README.md
