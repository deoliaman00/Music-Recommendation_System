import streamlit as st
import pickle
import pandas as pd
import numpy as np
import import_ipynb
import Recommenders as Recommenders
import code as cd

song_df = pickle.load(open('song_df.pkl','rb'))

ir = Recommenders.item_similarity_recommender_py()
ir.create(song_df, 'user_id', 'song')
user_items = ir.get_user_items(song_df['user_id'][5])

def recommend(music):
    # give related songs based on the words
    # give related songs based on the words
    exp = ir.get_similar_items(music)
    exp1 = exp['song']
    return exp1.values






music_list = pickle.load(open('music_5.pkl','rb'))
musicS=pd.DataFrame(music_list)



st.title('Music recommendation system')
selected_music_name = st.selectbox(
'Welcome to my project: AMANDEOLI',musicS)

if st.button('Recommend more :)'):
    recommendations= recommend(selected_music_name)
    for i in recommendations:
        st.write(i)

