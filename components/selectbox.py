import streamlit as st
from src.entities import entitiesSelection

# Agregar un dropdown
def entitiesSelectionBox():
    st.subheader("Por favor selecciona tu entidad u organismo", divider="gray")
    entity = st.selectbox(
        'Selecciona una opción: ',
        entitiesSelection,
        index=None,
        placeholder='Selecciona una entidad',
    )
    return entity