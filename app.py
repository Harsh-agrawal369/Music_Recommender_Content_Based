import streamlit as st
import numpy as np
import pickle as pk
import pandas as pd
import requests

st.title("Music Recommender System")

music_list = pk.load(open("musicrec.pkl", "rb"), encoding='utf-8')
music = pd.DataFrame(music_list)

similarity = pk.load(open("similarities.pkl", "rb"), encoding='utf-8')


def recommended(selected_music):
    music_index = music[music['title'] == selected_music].index[0]
    distances = similarity[music_index]
    music_list_recommended = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:7]

    recommended_music = []

    for i in music_list_recommended:
        music_tit = music.iloc[i[0]]
        recommended_music.append(music_tit)
    
    return recommended_music


Selected_music = st.selectbox(
    "Select your music:",
    music['title'],
    index=None,
    placeholder="Select music..."
)


if st.button("Recommend"):
    Recommended_music = recommended(Selected_music)
    
   
    recommended_df = pd.DataFrame(Recommended_music)
    
    # Drop the 'tags' column
    recommended_df = recommended_df.drop(columns=['tags'])
    
    recommended_df = recommended_df.rename(columns={'title': 'Song'})
    recommended_df = recommended_df.rename(columns={'Singer/Artists': 'Artist'})
    recommended_df = recommended_df.rename(columns={'Album/Movie': 'Album'})
    
    # Display the DataFrame as a table without index numbers
    st.dataframe(recommended_df)
