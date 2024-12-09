import pandas as pd

# Cargar el archivo Excel en un DataFrame
wwc_matrix = pd.read_excel(r'src\WWC_questions.xlsx')

def filtrar_por_entidad(df, entidad):
    """
    Filtra el DataFrame por el valor de la columna 'ENTITY'.

    :param df: DataFrame a filtrar
    :param entidad: Valor de la entidad para filtrar
    :return: DataFrame filtrado
    """
    return df.loc[df['ENTITY'] == entidad]

# Ejemplo de uso
entidad_filtrada = filtrar_por_entidad(wwc_matrix, 'DAP')
print(entidad_filtrada['QUESTION'])