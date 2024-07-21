#Importe las bibliotecas que pidio esto sirve para manejar los datos
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import StringIO

# Pidio que lo hicieramos del distrito de donde era, yo soy de El Agustino
data = """
45185,150111,"LIMA","LIMA","EL AGUSTINO",202003,21,2,86,71,15
45188,150111,"LIMA","LIMA","EL AGUSTINO",202004,1355,120,192,59,133
45193,150111,"LIMA","LIMA","EL AGUSTINO",202005,3470,320,446,55,391
45194,150111,"LIMA","LIMA","EL AGUSTINO",202006,1630,193,296,63,233
45198,150111,"LIMA","LIMA","EL AGUSTINO",202007,1482,154,194,68,126
45202,150111,"LIMA","LIMA","EL AGUSTINO",202008,2248,155,209,66,143
45203,150111,"LIMA","LIMA","EL AGUSTINO",202009,1335,82,151,67,84
45206,150111,"LIMA","LIMA","EL AGUSTINO",202010,1793,38,113,64,49
45209,150111,"LIMA","LIMA","EL AGUSTINO",202011,667,25,100,69,31
45212,150111,"LIMA","LIMA","EL AGUSTINO",202012,392,30,95,66,29
45179,150111,"LIMA","LIMA","EL AGUSTINO",202101,1037,116,199,79,120
45181,150111,"LIMA","LIMA","EL AGUSTINO",202102,1534,212,303,63,240
45184,150111,"LIMA","LIMA","EL AGUSTINO",202103,1609,216,310,71,239
45189,150111,"LIMA","LIMA","EL AGUSTINO",202104,1256,212,294,59,235
45191,150111,"LIMA","LIMA","EL AGUSTINO",202105,546,90,174,55,119
45196,150111,"LIMA","LIMA","EL AGUSTINO",202106,235,44,119,63,56
45197,150111,"LIMA","LIMA","EL AGUSTINO",202107,147,14,108,68,40
45200,150111,"LIMA","LIMA","EL AGUSTINO",202108,115,9,91,66,25
45204,150111,"LIMA","LIMA","EL AGUSTINO",202109,128,10,97,67,30
45207,150111,"LIMA","LIMA","EL AGUSTINO",202110,114,9,97,64,33
45210,150111,"LIMA","LIMA","EL AGUSTINO",202111,236,8,89,69,20
45213,150111,"LIMA","LIMA","EL AGUSTINO",202112,435,13,96,66,30
45180,150111,"LIMA","LIMA","EL AGUSTINO",202201,8172,36,135,79,56
45182,150111,"LIMA","LIMA","EL AGUSTINO",202202,759,19,94,63,31
45186,150111,"LIMA","LIMA","EL AGUSTINO",202203,88,8,97,71,26
45190,150111,"LIMA","LIMA","EL AGUSTINO",202204,24,8,93,59,34
45192,150111,"LIMA","LIMA","EL AGUSTINO",202205,35,8,90,55,35
45195,150111,"LIMA","LIMA","EL AGUSTINO",202206,187,4,95,63,32
45199,150111,"LIMA","LIMA","EL AGUSTINO",202207,1577,7,95,68,27
45201,150111,"LIMA","LIMA","EL AGUSTINO",202208,1047,13,98,66,32
45205,150111,"LIMA","LIMA","EL AGUSTINO",202209,145,10,71,67,4
45208,150111,"LIMA","LIMA","EL AGUSTINO",202210,34,4,66,64,2
45211,150111,"LIMA","LIMA","EL AGUSTINO",202211,1127,5,67,69,-2
45214,150111,"LIMA","LIMA","EL AGUSTINO",202212,1011,10,66,66,0
45178,150111,"LIMA","LIMA","EL AGUSTINO",202301,55,7,67,79,-12
45183,150111,"LIMA","LIMA","EL AGUSTINO",202302,25,5,51,63,-12
45187,150111,"LIMA","LIMA","EL AGUSTINO",202303,37,0,45,71,-26
"""

# Convertir los datos a un DataFrame, aquí recíen descrubri lo que eso era
# Me sirvio para guardar distintos tipos de datos en columnas
data_io = StringIO(data)
columns = ["ID", "Ubigeo_INEI", "Departamento", "Provincia", "Distrito", "Fecha", "Casos", "Fallecidos", "Fallecidos_SINADEF", "Fallecidos_2019", "Exceso_Muertes"]
df = pd.read_csv(data_io, header=None, names=columns)

# Esto tambien me sorprendio, lo organiza para el grafico
print(df.head())
print(df.info())
print(df.describe())

# Por si aca para eliminar las filas sin contenido
df_cleaned = df.dropna()

# Convertir la columna Fecha a formato datetime para poder manipularlas
df_cleaned['Fecha'] = pd.to_datetime(df_cleaned['Fecha'].astype(str), format='%Y%m')
#Me permite utilizar los años y meses
df_cleaned['Año'] = df_cleaned['Fecha'].dt.year
df_cleaned['Mes'] = df_cleaned['Fecha'].dt.month

# Me permite agruparlo y sumar para cada caso, esto me permite comparar 
# y como fue evolucionando el número de casos
casos_mes = df_cleaned.groupby(['Año', 'Mes'])['Casos'].sum()
#Esta parte si se me complico demasiado, no entendia muy bien así que pedi ayuda
# Convertir el índice de 'casos_mes' a formato datetime para la gráfica
casos_mes.index = pd.to_datetime(casos_mes.index.map(lambda x: f"{x[0]}-{x[1]:02d}-01"))

# Lo que va a imprimir
plt.figure(figsize=(12,6)) #tamaño del gráfico
plt.plot(casos_mes.index, casos_mes.values, marker='o') #me permite graficar las líneas
plt.title('Evolución de la pandemia en El Agustino')
plt.xlabel('Fecha')
plt.ylabel('Número de casos')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
