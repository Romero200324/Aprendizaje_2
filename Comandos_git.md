# Los Comandos de git :
[***Contenido de datos..*** ](https://www.markdownguide.org/getting-started/)

![Imagenes](https://images.datacamp.com/image/upload/v1651047046/image8_0e61d0dad8.png)

[***>>Mas comados la paginan de ("md")<<***](https://www.markdownguide.org/getting-started/)

[***>>Mas comandos de (git)<<***](https://git-scm.com/doc)

### Saber nuestra ubicacion:

> ls / dir 

### Localizacion actual en la carpeta en la que nos encotramos:
> pwd

###  Agregacion de una nueva ruta en donde inicio de (git init):

> git config --global --add safe.directory "Ruta del directorio"

## Creacion de una huella de tipo "ssh" 
> $ ssh-keygen -t ed25519 -C "oro0069074@gmail.com"

## Inicio de seccion de git a GitHub
> $ ssh -T git@github.com

### Nos permite ver el contenido de fichero:

> cat nombre del archivom completo

### Nos lleva a la ruta de carpetas y demas en cuestion:

> cd Ruta del archivo ("Ficheros")

### Te lleva al ultimon fichero que estabas:

> cd - 

### Ver todos los archivos como una lista en donde incluye el usuario, grupo, permisos sobre el archivo, tamaño, fecha y hora de creación :

> ls -l

### Borrar un archivo o carpeta:

> rm nobre del archivo

### Copiar archivos 

> cp nombre del fiquero / donde lo queremos mover 

### Ver historial de comandos ejecutados
> history

### Creacion de una carpeta sera el siguiente comando:

> mkdir "Nombre de la carpeta"

### Entrar a Visual Studio Code:
> code .

### @ COMANDOS DE GIT 

### Para ver las verciones del git que tenemso usamos : 
> git -v

### Para saber los comandos de git o saber que hacen los comandos:
> git -h

### Configuracion para comenzar con git se usa el comando pueda controlar uso personal

> git config --global user.name "OscarRomero"

### La agregacion del emil desde la consala

> git config --global user.emil "oro0069074@gmail.com"

### CREACION DE UNFICHERO DESDE LA CONSALA...

> touch helloword.py

### Limpieza la consola 

> clear 

### COMANDOS PARA LA CONSOLA DE GIT (Inicio de un documento) nuevo..

> git init 


### CAMBIO DE NOMBRE DE LA RAMA MAESTRA SERA LO SIGUIENTE

> git branch -m main


### PARA OBSERVAR LOS CAMBIOS QUE YA SEAN HECHO ANTES..

> git status


### Para tomar las fotos del codigo se implementara el codigo..

> git add nombredelfichero
 

### REALIZACION DE YA DE LA FOTOGRAFIA DEL CODIGO

> git commit


### ASIGNACION DE UN COMENTARIO INICIAL DE FORMA RAPIDA\

> git commit -m comentario que queremos que tenga


### MOSTRACION LAS PERSONA QUEAN MODIFICADO LOS ARCHIVOS
> git log


### PARA COLOCARNO EN UN PUNTO CONCRETO DEL PROGRAMA QUE EMOS DESARROLLADO

> git checkout nombre del fichero


###  PARA LA REGRECION DE LA ULTIMA FOTOGRAFIA 

> git reset


### SOLO PARA HACER UN CHEQUEO RAPIDO DEL FICHERO EN CUESTION 

> git checkout nombre del fiquero que queremos ver


### LA MENERA DE VER DE DIFERENTES LAS EDITACIONES HECHAS

> git log --graph


### DEMENERA MAS RAPIDA Y EN UNA SOLA LINEA DE CODIGO

> git log --graph --pretty=oneline


### DECORACION DEL CODIGO PARA SER MAS FACIL SU ENTENDIMIENTO

> git log --graph --decorate --all --oneline


### CREACION DE UN ALIAS PARA SER MAS FACIL SU USO

> git config --global alias.nombre que eligamos "Comando de remplazara"


### LA INGNORACION DE FORMATOS QUE NO QUEREMOS MAS UTILIZAR JAMAS

> touch .gitignore


### AGREGACION DE LOS FICHEROS PARA SER IGNORADOS ENTRO DE (.gitignore)

**/nombre del fichero


### RECONOCER LOS ULTIMOS MOVIMIETOS HECHOS EN EL DOCUMENTOS

>git diff


### PARA SABER LA UBICACION EXACTA DE DONDE NOS ENCONTRAMOS

> git checkout HEAD


### PARA REALIZAR UNA UBICACION DENTRO DE LOS ARCHIVOS

> git checkout id del FICHERO

### BORRAR LOS ARCHIVOS PARA LLEGAR A UN LUGAR DEL ARCHIVO

> git reset --hard id del fichero


### RECUPERACION DE LOS ELEMENTOS BORRADOS 
> git reflog

### GIT CONECION DE DIVESOS EQUIPOS DE MANERA REMOTA 

> git "Biscar comando"

### Creacion de una tabla en (.md)

[> Creacion de tablas mas rapido](https://www.tablesgenerator.com/markdown_tables)

|Syntem | Descripcion|
|---|------------|
|header | tible      |
|paragrahp| text     |


| Nombre | Apellido  | Correo |Codigo   |edad   |
|---|---|---|---|---|
|Oscar   |Romero   |oro0069074@gmail.com   |35074   | 20   |
|   |   |   |   |   |
|   |   |   |   |   |


``` python
print("Romerom reom re")
valor = input("Ingre un valor")
# Crecion de condicionales

if valor == "Oscar romero"
    print(f"Hola como estas {valor}")
elif valor == "Romero"
    print("Ese es tu apellido")
```
``` 
```


