# Docuemntacion necesario para aprender de pandas

### > Exportacion de los datos en la implementacion de pandas

![iamgen](https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Pandas_logo.svg/1200px-Pandas_logo.svg.png)

***Los archivos que se puden exporta son:***
- CSV
- XLS
- PARQUET
- HTML
- HDF5
- JSON
- GBQ 
- SQL 


**DATAFREN**: 
Esto quiere decir que al momento de ejecutar el archivo lo tratara como una tabla con diferentes valores que lo componen..
 
### > Codigo de pandas

``` python
# importacion de la libreria pandas 
> import pandas as pd

// Asignacion del archivo en una variable
> df = pd.read_csv("Nobre_del_archivo")
> df
 # Nos muestra las 5 filas de los datos
> df.head() 

# Nos muetra las ultimas 10 filas de datos 
> df.tall() #Definicion de valores a costrar sera de el numero en el parentecis

# Encontrar la medias, medio y clasificacion de valores 
> df.describe()

# Limpieza de datos eliminacion de los datos que son "NAN" 
> df.dropna()

# Remplazo de valores de NAN con otros valores numericos
> df.fillna(0)

# LLenados de datos en tablas de NAN
> df.fillna("Nobre de la columna":numero, "Nombre de la columna":numero en que remplazar)

# Filtrado de datos de una columna
> df["Nombre de la comlumna"]

# Filtrar varias comlumnas 
> df.[["Nombre de la comlumna 1", "Nombre de la comlumna 2"]]

# Filtracion de las filas 
> df.iloc[0]
>
>
>
>
>
>
>



```
