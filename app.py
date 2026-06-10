
import kagglehub
import os
import pickle
import streamlit as st
import pandas as pd
from pyngrok import ngrok

st.set_page_config(
    page_title="Analisis Sentimen Review Tokopedia",
    page_icon="📊",
    layout="wide",
)

@st.cache_resource
def load_model():
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

model = load_model()

st.title("Analisis Sentimen Review Tokopedia")
st.write('Masukkan Ulasan Pelanggan Untuk Memprediksi Kategori Sentimen')

review = st.text_area(
    "Masukkan Ulasan",
    height=150,
    placeholder='Contoh: Kualitas barang bagus dan seller responsif'
)

if st.button('Prediksi'):

  if review.strip() == "":
    st.warning('Ulasan Kosong. Masukkan Ulasan Terlebih Dahulu!')
  else:
    prediction = model.predict([review])[0]

    st.subheader('Hasil Prediksi:')
    
    if prediction == 'positive':
        st.success('Sentimen: Positive ')

    elif prediction == 'neutral':
        st.info('Sentimen: Neutral')
    else:
        st.error('Sentimen: Negative')

