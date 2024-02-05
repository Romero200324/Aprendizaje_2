# Sección de ejercicios de PANDA
import pandas as pd

# (pd) importación de la libreía de panda
print("(pd) importación de la libreía de panda".upper())
#1 Escribir un programa que pregunte al usuario por las ventas de un rango de 
# años y muestre por pantalla una serie con los datos de las ventas indexada por los años,
#  antes y después de aplicarles un descuento del 10%.

def registro_de_ventas ():
    df = pd.read_csv("ArchivosCSV\\Pandas\\ventas_del_empresa.csv")
    df_años = ["Años" ]
    return df,df_años

df_valor = registro_de_ventas()
print(df_valor)

#2
#3 

# (.read_csv) Atributo de panda (Para leer archivos)
print("|.read_csv| Atributo de panda - Para leer archivos-".upper())

#1 Exportacion y visualización de los datos que esta en otras carpetas...



localizacion = pd.read_csv("ArchivosCSV\\datos.csv")
print(f"""La localización de tu satos fueron :
{localizacion}""")

#2
#3 


# (df) Para el data (framework) Más utilizado ocurrente para la programción.
print("(df) Para el data (framework)".upper())

#1 
#2
#3 

# ([" "]) Impresión de unarchivo especifico
print("([" "]) Impresión de unarchivo especifico".upper())
#1
#2
#3 
