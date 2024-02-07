# Documentacion  de datos (PANDAS)

# (pd) importacion de libreria de pandas
import pandas as pd
linas_divicibas = "------------------------------------------"

print(linas_divicibas) # Ignorar estas lineas de programcion

# (.read_csv) Atributos de la libreria de (Pandas) 
archivos = pd.read_csv("Aprendizaje Python\\ArchivosCSV\\datos.csv")
print(archivos)

print(linas_divicibas)
# (df) Es la data (framework) # Forma más común en la programación 
df = pd.read_csv("ArchivosCSV\\datos.csv")
df2 = pd.read_csv("ArchivosCSV\\Pandas\\ventas_del_empresa.csv")
print(df)

print(linas_divicibas)
#([" "]) Impresión de un valor espeficico 
nombres = df["nombres"]
print(f"Esta es la lista de nombre:\n{nombres}") 

print(linas_divicibas)

# names =[""] Cambio de nombre o asignación de nombre a nuevos datos..
dfs = pd.read_csv("ArchivosCSV\\datos.csv", names = ["name","lastname","age"])
print(f"""Los datos ahora se llamaran : 
{dfs}""")

print(linas_divicibas)

# [:] Asignación de la lectura en lo tipo de datos de cadena
cadena_de_numeros = "12345678910"
print(cadena_de_numeros[1:8])

print(linas_divicibas)

# Ejemplo_de_data (framework) para ordenar los valores:
edades = df["edades"]
print(f"""Petición de datos del rango serán: 
{edades[:2]}""")

print(linas_divicibas)
# (sort_values) Oredanamiento de (Menor a Mayor) en los valores en los números
df_acendete = df.sort_values("edades")

print(f"""Ordenación correcta de los datos de mayor valor y menor valor son :
{df_acendete[:2]}""")

print(linas_divicibas)

# (ascending=False) Para ordenar los valores de forma desedente
df_decendente = df.sort_values("edades",ascending=False)

print(f"""Los valore de forma decendente: 
{df_decendente} """)


print(linas_divicibas)

# (.concat) Concatenación de datos 
df_concatenacion_de_valores = pd.concat([df,df2])
print(f"Concatenación de 2 dataframes:\n{df_concatenacion_de_valores}") 

print(linas_divicibas)

# (.head) Parametro de pandas para mostrar un contenido especifico.
fila_uno = df2.head(3)
print(f"Primeras filas son:\n{fila_uno}") 

print(linas_divicibas)

# (.tail) Parametro para las ultimas filas...
final_de_filas = df2.tail(3)
print(f"Las ultimas filas son:\n{final_de_filas}")

print(linas_divicibas)

# (shape) Es una metodo para aceder a valores especificos..
# Desempaquetado..
filas_totales,columnas_totales = df2.shape

print(f"El numero de finas son:\n{filas_totales} \nY el número de columnas son: \n{columnas_totales}")

print(linas_divicibas)

print("Ciencía de datos".upper())

# (.describe) Estadistica de los datos extraidos del dataframe...
df_informacion = df2.describe()
print(f"Las estadisticas de lso datos son:\n{df_informacion}")

print(linas_divicibas)

# (.loc[ ]) Acceder a un dato especifico de un valor...
valor_especifico = df2.loc[2,"No ventas"]
print(valor_especifico)

print(linas_divicibas)

# (.iloc[ ]) Acceder deacuerdo a su indice de su valor...
indice_especifico = df2.iloc[2,2]
print(indice_especifico)

print(linas_divicibas)

# (.iloc[:,0]) Acceder a todos los elementos de una columna
elementos_total_columna = df2.iloc[:,5]
print(f"Los elementos total de la columna de nombress son:\n{elementos_total_columna}")

print(linas_divicibas)

# (.loc[2,:]) Acceder a todos elemtnos de uan fila
total_de_elementos_de_fila = df2.loc[2,:]
print(f"Total de elememntos de una fila {total_de_elementos_de_fila}")

print(linas_divicibas)

# Filas aplicando con condiciones...

 
import random as emplado_ranmdon
nombres_ganadores = df2.loc[df2["Cantidad de ventas en total"]>20,:]
nombres_ganadores = df2.loc[:5]
print(f"¡¡ Felicitaciónes Ustedes son los gandores del mes !!:\n{nombres_ganadores}".upper())

print(linas_divicibas)

ganador_de_premio_mayor = emplado_ranmdon.randrange(0,5)
referencia = df2.loc[ganador_de_premio_mayor,:]
print(f"El premio mayor es para el numero de empleado:\n{ganador_de_premio_mayor}\nY sus resultados son:\n{referencia}")

