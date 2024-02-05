# Ejercicios para graficar los datos...

# (sns.lineplot(x="",y="")) Visualizacion de datos de conjunyos 

#1 Ejercicio 1
# Escribir un programa que pregunte al usuario por las ventas
#de un rango de años y muestre por pantalla un diagrama de líneas con la evolución de las ventas.

import pandas as pd
import matplotlib.pyplot as plt # Uninon de datos en conjuntos..
import seaborn as sns # visualizacion de datos '

# Importacion de archivos 
#df= pd.read_csv("Aprendizaje Python\\Graficas\\Document\\librerias.csv")
# Union de conjuntos 
#sns.lineplot(x="consecutivo",y="estado",data=df)
# visulizacion de datos.
#plt.show()

#2 Ejercicios de Banco es :


# Lectura de archivos sera:
df = pd.read_csv("Aprendizaje Python\\Graficas\\Document\\bancos.csv")
# Union de datos 
sns.barplot(x="Apertura",y="Cierre",data=df)
# Imprecion de datos y resultado final 
plt.show()


#3