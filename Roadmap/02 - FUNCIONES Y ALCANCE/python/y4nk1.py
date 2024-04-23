# sin parametros ni retorno
def saludo():
    print("hola como estas")

saludo()

# con 2 parametros 
def pase_de_lista(nombre,apellido):
     return nombre,apellido
respuesta=input("ingrese su respuesta ")

if respuesta == "presente":
     print("que bueno")

elif respuesta=="ausente":

     print("otra vez")

else:
     print("responda bien")
     

    #  funcion dentro de otra funcion
    
def funcion_externa():
    print("hola soy la funcion externa")
     
    def funcion_interna():
     print("hola soy la funcion interna")

    funcion_interna()  

funcion_externa()

# funciones ya creadas
cantida_de_objeto={"hola","adios","bienvenido"}

cuantos_hay=len(cantida_de_objeto)
print(cuantos_hay)

# prueba de concepto de variable local y global

# Variable global
x = 10

def mi_funcion():
    # Se intenta modificar la variable global dentro de la función
    # Pero Python creará una nueva variable local en su lugar
    x = 20  # Esta es una variable local, no afecta a la global 'x'
    print("Dentro de la función:", x)

# Llamamos a la función
mi_funcion()

# La variable global 'x' permanece sin cambios
print("Fuera de la función:", x)
