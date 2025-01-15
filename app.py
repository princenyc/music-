import streamlit as st

# Title and instructions
st.title("🎵 AI Music Recommendation App")
st.write("Enter a song and artist to discover similar but obscure tracks!")

# User input fields
song = st.text_input("Song Name", placeholder="Enter the song name")
artist = st.text_input("Artist Name", placeholder="Enter the artist's name")

# Button to submit
if st.button("Get Recommendations"):
    st.write(f"Searching for recommendations based on: **{song}** by **{artist}**")
import streamlit as st

# Title and instructions
st.title("🎵 AI Music Recommendation App")
st.write("Enter a song and artist to discover similar but obscure tracks!")

# User input fields
song = st.text_input("Song Name", placeholder="Enter the song name")
artist = st.text_input("Artist Name", placeholder="Enter the artist's name")

# Button to submit
if st.button("Get Recommendations"):
    st.write(f"Searching for recommendations based on: **{song}** by **{artist}**")
