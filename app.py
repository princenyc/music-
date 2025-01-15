import streamlit as st
import openai

# Title and instructions
st.title("🎵 AI Music Recommendation App")
st.write("Enter a song and artist to discover similar but obscure tracks!")

# User input fields
song = st.text_input("Enter the song name", placeholder="Enter the song name", key="song_input")
artist = st.text_input("Enter the artist's name", placeholder="Enter the artist's name", key="artist_input")

# OpenAI API Key (Replace 'YOUR_API_KEY' with your actual key)
openai.api_key = "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"

# Function to get recommendations
def get_recommendations(song, artist):
    prompt = f"Recommend 2-3 obscure songs similar to '{song}' by '{artist}'."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip().split("\n")

# Button to submit
if st.button("Get Recommendations", key="recommend_button"):
    if song and artist:
        st.write(f"Searching for recommendations based on: **{song}** by **{artist}**")
        try:
            recommendations = get_recommendations(song, artist)
            st.write("### Recommendations:")
            for rec in recommendations:
                st.write(f"- {rec}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please provide both song and artist.")
