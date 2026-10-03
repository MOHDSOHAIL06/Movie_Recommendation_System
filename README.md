# 🎬 Movie Recommendation System

A content-based movie recommendation web app built with Django. Pick a movie you like, and it suggests similar titles based on genre and plot overview — with posters pulled live from the OMDb API.

---

## How it works

The app uses **TF-IDF vectorization** over each movie's genre and overview text, then computes **cosine similarity** to find the most similar titles. Rather than storing a full similarity matrix (which would be huge — a 10,000-movie matrix is ~800MB), it precomputes and stores only the **top 15 nearest neighbors per movie**, keeping the model file under 1MB while still giving fast, accurate recommendations.

## Tech stack

- **Backend:** Django
- **ML:** scikit-learn (TF-IDF + cosine similarity), pandas, joblib
- **Posters:** OMDb API
- **Static files:** WhiteNoise
- **Server:** Gunicorn

## Running locally

1. **Clone the repo**
   ```bash
   git clone https://github.com/MOHDSOHAIL06/Movie_Recommendation_System.git
   cd Movie_Recommendation_System/movie_recommendation_system
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```



4. **Run the server**
   ```bash
   cd movie_recommendation_system
   python manage.py runserver
   ```

5. Open **http://127.0.0.1:8000/**, pick a movie, and get recommendations.

