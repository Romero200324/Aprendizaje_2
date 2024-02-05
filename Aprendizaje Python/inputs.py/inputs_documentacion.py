# Seccion de inputs

#inputs 
peticion_de_dato = input("Me puedes dar tu nombre completo: ")

if peticion_de_dato == "Oscar Romero Romero":
    print(f"Bienvenido {peticion_de_dato}")
else:
    print("Lo siento pero su nombre no es correto..")

# numeros enteros (int)

peticion_de_numero = input("Me pudes dar un numero para la suma de dos valores: ")
suma = int(peticion_de_numero) + 333
print(f"La suma de dos valores es: {suma}")

# numeros con punto decimal (float)

peticion_de_numero_decimal = input("Me puede proporcionar un numero decimal: ")
operaciones = float(peticion_de_numero_decimal) * suma
print(f"La operacion nos da como resultado el siguiente valor: {operaciones}")

