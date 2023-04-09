Bucle while: Este bucle se repite mientras se cumpla una determinada condición.

i = 1
while i <= 5:
    print(i)
    i += 1
    
Bucle for: Este bucle se utiliza para iterar sobre una secuencia de elementos.

lista = ["a", "b", "c"]
for elemento in lista:
    print(elemento)
    
    
Bucle for con range(): Este bucle se utiliza para iterar sobre una secuencia de números.

for i in range(1, 6):
    print(i)
 
 
Bucle for anidado: Este bucle se utiliza para iterar sobre múltiples secuencias.

lista_1 = ["a", "b", "c"]
lista_2 = [1, 2, 3]
for elemento_1 in lista_1:
    for elemento_2 in lista_2:
        print(elemento_1, elemento_2)
 
 
Bucle while con break: Este bucle se utiliza para salir del bucle cuando se cumpla una determinada condición.

i = 1
while True:
    print(i)
    i += 1
    if i > 5:
        break
        
        
Bucle for con continue: Este bucle se utiliza para saltar a la siguiente iteración cuando se cumpla una determinada condición.

lista = ["a", "b", "c", "d", "e"]
for elemento in lista:
    if elemento == "c":
        continue
    print(elemento)
