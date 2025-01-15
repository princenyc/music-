import streamlit as st

# App Title
st.title("Song Recommendation App")

# User Input
song = st.text_input("Enter a song title:")
artist = st.text_input("Enter the artist's name:")

# Placeholder for recommendations
if song and artist:
    st.write(f"You entered: {song} by {artist}")
    st.write("Recommendations will appear here soon!")
else:
    st.write("Please enter a song and artist to get started.")
