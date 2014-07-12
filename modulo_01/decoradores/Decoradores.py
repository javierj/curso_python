
# Decoradores de metodos en Python

class Demo(object):
    # atributo estatico
    soy_estatico = "El mismo para todos los objetos"

	# constructor
    def __init__(self):
        self.nombre = "Clase demo"


    # Representa el objeto como una cadena
    def __str__(self):
        return "Mi nombre: " + self.nombre


    # Metodo estatico
    @staticmethod
    def no_necesito_self():
        return 3


    # Metodo get
    @property
    def el_nombre(self):
        return self.nombre


    # Metodo set
    @el_nombre.setter
    def el_nombre(self, value):
        self.nombre = value
		


if __name__ == "__main__":
    demo = Demo()

    print("Atributo estatico: ", Demo.soy_estatico)
    print("Metodo estatico: ", Demo.no_necesito_self())
    print("Metodo str:", demo)
    demo.el_nombre = "Otro nombre"
    print("Nuevo nombre: ", demo.el_nombre)