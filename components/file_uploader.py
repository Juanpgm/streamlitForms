import streamlit as st

def recepcionar_archivos(criterio,definicion,pregunta,producto):
    st.write("Por favor cargue las evidencias que cumplan el criterio definido en la pregunta")
    st.write(criterio)
    st.write(definicion)
    st.write(pregunta)
    st.write(producto)
    uploaded_files = st.file_uploader(
        "Cargue sus Archivos Aquí",accept_multiple_files=True
    )
    if uploaded_files:
        for uploaded_file in uploaded_files:
            bytes_data = uploaded_file.read()
            st.write("Nombre del Archivo:", uploaded_file.name)
            #st.write(bytes_data)
    
    return uploaded_files