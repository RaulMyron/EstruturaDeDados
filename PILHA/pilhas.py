#PILHAS = STACK

from typing import List
from copy import deepcopy

stack: List[str] = []
stack.append('A')
stack.append('B')
stack.append('C')

#deve-se remover do topo (Ou em lista = ultimo elemento)
'''item_do_topo = stack.pop()
item_do_topo = stack.pop()
item_do_topo = stack.pop()'''

#REMOVE O ITEM DO "TOPO DA pilha"
'''print(stack, item_do_topo)'''

#PARA FOR
'''for item in stack[::-1]:
  print(item)'''

#PARA WHILE
'''
while stack:
  item = stack.pop()
  print(item)'''

#FAZENDO COPIAS DAS LISTAS

stack_copy = stack.copy()
#nativa shallow copy (itens imutaveis) exception: list MANIPULA O ORIGINAL -- parece reverse e reversed

stack_copy_DEEP = deepcopy(stack)
#IMPORTADA, CÓPIA literal

#NÃO FAÇA saporra é uma fila? não! é uma pilha
'''first_item = stack.pop(0)'''
#TENTE USAR EOF PRA N DAR INDEXERROR

try:
  top_item = stack.pop()
except IndexError:
  print("vazia")
