# Step 1: Setting Up Tools and Environment
# The user will use GitHub and Streamlit Cloud for hosting.
# Python and Streamlit will be the primary technologies used.

# Install necessary libraries
# To install libraries, use the following command in the Streamlit Cloud or a setup script:
# pip install streamlit openai spotipy requests

import streamlit as st
import openai
import requests
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy

# Streamlit interface setup
st.title("AI-Powered Song Recommender")
st.subheader("Find your next favorite obscure song!")

# Step 2: User Input
song_name = st.text_input("Enter the song name:")
artist_name = st.text_input("Enter the artist name:")

# Step 3: OpenAI API Key Setup
# Replace 'your_openai_api_key' with your actual OpenAI API key
openai.api_key = "your_openai_api_key"

def get_song_recommendations(song_name, artist_name):
    """Fetches obscure song recommendations using OpenAI API"""
    prompt = f"Suggest 2-3 obscure songs similar to '{song_name}' by {artist_name}. Include a brief fact about each song or artist."  
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error fetching recommendations: {str(e)}"

# Step 4: Display Recommendations
if st.button("Get Recommendations"):
    if song_name and artist_name:
        st.info("Fetching recommendations...")
        recommendations = get_song_recommendations(song_name, artist_name)
        st.markdown(recommendations)
    else:
        st.warning("Please provide both a song name and an artist name.")

# Step 5: Future Enhancements Placeholder
st.sidebar.title("Future Enhancements")
st.sidebar.markdown("- Add user feedback system")
st.sidebar.markdown("- Integrate Spotify links")
st.sidebar.markdown("- Enable user profiles for tailored suggestions")

# Step 6: Deployment Instructions
# After testing locally, deploy this script to Streamlit Cloud.
# Link your GitHub repository containing this script to Streamlit Cloud for automatic deployment.


