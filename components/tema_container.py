import streamlit as st
from components.file_uploader import recepcionar_archivos

def tema_container(tema):
    container = st.container()
    container.subheader(tema)
    recepcionar_archivos('**CRDM1. Implementación de la estrategia y la gobernanza de datos**', 
                         "*Su gobierno local mantiene una lista documentada de responsabilidades de estrategia y gobernanza de datos y se reúne al menos trimestralmente para cumplir dichas responsabilidades.*", 
                         "**DM1.1: El proceso de estrategia y gobernanza de datos tiene aprobación ejecutiva y se guía por una estrategia de datos de toda la ciudad, un acta constitutiva, una declaración de propósito o un conjunto documentado de objetivos y metas.**", 
                         "*Marco de equidad: Incluir un marco de equidad en la práctica de gobernanza de datos significa que los gobiernos locales están incorporando equidad en todas las etapas del proceso de gobernanza de datos: a medida que desarrollan sus estatutos, organizan el comité de gobernanza de datos, establecen un proceso de recopilación de datos que incluye casos de uso, designan conjuntos de datos, seleccionan administradores de datos y garantizan que los datos se utilicen de la manera más equitativa. Por ejemplo, los comités de gobernanza de datos pueden crear una política o proceso que aliente a los administradores de datos a cuestionar sus propios casos de uso de datos o garantizar que los datos recopilados coincidan con los casos de uso propuestos y explorar marcos más equitativos.*")
    return container
