#operadores aritmeticos
#de suma
print (f"suma 2+3 es igual a {2+3}")
#de resta
print(f"resta 5-3 es igual a {5-3}")
#multiplicacion
print(f"multiplicacion 5*5 es igual a {5*5}")
# division
print(f"division 50/2 es igual a {50/2}")
# modulo
print(f"modulo 10%3 es igual a {10%3}")

 # operadores relacionados
  #menor que 
print(f"10 es menor que 15 {10<15}")
# mayor que 
print(f"15 es mayor que 10 ¨{25>10}")
# igual
print(f"10 es igual que 10 {10==10}")
# Devuelve True si el operador de la izquierda es mayor o igual que el operador de la derecha
print(f"10 es mayor o igual que 5 {10>=5}")
# Devuelve True si el operador de la derecha es mayor o igual que el operador de la izquierda
print(f"5 es menor o igual que 10 {5<=10}")
# Devuelve True si ambos operandos no son iguales
print(f"5 no es igual a 6 {5!=6}")

# operadores logicos
# ambas condiciones se deben cumplir 
print(f"10-7==3 y 15-5==10 {10-7==3 and 15-5==10}")
# una de las 2 condiciones se deben cumplir
print(f"15+10==25 o 10-7==6 {15+10==25 or 10-7==6}")


# la condicion no se debe cumplir
print(f"15-5 no es igual a 25 { not 15-5==25}")

# operadores de asignacion

# asignacion


prueba = 5
print(prueba)
# suma
prueba += 5
print(prueba)

# resta y asiganacion
prueba-= 5
print(prueba)
# multiplicacion y asignacion
prueba *= 5
print(prueba)
# division y asignacion
prueba /=5
print(prueba)
# modulo y asignacion
prueba %= 5
print(prueba)
# etc

# operadores de identidad

# operador IS verifica que ambas variables hagan referencia a el mismo objeto
a=5
b=5
print(a is b)

# operador IS NOT este devuelve true cuando ambas variables no hacen referencia a el mismo objeto
c=5
e=6
print(c is not e)

# operadores de pertenencia

# el operador IN verifica si el valor se encuentra presente en un la secuencia y devuelve true si el valor se encuentra
numero= {1,2,3,4,5,6,7,8,9}
print(8 in numero)

# el operador NOT IN verifica si un valor no se encuentra en la secuencia y devuelve true si el valor no se encuentra
numero2 = {1,2,3,4,5,6,7,8,9}
print(15 not in numero2 )
