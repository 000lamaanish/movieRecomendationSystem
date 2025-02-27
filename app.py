import streamlit as st
import pickle

movies=pickle.load(open('movies.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))
movies_list=movies['title'].values

st.header('Movie Recommender System')
st.selectbox("Select movies from dropdown", movies_list)

def recommend(movie):
    movie_index = movies[movie['title']==movie].index[0]
    distances = similarity[movie_index]
    movies_list=sorted(list(enumerate(similarity[0])),reverse=True,key=lambda x:x[1])[1:5]
    recommend_movie=[]
    
    for i in movies_list:
        recommend_movie.append(movies.iloc[i[0]].title)
    

