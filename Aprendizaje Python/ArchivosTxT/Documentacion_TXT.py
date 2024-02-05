# Documentacion de archivos txt

# (open()) Abrir un archivo de tipo "texto plano"
archivo = open("ArchivosTxT\\documento.txt")

# (,encoding = 'UTF-8') Correcion de letras extrañas
archivo = open("ArchivosTxT\\documento.txt",encoding='UTF-8')

# (.read()) Leer archivo text
print(f"""
      
      {archivo.read()}
      
      Termino de lectura 

      """)

 
Archivo_preparado = open("ArchivosTxT\\documento.txt",encoding='UTF-8')

# (.readlineas()) Leer lineas por lineas
lineas = Archivo_preparado.readlines()
print(f"""
            Para leer todo en una sala linea : 
                    {lineas}""")


Archivo_preparado_una_linea = open("ArchivosTxT\\documento.txt",encoding='UTF-8')

# (.readlinea()) Leer solo una linea
una_linea = Archivo_preparado_una_linea.readline()
print(f"""
            Lecutura solo una linea: 
                    {una_linea}""")

Archivo_preparado_letras = open("ArchivosTxT\\documento.txt",encoding='UTF-8')

# (.readlinea(1)) Leer solo una linea
letras = Archivo_preparado_letras.readline(2)
print(f"""
            Lectura por letras: 
                    {letras}""")

# (close) Cerrar el archivo tipo texto plano
archivo.close()
Archivo_preparado.close()
Archivo_preparado_una_linea.close()
Archivo_preparado_letras.close()
