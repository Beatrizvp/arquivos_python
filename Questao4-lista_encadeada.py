"""
Questao 4
Programe três estruturas de dados para imprimir listas de alimentos, clientes e funcionários.
- Lista Duplamente encadeada; ( incluir todos seus comportamentos)
- Lista Linear; (incluir os seus comportamentos)
- Lista Encadeada. (incluir seus comportamentos)
"""


##################################
## NO
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

##################################
## LISTA ENCADEADA
class Listaencadeada:
    # contrutor
    def __init__(self):
        self.head = None
        self._size = 0
    #######################

    def append(self, elemento):
        if self.head:
            # caso ja exista uma inserção add no next
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(elemento)
        else:
            # primeira insersão
            self.head = Node(elemento)

        self._size = self._size + 1

    def __len__(self):
        "Retorna tamanho da lista"
        return self._size

    def _getnode(self, item):
        pointer = self.head
        for i in range(item):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError(":p List index out of range")
        return pointer

    def __setitem__(self, item, newitem):
        # lista[2] = 10
        pointer = self._getnode(item)
        if pointer:
            pointer.data = item
        else:
            raise IndexError(":p List index out of range")

    def __getitem__(self, item):
        # b = lista[2]
        pointer = self._getnode(item)
        if pointer:
            return pointer.data
        else:
            raise IndexError(":p List index out of range")


    def index(self, item):
        """Retorna o indice do elemento da lista"""
        pointer = self.head
        i = 0
        while(pointer):
            if pointer.data == item:
                return i
            pointer = pointer.next
            i = i + 1
        raise ValueError("{} is not in list".format(item))


    def insert(self, index, item):
        node = Node(item)
        if index == 0:
            "insere no começo"
            node.next = self.head
            self.head = node
        else:
            "insere no fim"
            pointer = self._getnode(index-1)
            node = Node(item)
            node.next = pointer.next
            pointer.next = node

    def remove(self, item):
        if  self.head == None:
            raise ValueError("{} is not in list".format(item))
        elif self.head.data == item:
            self.head = self.head.next
            self._size = self._size - 1
            return True
        else:
            ante = self.head
            pointer = self.head.next
            while(pointer):
                if pointer.data == item:
                    ante.next = pointer.next
                    pointer.next = None
                ante = pointer
                pointer = pointer.next
            self._size = self._size - 1
            return True
        #error abaixo caso nao exista o item na lista
        ValueError("{} is not in list".format(item))


    def __repr__(self):
        r = ""
        pointer = self.head
        while(pointer):
            r = r +"["+ str(pointer.data) +"] -> "
            pointer = pointer.next
        return r

    def __str__(self):
        return self.__repr__()


lista = Listaencadeada()

# INSERE
lista.append("Arroz")
lista.append("Feijão")
lista.append("Macarrao")
lista.append("Bolacha")
print("Alimentos: ", lista, "\n")


# BUSCA
print("busca Bolacha: ", lista[3])

# REMOVE
lista.remove(2)
print("remove Bolacha: ",lista.remove("Bolacha"))

# INSERE ALIMENTOS EM ALGUMA POSICAO
lista.insert(2, "Refrigerante")
print("inseriu ['Refrigerante'] na posicao [2]")
print("\nAlimentos: ", lista)



