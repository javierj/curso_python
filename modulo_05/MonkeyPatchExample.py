__author__ = 'Javier'


class DiHola(object):
   def saludo(self, nombre):
        print( "Hola " + nombre )

class DiAdios(object):
   def saludo(self, nombre):
        print ("Adios " + nombre)


if __name__ == "__main__":
    hola = DiHola()
    adios = DiAdios()

    tmp = hola.saludo
    hola.saludo = adios.saludo

    hola.saludo("curso")
    adios.saludo("curso")

    hola.saludo = tmp

    hola.saludo("curso")
    adios.saludo("curso")

