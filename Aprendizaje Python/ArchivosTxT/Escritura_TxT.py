# Documentacion para la escritura de (textos planos)

# (.write) y ('w') Sobre escribir dentro de un texto plano
with open("Aprendizaje Python\\ArchivosTxT\\documento.txt",'w',encoding='UTF-8') as archivo:
    archivo.write("Es es una alteracion dentro del archivo")
    print(archivo)

# (.writelines) Sobre escritura en una cadena de un archivo de texto plano
with open("Aprendizaje Python\\ArchivosTxT\\documento.txt",'w',encoding='UTF-8') as escritura:
    escritura.writelines(["Oscar\n","Romero Romero\n"])
    escritura.writelines(["Se puden comular\n","En varias lineas\n"])
    print(escritura)

# ('a') ¡Crea de carpeta! y cuando se ejecuta simpre se imprimiera el resultado
with open("Aprendizaje Python\\ArchivosTxT\\documento.txt",'a',encoding='UTF-8') as repiticion:
    repiticion.writelines(["Copiar\n","Pegar\n"])
    print(repiticion)