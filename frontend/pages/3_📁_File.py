import streamlit as st
import pandas as pd
import pickle
import requests


# Streamlit setup
st.set_page_config(
    page_title="Vision Forge - File",
    page_icon="📁",
    layout="wide",
    initial_sidebar_state="expanded",
    
)

# Load movies data from pickle file
movie_dict_url = "https://github.com/CosecSin/VisionForge/raw/main/frontend/movie-files/movie_dict.pkl"
similarity_url = "https://github.com/CosecSin/VisionForge/raw/main/frontend/movie-files/similarity.pkl"
best_movies_url = "https://github.com/CosecSin/VisionForge/raw/main/frontend/movie-files/Best_movies.pkl"
genre_movie_url = "https://github.com/CosecSin/VisionForge/raw/main/frontend/movie-files/genres_movie_list.pkl"

# Function to load pickle file from a URL
def load_pickle_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return pickle.loads(response.content)
    else:
        st.error(f"Failed to load file from URL: {url}")
        return None
        
# Load movies data from pickle file
movies_dict = load_pickle_from_url(movie_dict_url)
movies_df = pd.DataFrame(movies_dict)
similarity = load_pickle_from_url(similarity_url)



st.header("Movies list")
st.write(movies_df)

Popular_movies = load_pickle_from_url(best_movies_url)

st.header("Popular Movie List")
st.write(Popular_movies)

Movies =  load_pickle_from_url(genre_movie_url)

Movies = Movies.sort_values('rating', ascending=False)

st.header("Movie List For Genre")
st.write(Movies)
