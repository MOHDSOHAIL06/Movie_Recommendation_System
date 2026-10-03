
1. **Clone the repo**
   ```bash
   git clone https://github.com/samadkhan-18/movie-recommendation-app.git
   cd movie-recommendation-app
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set environment variables** (optional for local dev — sensible defaults exist, but you'll want your own OMDb key)
   ```bash
   export SECRET_KEY="any-long-random-string"
   export DEBUG=True
   export OMDB_API_KEY="your-omdb-api-key"      # get one free at omdbapi.com/apikey.aspx
   ```

4. **Run the server**
   ```bash
   cd movie_recommendation_system
   python manage.py runserver
   ```

5. Open **http://127.0.0.1:8000/**, pick a movie, and get recommendations.



