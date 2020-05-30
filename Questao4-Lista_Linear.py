"""
Questao 4
Programe três estruturas de dados para imprimir listas de alimentos, clientes e funcionários.
- Lista Duplamente encadeada; ( incluir todos seus comportamentos)
* Lista Linear; (incluir os seus comportamentos)
- Lista Encadeada. (incluir seus comportamentos)


A lista linear que usei é uma pilha
"""


##################################
## NO
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class ListaLinear:
    #contrutor
    def __init__(self):
        self.top = None
        self._size = 0
    #######################

    #insere
    def push(self, elem):
        node = Node(elem)
        node.next = self.top
        self.top = node
        self._size = self._size + 1
        return "Insere: "+node.data

    #remove (do top)
    def pop(self):
        if self._size > 0:#ser a lista tiver vazia nao executa
            node = self.top
            self.top = self.top.next
            self._size = self._size - 1
            return "Removeu: "+node.data
        else:
            raise IndexError("A lista estar vazia :(")

    #observar topo
    def peek(self):
        if self._size > 0:#ser a lista tiver vazia nao executa
            return self.top.data
        else:
            raise IndexError("A lista estar vazia :(")

    #retorna tamnaho
    def __len__(self):
        return self._size
    def len(self):
        return self.__len__()

    #exibir
    def __repr__(self):
        r = ""
        pointer = self.top
        while(pointer):
            r = r +"["+ str(pointer.data) +"] \n"
            pointer = pointer.next
        return r

    #exibir como string
    def __str__(self):
        return self.__repr__()


############################
## TESTE
lista = ListaLinear()

#insere
lista.push("Auxiliar")
lista.push("Operador")
lista.push("Supervisor")
lista.push("Lider")
print("\n##################################")
print("Funcionarios: ", lista.len())
print(lista)

# REMOVE
print(lista.pop())

# Insere
print(lista.push("Diretor"))
print(lista.push("Almoxarife"))

print("\n##################################")
print("Funcionarios: ", lista.len())
print(lista)


