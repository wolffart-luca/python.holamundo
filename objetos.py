#resumen de clase "programacion apuntada a objetos en python"

'''
>>>>>>>>NOTA<<<<<<<<<
En python todo puede reescribirce, entonces se declara una regla popular que es "_". Es decir que si una funcion comienza con guion bajo no debe ser modificada "_ejemplo" Si fuese necesario modificarla se debe modificar desde dentro de la funcion 


class luz:
    _enciende = True

    def apaga(self):
    #En este ejemplo, "self" se utiliza para acceder al atributo "luz" 
        self._enciende = False
        #al colocar "self." hago referencia a una variable de mi clase, en este caso "_enciende"
    #esta es la manera corecta de modificar la funcion guionizada.

        
l = luz()
#hacemos que l tenga todo el contenido de luz
print(l._enciende)
#para llamar alguna funcion de mi objeto se utiliza ".", es decir "l.ejemplo"
l.apaga()
print(l._enciende)


#herencias: una clase hereda las propiedades y los metodos de una clase padre

class lampara:
    _prende = True

    def encendido(self):
        print("se prendio")
        self._prende = True

    def apagado(self):
        print("se apago")
        self._prende = False

    def roto(self):
        self._prende = "ze rompio"


class lamparita(lampara):
#aqui, al colocar (lampara). la clase "lamparita" hereda automaticamente todas las clases dentro de "lampara", la cual se convierte automaticamente en la clase padre.
    _ernchufado = True

    def desenchufado(self):
        self._ernchufado = False

lamp = lamparita()
lamp.encendido()



#constructor

class lampara():
    def __init__(self, estado):
    #el constructor se define con el parametro "__init__", mediante el cual podremos establecer nuevos parametros, sin necesidad de escribirlos aqui
    #tambien se puede utilizar "__del__", esto se conoce como DESTRUCTOR, pero no suele ser utilizado, ya que python incluye un recolector de basura para las instancias no utilizdas.
        print("la lampara esta", estado)

l = lampara("encendida")



#clases abstractas
#Las clases abstractas definen una serie de funciones que seran comunes para otras clases.

from abc import ABC, abstractmethod

class lampara(ABC):
    @abstractmethod
    #aqui definimos el metodo abstracto de la clase padre
    def encendido(self):
     pass

class lamparita(lampara):
    def encendido(self):
       estado = True
       print("la lampara encendio? ", estado)

class led (lampara):
   def encendido(self):
      estado = False
      print("el led esta encendido? ", estado)

#entonces aqui ambas clases pueden utilizar el contenido de "lampara" siendo que ambas son clases totalmente distintas y pueden tener distintos resultados. Asi ahorramos codigo

l = lamparita()
l.encendido()

l2 = led()
l2.encendido()

'''
#Lo anteriormente visto (herencias) se conoce como "relaciones HIS-A"

#Relaciones HAS-A



class motor:
    tipo = "Vtec"
    cilindros = 4
    litros = 2.0
    turbo = True

class carroceria:
    puertas = 2
    traccion = "Delantera"
    modelo = "Type R"


class honda_civic:
    mecanica = motor()
    elementos = carroceria()

h = honda_civic()
print("honda civic", h.mecanica.tipo, h.mecanica.litros, h.elementos.modelo, "traccion", h.elementos.traccion)
#de este modo todo lo detallado en las anteriores clases, se anidan en clase "honda_civic" (HAS-A significa "contiene")