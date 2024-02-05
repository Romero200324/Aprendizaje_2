# El hola mundo 
print ("Hola mundo")

#Variables
numeracion = [1,2,3,4,5,6,7,8,9,10] 
print (numeracion)

# Funciones, Condiciones y Interaciones 

# Funcion 
def HelloWorldXY(x, y):

  # Condiciones 
  if (x < 10):
    print("Hello World, x was < 10")
  elif (x < 20):
    print("Hello World, x was >= 10 but < 20")
  else:
    print("Hello World, x was >= 20")
  return x + y

# Interacciones 
# Bucle     
for i in range(8, 25, 5):  # i=8, 13, 18, 23 (start, stop, step)
  print("--- Now running with i: {}".format(i))
  r = HelloWorldXY(i,i)
  print("Result from HelloWorld: {}".format(r))


#  Ciclo 

print("Iterate over the items. `range(2)` is like a list [0,1].")
for i in range(2):
  print(i)

print("Iterate over an actual list.")
for i in [0,1]:
  print(i)

print("While works")
i = 0
while i < 2:
  print(i)
  i += 1

# Datos boleanos 

print("Python supports standard key words like continue and break")
while True:
  print("Entered while")
  # Terminar el ciclo 
  break
