import streamlit as st
from components.selectbox import entitiesSelectionBox

def main():
    st.title("What Work Cities - Santiago de Cali")
    st.write("Formulario de inscripción para la generación de inventarios para el programa de certificación de ciudades inteligentes")
    #st.subheader("Por favor selecciona tu entidad u organismo", divider="gray")
    entity = entitiesSelectionBox()
    # Mostrar advertencia solo si se ha seleccionado una entidad
    if entity:
        st.warning(f"**Entidad seleccionada:** {entity}", icon="⚠️")
    st.button("Siguiente")

if __name__ == "__main__":
    main()