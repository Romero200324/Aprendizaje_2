# Documentación de esepciones

def suma_de_numeros ():
    # Creación de Bucle.. 
    while True:        
            numero_1 = input("Ingrese un numero: ")
            numero_2 = input("Ingrese un segudo valor: ")
        
        # (try:) Primera parte de una (Excepciones)
            try:  #(break) Cumple las condiones Termina el programa...  
                operacion = int(numero_1) + int(numero_2)
                break

            except:
                print("Intentelo otra vez...")
    return operacion

print(suma_de_numeros())