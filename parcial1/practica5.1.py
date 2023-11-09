import pandas as pd

# Ruta del archivo Excel
excel = "parcial1/pandas.ods"
sheet_name = "Hoja1"

# Leer el archivo Excel en un DataFrame
df = pd.read_excel(excel, sheet_name=sheet_name)

# Imprimir el DataFrame
print(df)

# Obtener información sobre el DataFrame
print(df.info())

# Obtener tipos de datos de columnas
print(df.dtypes)

# Obtener el índice del DataFrame
print(df.index)

# Búsqueda de datos en la columna 0 (primera columna)
print(df.iloc[:, 0])

# Filtro para encontrar datos donde la columna 'Sexo' es igual a 'Hombre'
cons_hom = df["Sexo"] == 'Hombre'
df_hom = df[cons_hom]

# Imprimir las primeras filas del DataFrame resultante
print(df_hom.head())
