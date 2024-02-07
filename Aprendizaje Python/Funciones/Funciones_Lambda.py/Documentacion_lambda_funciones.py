# Apertado para funciones lambda

# (lambda) Creacion de una funcion sensilla con un parmatro

listado = [1,2,3,3,4,5,6,6,7]

multiplicaion = lambda n : n*2

print(multiplicaion(8))



numero_pares = filter(lambda listado:listado%2 == 0,listado)
print(list(numero_pares))
