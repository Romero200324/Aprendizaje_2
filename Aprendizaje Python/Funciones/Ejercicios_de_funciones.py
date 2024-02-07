# EN EL VIDEO DE CUERO DE PYTHON VOY EN (4:38 mimutos)



# Ejercicios de (Funciones integradas).

#1 Escribir una función que aplique un descuento a un precio y otra que aplique el IVA a un precio.

# Numeros precio : $525 Descuento %15 Resultado = $446.25  Iva 0.5  Resultado de ambos = 

producto = int(input(" Precio de tu producot es:$"))

def decuento_de_precios (producto):
    # Ejemplo : 30%, divides 30 entre 100= 0,3. 2.X precio del producto
    descuesto = int(input("Hola cuales seran los descuentos de esta semana:%"))

    aplicacion_de_descuneto = descuesto / 100 * producto 
    resultado = producto - aplicacion_de_descuneto
    return(round(resultado))

valor_final_de_descuentos = decuento_de_precios(producto)


def producto_iva (producto):

    # Ejemplo :  IVA = 100 x 0.16 = 16 pesos
    # precio * IVA / 100
    iva = int(input("El iva de hoy: "))
    aplicacion_con_iva =  producto * iva / 100 
     
    return(round(aplicacion_con_iva))

valor_final_con_iva = producto_iva(producto)

    
# Escribir una tercera función que reciba un diccionario con los precios y porcentajes de una cesta de la compra,
    # y una de las funciones anteriores, y utilice la función pasada para aplicar los descuentos o el IVA a los productos
# de la cesta y devolver el precio final de la cesta.


def creacion_de_diccionario (valor_final_de_descuentos,valor_final_con_iva ):
    almacen = { "Articulo con descuento" : valor_final_de_descuentos, 
                 "Articulo con impuesto de IVA" : valor_final_con_iva
              }
    return (almacen)
almacen_total = creacion_de_diccionario ( valor_final_de_descuentos,valor_final_con_iva )


valor_de_promociones_con_iva = round((valor_final_de_descuentos + valor_final_con_iva))
valor_de_promocion_sin_iva = round((valor_final_de_descuentos ))

print("""
        SUGERENCIAS ANTES DE HACER TUS COMPRAS: 
""")

if valor_de_promociones_con_iva >= producto:
    operacion_interna = producto - valor_de_promociones_con_iva  
    print(f"Enserio quieres pagar más de lo que vale el articulo, Ya que lo que vas gastar de más sera: ${operacion_interna} ")

elif valor_de_promociones_con_iva <= producto:
    operacion_interna_2 = producto - valor_de_promociones_con_iva
    print(f"Pues aún es una buena compra,Ya que vas ahorar sera : ${operacion_interna_2}")

else:
    print("Lo siento pero algo esta mal-")


print (f"""Tus productos con el (Descuento y IVA seran): {almacen_total}

        Valor de tú articulo con descuento más sumando el IVA seran:
        El Total : ${valor_de_promociones_con_iva}

        El valor de tú articulo con decuento sin la suma IVA sera: ${valor_de_promocion_sin_iva}
       """)


# (*valor) Colocar muchos parametreos en un solo elemento

#1 sumacion de valores..

# Suspedido por el momento
#def sumacion (*enumeracion):
 #   return sum(enumeracion)

#valor = sumacion(10,20,10,10,50)
#print(f"El resultado del suma es :{valor}")


#2

#3