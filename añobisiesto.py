año = ""
while len(año) != 4 or int(año) >= 2023:
    año = input("dime en que año naciste ")
    if len(año) != 4 or int(año) >= 2023:
        print("el numero no debe ser menor a 4 cifras, ni mayor a 2023, intente de nuevo")
        continue

respuesta = int(año)
numero = respuesta % 10

if respuesta % 4 == 0 and (respuesta % 100 != 0 or respuesta % 400 == 0):
    print("Vaya, naciste en un año bisiesto :D")
else: 
    print("usted no nacio en año bisiesto")

'''
Anotaciones:
    La función int() en Python se utiliza para convertir un valor en un número entero
        tambien sirve para redondear, separar, cambiar texto a numero, etc.
    La función len() en Python se utiliza para obtener la longitud o cantidad de elementos
        ejemplo:
            cadena = "Hola mundo"
            longitud_cadena = len(cadena)
            print(longitud_cadena)  # Salida: 10

            lista = [1, 2, 3, 4, 5]
            longitud_lista = len(lista)
            print(longitud_lista)  # Salida: 5

            tupla = (1, 2, 3, 4, 5)
            longitud_tupla = len(tupla)
            print(longitud_tupla)  # Salida: 5

            diccionario = {"a": 1, "b": 2, "c": 3}
            longitud_diccionario = len(diccionario)
            print(longitud_diccionario)  # Salida: 3
'''