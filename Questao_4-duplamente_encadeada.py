"""
Questao 4
Programe três estruturas de dados para imprimir listas de alimentos, clientes e funcionários.
* Lista Duplamente encadeada; ( incluir todos seus comportamentos)
- Lista Linear; (incluir os seus comportamentos)
- Lista Encadeada. (incluir seus comportamentos)
"""
class Node:
    def __init__(self, dado):
        self.value = dado
        self.next = None
        self.prev = None

class DuplamenteEncadeada:
    def __init__(self, dado):
        self.inicio = Node(dado)
        self.fim = self.inicio

    def append(self, dado):
        pointer = self.inicio
        while pointer.next != None:
            pointer = pointer.next

        novoNo = Node(dado)
        pointer.next = novoNo
        novoNo.prev = pointer
        self.fim = novoNo

    def insertNode(self, dado, novoDado):
        if self.fim.value == dado:
            self.append(novoDado)
        elif self.inicio.value == dado:
            novoNode = Node(novoDado)
            novoNode.next = self.inicio.next
            novoNode.prev = self.inicio
            novoNode.next.prev = novoDado
            self.inicio.next = novoNode
        else:
            pointer = self.inicio.next
            while pointer.value != dado:
                pointer = pointer.next
            novoNode = Node(novoDado)
            novoNode.next = pointer.next
            novoNode.next.prev = novoNode
            novoNode.prev = pointer
            pointer.next = novoNode

    def remove(self, dado):
        if self.inicio.value == dado:
            self.inicio = self.inicio.next
            self.inicio.prev = None
        elif self.fim.value == dado:
            self.fim = self.fim.prev
            self.fim.next = None
        else:
            pointer = self.inicio.next
            while pointer.value != dado:
                pointer = pointer.next
            pointer.prev.next = pointer.next
            pointer.next.prev = pointer.prev

    def exibirLista(self):
        pointer = self.inicio
        while pointer:
            print(pointer.value)
            pointer = pointer.next



clientes = DuplamenteEncadeada("Maria")
clientes.append("Jose")
clientes.append("Marcos")
clientes.append("Ana")

print("#### Clientes ####")
clientes.exibirLista()
print("")

clientes.remove("Jose")
print("# removeu: Jose")

clientes.append("Joao")
print("# inseriu: Joao\n")

print("#### Clientes ####")
clientes.exibirLista()
print("")

