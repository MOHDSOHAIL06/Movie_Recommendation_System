import os
import joblib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

movie_path = os.path.join(BASE_DIR, "dataset.joblib")
similarity_path = os.path.join(BASE_DIR, "movie_similarity.joblib")

movies = joblib.load(movie_path)

_similarity_data = joblib.load(similarity_path)
top_idx = _similarity_data["top_idx"]
top_score = _similarity_data["top_score"]


def recommendation(movie_name):
    idx = movies[movies.title == movie_name].index[0]

    neighbor_indices = top_idx[idx]
    movie_list = [movies.iloc[i].title for i in neighbor_indices]

    return movie_list


def get_all_movies():
    return list(movies.title.values)
