from collections import deque
#ou import collections
#lista = collections.deque()
lista = deque()

#I v insere o valor v no início da lista.
#F v insere o valor v no final da lista.
#P remove do final e imprime valor removido.
#D remove do início e imprime valor removido.
#V n Remove o valor n e retorna a quantidade de itens removidos.
#E v Remove elemento da posição v e retorna o valor removido.
#T v n Troca o valor da primeira ocorrencia de v pelo valor de n.
#C v Retorna ocorrencias de valor v.
#X Indica o final das operações e que a lista resultante deve ser impressa.

while True:
  inserido = input().split()
  inserido.append(-1)
  operacao = inserido[0]

  if inserido[1] != -1:
    valor = int(inserido[1])

  if operacao == 'X':
    print()
    while lista:
      print(lista.popleft())
    break

  if(operacao == 'I'):
    lista.appendleft(valor)
  elif(operacao == 'F'):
    lista.append(valor)
  elif(operacao == 'P'):
    print(lista.pop())
  elif(operacao == 'D'):
    print(lista.popleft()) #certo
  elif(operacao == 'V'):
    contador = 0
    try:
      x = lista.index(valor)
      for i in lista:
        if i == valor:
          contador +=1
      while contador!=0:
        lista.remove(valor)
        contador-=1
    except ValueError:
      None
    print(contador)
  elif(operacao == 'E'):
    lista.rotate(-valor+1)
    print(lista.popleft())
    lista.rotate(valor-1)
  elif(operacao == 'T'):
    try:
      posicao = lista.index(valor)
      lista.rotate(-posicao)
      lista.popleft()
      lista.appendleft(int(inserido[2]))
      lista.rotate(posicao)
    except ValueError:
      None
  elif(operacao == 'C'):
    contador = 0
    for i in lista:
      if i == valor:
        contador +=1
    print(contador)