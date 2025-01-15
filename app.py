import streamlit as st
import openai

st.title("🎵 AI Music Recommendation App")
st.write("Enter a song and artist to discover similar but obscure tracks!")

song = st.text_input("Enter the song name", placeholder="Enter the song name", key="song_input")
artist = st.text_input("Enter the artist's name", placeholder="Enter the artist's name", key="artist_input")

openai.api_key = "your_actual_api_key_here"

def get_recommendations(song, artist):
    try:
        prompt = f"Recommend 2-3 obscure songs similar to '{song}' by '{artist}'."
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant for song recommendations."},
                {"role": "user", "content": prompt}
            ]
        )
        return response['choices'][0]['message']['content'].strip().split("\n")
    except Exception as e:
        return [f"Error occurred: {e}"]

if st.button("Get Recommendations", key="recommend_button"):
    if song and artist:
        st.write(f"Searching for recommendations based on: **{song}** by **{artist}**")
        recommendations = get_recommendations(song, artist)
        st.write("### Recommendations:")
        for rec in recommendations:
            st.write(f"- {rec}")
    else:
        st.warning("Please provide both song and artist.")

