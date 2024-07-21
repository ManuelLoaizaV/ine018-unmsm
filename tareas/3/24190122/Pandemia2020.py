import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos desde el archivo CSV
df = pd.read_csv('datos_pandemia.csv', sep=';')

# Verificar los primeros registros cargados
print(df.head())

# Calcular estadísticas
total_casos = df['Casos'].sum()
total_muertes = df['Muertes'].sum()
total_muertes_totales = df['Muertes totales'].sum()

# Calcular porcentajes si es necesario
df['Contagios (%)'] = (df['Casos'] / df['Poblacion']) * 100
df['Mortalidad (%)'] = (df['Muertes'] / df['Casos']) * 100
df['Muertes Covid (%)'] = (df['Muertes'] / df['Muertes totales']) * 100

# Visualización de datos (ejemplo de gráfico de barras)
plt.figure(figsize=(12, 6))

# Gráfico de barras de contagios por provincia
plt.subplot(1, 3, 1)
plt.bar(df['Provincia'], df['Contagios (%)'], color='skyblue')
plt.title('Contagios por provincia')
plt.xlabel('Provincia')
plt.ylabel('Contagios (%)')
plt.xticks(rotation=45)

# Gráfico de barras de mortalidad por provincia
plt.subplot(1, 3, 2)
plt.bar(df['Provincia'], df['Mortalidad (%)'], color='salmon')
plt.title('Mortalidad por provincia')
plt.xlabel('Provincia')
plt.ylabel('Mortalidad (%)')
plt.xticks(rotation=45)

# Gráfico de barras de muertes Covid por provincia
plt.subplot(1, 3, 3)
plt.bar(df['Provincia'], df['Muertes Covid (%)'], color='lightgreen')
plt.title('Muertes Covid por provincia')
plt.xlabel('Provincia')
plt.ylabel('Muertes Covid (%)')
plt.xticks(rotation=45)

# Ajustes de diseño y mostrar gráficos
plt.tight_layout()
plt.show()