__author__ = 'Javier'

"""
Para definir métodos con parámetros variable sutilizamos la notación
especial * y **. A continuación tienes varios ejemplos de uso.
"""

def lista_de_parametros(*args):
    print("lista_de_parametros", args)

def parametro_fijo_y_variables(uno, *los_demas):
    print("parametro_fijo_y_variables", uno, los_demas)

def parametro_tipo_lista(es_lista):
    print("parametro_tipo_lista", es_lista)

lista_de_parametros([1, 2, 3])
parametro_tipo_lista([1, 2, 3])
parametro_fijo_y_variables([1, 2, 3])
lista_de_parametros(1, 2, 3)
# parametro_tipo_lista(1, 2, 3) -- Error de ejecución
parametro_fijo_y_variables(1, 2, 3)

def diccionario_de_parametros(**args):
    print(diccionario_de_parametros, args)

#diccionario_de_parametros({'a':1}) -- Error de ejecución
#diccionario_de_parametros('a',1) -- Error de ejecución
# no hay ninguna a declarada, pero no da error.
diccionario_de_parametros(a=1)

def listas_y_diccionarios(*args, **dict_args):
    print("listas_y_diccionarios", args, dict_args)

listas_y_diccionarios(1, 2, 3)
listas_y_diccionarios([1, 2, 3])
listas_y_diccionarios({'a':1})
listas_y_diccionarios(a=1)
# listas_y_diccionarios(a=1, 2, b=3) -- Error
listas_y_diccionarios(1, a=2, b=3)





