"""
QUESTAO 3
Desenvolva uma árvore binária de Busca em Python.
E em seguida nesta mesma árvore binária
desenvolva a busca pela chave de número 5.
"""


import random
# NO
class Node:
    def __init__(self, dado):
        self.dado = dado
        self.dir = None
        self.esq = None
    def __str__(self):
        return str(self.dado)

#####################################
#ARVORE BINARIA
class ArvoreB:
    def __init__(self, dado=None, node=None):
        if node:
            self.root = node
        elif dado:
            node = Node(dado)
            self.root = node
        else:
            self.root = None

    '''percurso simetrico'''
    def percuso_simetrico(self, node=None):
        if node is None:
            node = self.root

        if node.esq:
            self.percuso_simetrico(node.esq)
        print(node, end=' ')

        if node.dir:
            self.percuso_simetrico(node.dir)

#####################################
#ARVORE BINARIA DE BUSCA
class BinarySearchTree(ArvoreB):
    
    """Inserir na arvore"""
    def insere(self, valor):
        pai = None
        aux = self.root
        while(aux):
            pai = aux
            if valor < aux.dado:
                aux = aux.esq
            else:
                aux = aux.dir
        if pai is None:
            self.root = Node(valor)
        elif valor < pai.dado:
            pai.esq = Node(valor)
        else:
            pai.dir = Node(valor)

    """Buscar na arvore"""
    def busca(self, valor):
        return self._buscar(valor, self.root)

    def _buscar(self, valor, node):
        if node is None:
            return node
        if node.dado == valor:
            return BinarySearchTree(node)
        if valor < node.dado:
            return self._buscar(valor, node.esq)
        return self._buscar(valor, node.dir)


########################################
#### TESTE Busca
#random.seed(77)
valores = random.sample(range(1, 40), 10)

bst = BinarySearchTree()
for i in valores:
    bst.insere(i)

bst.percuso_simetrico()

chave = [5]
for item in chave:
    r = bst.busca(item)
    print("")
    if r is None:
        print("(",item, ") nao encontrou")
    else:
        print("(",r.root.dado, ") encontrou")
