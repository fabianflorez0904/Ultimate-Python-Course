class Lista(list):
    def preppend(self, item):
        self.insert(0, item)


lista = Lista([1, 2, 3])
lista.append(4)
lista.preppend(0)
print(lista)
