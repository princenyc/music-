import streamlit as st
import openai

# OpenAI API Key
OPENAI_API_KEY = "your_openai_api_key"  # Replace with your API key
openai.api_key = OPENAI_API_KEY

# App Title
st.title("Song Recommendation App")

# User Input
song = st.text_input("Enter a song title:")
artist = st.text_input("Enter the artist's name:")

# Function to get recommendations
def get_recommendations(song, artist):
    prompt = (
        f"Suggest 2-3 obscure songs that are similar to '{song}' by {artist}. "
        "Include the song title, artist name, a link (if available), and trivia about the artist."
    )
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150,
            temperature=0.7
        )
        return response.choices[0].text.strip()
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
