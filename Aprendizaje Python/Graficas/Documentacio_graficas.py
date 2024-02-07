# Seccion para trabajar con graficas 
# IMPOTACION DE LIBRERIAS...
import pandas as pd
import matplotlib.pyplot as plt # Libreria para visulizacion de dartos. 
import seaborn as sns # Visualizacion de datos en conjuntos.


# Importacion de archivo ó archivos 
df = pd.read_csv("Aprendizaje Python\\Graficas\\Document\\puebla_2023.csv") 

# (sns.lineplot(x="",y="")) visulizacion de datos en conjuntos
sns.lineplot(x = "Mes",y ="Llegada de turistas",data = df)

# Remarcar datos importante dentro de la grafica 
plt.plot("Mayo",275,"o")

# Mostrar la grafica final 
plt.show()


print("---------------\ncodigo para hacer una grafica de barras\n--------------- ".upper())

# Crecion de diagramas de barras:

barras = pd.read_csv("Aprendizaje Python\\Graficas\\Document\\puebla_2023.csv")

# (sns.barplot(x="",y=""))
sns.barplot(x="Mes",y="Porcentaje de ocupación",data = barras)

# Mostrar la grafica final 

suma_de_datos = df ['Porcentaje de ocupación'].sum() # Metodo aplicado...
print(f"La cantidad de ocupaciones es en tota: {suma_de_datos}")

plt.show()


print("---------------\ncodigo para hacer una grafica de puntos\n--------------- ".upper())

# Creacion de diagrama de punto:
sns.scatterplot(x="Llegada de turistas",y="Año",data=barras)

# Imprecion de la grafica 
plt.show()

print("---------------\ncodigo para hacer una grafica de bigotes(Box)\n--------------- ".upper())

# Union de conjuntos
sns.boxplot(x="Mes",y="Estadía Promedio",data=df)

# Imprecion de grafica final 
plt.show()