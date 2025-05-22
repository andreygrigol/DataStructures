class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class LinkedList:
    def __init__(self):
        self.head = None

    def adicionar_ao_final(self, valor):
        novo_no = Node(valor)
        if not self.head:
            self.head = novo_no
            return
        atual = self.head
        while atual.proximo:
            atual = atual.proximo
        atual.proximo = novo_no

    def imprimir(self):
        atual = self.head
        while atual:
            print(atual.valor, end=" -> ")
            atual = atual.proximo
        print("None")


lista = LinkedList()
lista.adicionar_ao_final(10)
lista.adicionar_ao_final(20)
lista.adicionar_ao_final(30)
lista.adicionar_ao_final(25)
lista.adicionar_ao_final(15)

lista.imprimir()
