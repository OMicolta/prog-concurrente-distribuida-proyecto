import streamlit as st
from src.images import download_images_concurrent

if __name__ == '__main__':
    query = st.text_input('Temática:')
    num_images = st.number_input('Cantidad de imagenes deseadas:', min_value=1, max_value=10000, step=1)
    if st.button('Download Images'):
        progress_bar = st.progress(0)
        status_text = st.empty()
        download_images_concurrent(query, num_images)
        progress_bar.progress(100)
        status_text.text('Descarga completada!')

