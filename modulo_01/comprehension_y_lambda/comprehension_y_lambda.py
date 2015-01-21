__author__ = 'Javier'

# Como crear una lista de 10 números pares de la manera más fea posible en Python
l1 = list()
for i in range(10):
    l1.append(i*2)

# Creando la misma lista con comprehension cmo auténticos Python masters
l2 = [x*2 for x in range(10)]

# Una alternativa más rebuscada que sirve de ejemplo para ver cómo añadir condiciones
l3 = [x for x in range(20) if x % 2 == 0]


# Las tres listas tienen los mismos elementos
print(l1)
print(l2)
print(l3)

#------------------------------------------------------------

# Un comando de Python es filter(f, i), que devuelve una lista (v2.x) o un iterador (v3.x)
# con los elementos del iterable i que cumplen la función f.
# Un ejemplo sería

l = [1, 2, 3, 4, 5, 6]

def es_par(num):
    return num%2 == 0

it1 = filter(es_par, l)
for i in it1:
    print(i)

# Podemos ahorranos la función es_par utilizando lambdas

it2 = filter(lambda x: x%2 == 0, l)
for i in it2:
    print(i)

