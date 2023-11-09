import pandas as pd

#datos = {"Nombres" :['Maria','Juan'],
         #"Edad":[18,20],
         #"Grado":["4A","4B"],
         #"Correo":["maria@gmail.com","juan@gmail.com"]}

#df = pd.DataFrame(datos)
#print(df)

# IMPORTAR DEL EXCEL
excel = "parcial1/pandas.ods" 
sheet_name ="Hoja1"
df = pd.read_excel(excel,sheet_name)
print(df)

