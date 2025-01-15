import streamlit as st
import openai

# Display the OpenAI Library Version
st.write(f"OpenAI Library Version: {openai.__version__}")

# OpenAI API Key from Streamlit secrets
openai.api_key = st.secrets["openai"]["api_key"]

# App Title
st.title("Song Recommendation App")

# User Input
song = st.text_input("Enter a song title:")
artist = st.text_input("Enter the artist's name:")

# Function to get recommendations using ChatCompletion
def get_recommendations(song, artist):
    # Return a dummy response for testing
    return f"Here are some dummy recommendations for '{song}' by {artist}: [Song A, Song B, Song C]"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7,
            max_tokens=200
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Display recommendations
if song and artist:
    st.write(f"You entered: {song} by {artist}")
    st.write("Fetching recommendations...")
    recommendations = get_recommendations(song, artist)
    st.write(recommendations)
else:
    st.write("Please enter a song and artist to get started.")
