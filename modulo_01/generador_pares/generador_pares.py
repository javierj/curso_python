
# Clase Iterador
class ClaseNumerosPares:

    def __init__(self, max_value = 20):
        self.max_value = max_value

    def __iter__(self):
        self.num = 0
        return self

    # Método a usar en Python 3
    def __next__(self):
        self.num += 2
        if self.num >= self.max_value:
            raise StopIteration
        return self.num

    # Método a usar en Python 2
    def next(self):
        return self.__next__()


# Clase generadora
def gen_numeros_pares(max_value = 20):
    numero_interno = 2
    while numero_interno < max_value:
        yield numero_interno
        numero_interno += 2

# Main
if __name__ == '__main__':
    print("Con el clase iteradora")
    it = ClaseNumerosPares(10)
    for i in it:
        print(i)

    print("Con la metodo generador")
    it = gen_numeros_pares(10)
    for i in it:
        print(i)

    print("Con el modulo itertoools")
    import itertools
    for i in itertools.islice(itertools.count(2, 2), 0, 4):
        print(i)


