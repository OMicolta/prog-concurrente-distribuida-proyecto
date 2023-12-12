# main.py

import streamlit as st
from src.image_downloader import download_images_concurrently
from src.image_processing import apply_filters_and_statistics
from pages.streamlit_interface import display_configuration_form, display_results

if __name__ == '__main__':
    st.title('Proyecto Final - Programación Concurrente y Distribuida')

    query = st.text_input('Temática:')
    num_images = st.number_input('Cantidad de imágenes deseadas:', min_value=1, max_value=10000, step=1)
    filter_type, num_threads, programming_language = display_configuration_form()

    if st.button('Descargar e Procesar Imágenes'):
        progress_bar = st.progress(0)
        status_text = st.empty()

        try:
            # Realizar la búsqueda de imágenes con Bing Image Downloader
            from bing_image_downloader import downloader
            img_paths = downloader.download(query, limit=num_images, output_dir='data')

            # Descargar imágenes
            download_images_concurrently(img_paths, num_images, 'data')

            # Aplicar filtros y calcular estadísticas
            processed_images = apply_filters_and_statistics(img_paths, filter_type)

            # Mostrar resultados en la interfaz
            display_results(processed_images)

            # Actualizar la barra de progreso y el estado
            progress_bar.progress(100)
            status_text.text('Proceso completado!')

        except Exception as e:
            # Manejar errores y mostrar mensaje de error
            progress_bar.progress(0)
            status_text.text(f'Error: {e}')
