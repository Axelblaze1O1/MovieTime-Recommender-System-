import streamlit as st
import pickle
import pandas as pd
import requests





def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    ml = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []

    for i in ml:
        movie_id = i[0]
        recommended_movies.append(movies.iloc[movie_id].title)

    return recommended_movies


movies_list = pickle.load(open('movies_d.pkl', 'rb'))
movies = pd.DataFrame(movies_list)
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')
selected_movie_name = st.selectbox('Select a Movie !!', movies['title'].values)

if st.button('Show Recommendation'):
    recommended_movie_names = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])

    with col2:
        st.text(recommended_movie_names[1])


    with col3:
        st.text(recommended_movie_names[2])

    with col4:
        st.text(recommended_movie_names[3])

    with col5:
        st.text(recommended_movie_names[4])

