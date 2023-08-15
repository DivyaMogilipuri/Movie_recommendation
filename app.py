import streamlit as st
import pickle
import pandas as pd
import requests
def get_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8b1af3571278bf236d456ae85f147ea1&language=en-US%22'.format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w300/"+data['poster_path']


st.title("Movie Recommender System")
movies_dict=pickle.load(open("movies_dict.pkl",'rb'))
similarity=pickle.load(open("similar.pkl",'rb'))
movies_df=pd.DataFrame(movies_dict)
option=st.selectbox('search Movies here ',movies_df['title'].values)


def recommond(movie,new):
    movie_index = new[new['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    r_list=[]
    r_id=[]
    r_posters=[]
    for i in movie_list:
        r_list.append(new.iloc[i[0]].title)
        r_id.append(new.iloc[i[0]].id)

        r_posters.append(get_poster(new.iloc[i[0]].id))

    return r_list,r_id,r_posters
if st.button("Recommend"):
    movie_rec,movie_id,posters=recommond(option,movies_df)
    #for i in movie_rec:
        #t.write(i)

movie_rec,movie_id,posters=recommond(option,movies_df)





col1, col2 = st.columns(2,gap="medium")

with col1:
   st.write(movie_rec[0])
   st.image(posters[0])

with col2:
   st.write(movie_rec[1])
   st.image(posters[1])

col4,col5,col3= st.columns(3)
with col3:
   st.write(movie_rec[2])
   st.image(posters[2])
with col4:
   st.write(movie_rec[3])
   st.image(posters[3])

with col5:
   st.write(movie_rec[4])
   st.image(posters[4])

