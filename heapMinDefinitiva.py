import math

class HeapMin:

    def __init__(self):
        self.nos = 0
        self.heap = []

    def adiciona_no(self, u: tuple):
        self.heap.append(u)
        self.nos += 1
        f = self.nos
        while True:
            if f == 1:
                break
            p = f // 2
            if self.heap[p-1][0] <= self.heap[f-1][0]: # <= HeapMin
                break
            else:
                self.heap[p-1], self.heap[f-1] = self.heap[f-1], self.heap[p-1]
                f = p

    def mostra_heap(self):
        print(self.heap)

    def remove_no(self):
        no_removido = self.heap[0]
        self.heap[0] = self.heap[self.nos - 1]
        self.heap.pop()
        self.nos -= 1
        p = 1
        while True:
            f = 2 * p
            if f > self.nos:
                break
            if f+1 <= self.nos:
                if self.heap[f][0] < self.heap[f-1][0]:
                    f += 1
            if self.heap[p-1][0] <= self.heap[f-1][0]: 
                break
            else:
                self.heap[f-1], self.heap[p-1] = self.heap[p-1], self.heap[f-1]
                p = f
        return no_removido

    def tamanho(self):
        return self.nos

    def menor_elemento(self):
        if self.nos != 0:
            return self.heap[0]
        return 'A árvore está vazia'

    def filho_esqueda(self, i):
        if self.nos >= 2*i:
            return self.heap[2*i - 1]
        return 'Esse nó não tem filho!'

    def filho_direita(self, i):
        if self.nos >= 2*i+1:
            return self.heap[2*i]
        return 'Esse nó não tem filho à direita!'

    def pai(self, i):
        return self.heap[i // 2]
    
""" h = HeapMin()

h.adiciona_no((17, 'e1', ['sa']))
h.adiciona_no((25, 'e2', ['adsds']))

h.adiciona_no((7, 'e3', ['dsdsa']))

h.adiciona_no((3, 'e4', ['fdfd']))

h.adiciona_no((36, 'e5', ['hjkj']))



h.mostra_heap()

h.remove_no()
h.mostra_heap()
print(h.tamanho()) """