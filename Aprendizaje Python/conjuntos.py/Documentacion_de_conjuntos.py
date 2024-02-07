# ("""Documentacion de conjuntos""")

# (Set) Creacion de conjuntos
conjuntos = set(["Dato 1", "Dato 2"])
print(f"Creación de un conjunto: {conjuntos}")

# (frozeset) Congeladaos y añadir a un conjuto no mutaple
congelar_conjuntos = frozenset(["dato 1", "dato 2"])
congelar_conjuntos_2 = {congelar_conjuntos, "dato3 "}

print(congelar_conjuntos_2)

# (issubset) Para saber si es el subconjunto de otro.

enumeracion_de_conjunto_1 = {2,3,4,5}
enumeracion_de_conjunto_2 = {3,3,2,5}
        # Otra menera de escribir el codigo
resultado = enumeracion_de_conjunto_2 <= enumeracion_de_conjunto_2
resultado = enumeracion_de_conjunto_2.issubset(enumeracion_de_conjunto_1)
print(resultado)


# (issuperset) Para saber si es el superconjunto
resultado = enumeracion_de_conjunto_2.issuperset(enumeracion_de_conjunto_1)
print(resultado)


# (isdisjoint) Para saber si hay un numero en común (False) : SI hay uno.
resultado = enumeracion_de_conjunto_2.isdisjoint(enumeracion_de_conjunto_1)
print(resultado)