import requests

# Replace 'YOUR_API_KEY' with your actual TMDB API key
API_KEY = "655e0bd373de4b5e5de75cb11ad54032"
BASE_URL = 'https://api.themoviedb.org/3'

def get_movie_rating(movie_title):
    url = f'{BASE_URL}/search/movie'
    params = {'api_key': "655e0bd373de4b5e5de75cb11ad54032", 'query': movie_title}
    response = requests.get(url, params=params)
    data = response.json()
    if data['results']:
        movie_id = data['results'][0]['id']
        url = f'{BASE_URL}/movie/{movie_id}/ratings'
        params = {'api_key': "655e0bd373de4b5e5de75cb11ad54032"}
        response = requests.get(url, params=params)
        ratings_data = response.json()
        return ratings_data
    else:
        return None

# Example usage
movie_title = 'Inception'
ratings = get_movie_rating(movie_title)
if ratings:
    print(f"Ratings for '{movie_title}': {ratings}")
else:
    print(f"No ratings found for '{movie_title}'")

