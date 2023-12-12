# pages/streamlit_interface.py

import streamlit as st

def display_configuration_form():
    st.title('Configuración del Proceso')

    filter_type = st.selectbox('Seleccione el tipo de filtro:', ['Class 1', 'Class 2', 'Class 3', 'Square 3x3', 'Edge 3x3', 'Square 5x5', 'Edge 5x5', 'Sobel', 'Laplace', 'Prewitt'])
    num_threads = st.slider('Número de hilos:', 1, 10, 1)
    programming_language = st.selectbox('Seleccione herramienta para filtrado:', ['C', 'OpenMP', 'Multiprocessing', 'MPI4PY', 'PyCUDA'])

    # Devolver los tres valores
    return filter_type, num_threads, programming_language


def display_results(processed_images):
    st.title('Resultados del Procesamiento')

    for i, result in enumerate(processed_images[:10]):
        st.subheader(f'Imagen {i+1}')
        st.text(f'Dimensiones: {result["dimensions"]}')
        st.text(f'Valor Mínimo: {result["min_value"]}')
        st.text(f'Valor Máximo: {result["max_value"]}')
        st.text(f'Valor Medio: {result["mean_value"]}')
        st.text(f'Desviación Estándar: {result["std_deviation"]}')