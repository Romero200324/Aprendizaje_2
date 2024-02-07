# Documentacion de los metodos de Setters 

# (get_valor) # hacer de los valores de la mejor forma
class acceder_a_objecto:
    def __init__(self, nombre,edad):
        self._nombre = nombre 
        self._edad = edad

    def get_valor(self):
        return self._edad
    
    # Inscrustacion de un nuevo valor de trabajo. 

    def set_nombre(self, new_nombre):
         self._edad = new_nombre

# Declaracion de los datos a escojer...

oscar = acceder_a_objecto("Oscar", 20)

obtecion_de_datos = oscar.get_valor()
print(obtecion_de_datos)


# Incrustacion de una varible publica...

nuevo_dato = oscar.set_nombre("Romero Romero")

obtecion_de_datos = oscar.get_valor()
print(f"Los cambion fueron realizados correctamente: {obtecion_de_datos}")


