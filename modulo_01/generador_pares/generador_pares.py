# Python 3

class NumeroPar:

    def __init__(self, max_value = 20):
        self.max_value = max_value

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        self.num += 2
        if self.num >= self.max_value:
            raise StopIteration
        return self.num


# Main
if __name__ == '__main__':
    it = NumeroPar()
    for i in NumeroPar(10):
        print(i)

    # Alternativa
    import itertools
    for i in itertools.islice(itertools.count(2, 2), 0, 4):
        print(i)

