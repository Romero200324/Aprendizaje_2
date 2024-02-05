# Documentacion (Importacion de Archivos CSV)

# (csv) importacion 
import csv

#(with) Para abrir un dato CSV 
# (.reader()) Para archivos csv
with open("Aprendizaje Python\\ArchivosCSV\\datos.csv") as archivo:
    valor = csv.reader(archivo)
    for i in  valor:
        print(i) 