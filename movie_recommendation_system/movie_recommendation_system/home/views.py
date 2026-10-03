import os

from django.shortcuts import render
from home.ml.ml_utils import get_all_movies, recommendation
import requests

# Set the OMDB_API_KEY environment variable in production (e.g. in Render's dashboard).
# Falls back to the previously hardcoded key for local development only.
API_KEY = os.environ.get("OMDB_API_KEY", "47552ee5")


def fetch_movie_details(movie_title):
    url = "http://www.omdbapi.com/"
    params = {
        "apikey": API_KEY,
        "t": movie_title  # search by exact title
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()
    except requests.exceptions.RequestException:
        return {
            "title": movie_title,
            "poster": None,
            "imdb": f"https://www.imdb.com/find?q={movie_title}"
        }

    if data.get("Response") == "True":
        return {
            "title": data.get("Title"),
            "poster": data.get("Poster") if data.get("Poster") != "N/A" else None,
            "imdb": f"https://www.imdb.com/title/{data.get('imdbID')}"
        }

    return {
        "title": movie_title,
        "poster": None,
        "imdb": f"https://www.imdb.com/find?q={movie_title}"
    }


def home(request):

    movies = get_all_movies()
    movie_data = []

    if request.method == "POST":

        selected_movie = request.POST.get('movie')
        result = recommendation(selected_movie)

        for movie in result:
            movie_data.append(fetch_movie_details(movie))

        data = {
            "movies": movies,
            "result": movie_data
        }

        return render(request, "home.html", data)

    return render(request, "home.html", {"movies": movies})