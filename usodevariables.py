'''
#variable simple
def prueba(nombre):
    print('hola', nombre, 'esto es una prueba en python')

prueba('nate gentile')

#variable utilizando return
def prueba(nombre, situacion):
    resultado = nombre + situacion
    return resultado

final=prueba('nate gentile ', 'esto es una prueba en python')

print(final)


#modificar variables

def suma(*alls):

    resultado = 0
    
    for all in alls:
        resultado += all

    print(resultado)

suma (1, 2, 3, 4, 3, 3, 4, 5)


#Parametros diccionario
def suma(**kwargs):
    if 'coche' not in kwargs:
        return #aqui "return" cierra el 
                #proceso si "coche" no esta en kwargs
    if kwargs ['coche'] == 'bonito':
        print("tu coche es bonito")
suma(coche='bonito')


def suma(**kwargs):
    for key, value in kwargs.items():
    #key y value da parametros a los items
    #.items los ordena uno debajo del otro
        print(key, "=", value)

#suma(a= "id", b="genero", c="estado civil", d="contrato")
suma(id=2, genero="masculino", EC="soltero", contrato="permanente")
'''
#****NOTA****
#Nunca se usa "print" para devolver resultados en variables.
#En su lugar se utiliza "return"
#Ejemplo 

'''
def suma(a, b):
    return a + b

resultado = suma(4, 3)
print(resultado)
'''

#Al utilizar "return" damos el parametro que deseamos que realice.
#En este caso "a+b" luego debajo damos la variable numerica
#Esto se puede hacer con distintos parametros. Ejemplo:
'''
def suma(a, b):
    return a + b

resultado = suma(4, 3)
resultado2= suma(5, 4)

print(resultado, resultado2)

def operaciones(a, b):
    return a*b, a+b, a-b

#primer = operaciones(2, 4)
multi, suma, resta = operaciones(2, 4)
#aqui asignamos nombre a cada variable del return
print(multi, resta)

'''
#variables lambda: Las variables lambda son funciones llamadas "anonimas". Ya que se asignan a una funcion sin utilizar "def = " sino que se usa el nombre de la variable asi "variable = lambda" Luego se asigna el valor "variable = lambda valor" Por ultimo la funcion "variable = lambda valor: print (funcion)" esto nos daria de resultado "valor"

variable = lambda saludo, persona: print(saludo, persona)

variable("hola", "juan")
