def get_tres(lista, posicao, janela):
  try:
    lista = lista[posicao:posicao+janela]
    return lista
  except IndexError:
    return None

N = int(input())
valores = list(map(int, input().split()))
janela = int(input())

de0ateN = range(0,N)

maiores = []
'''
if(janela == 1):
  for i in range(len(valores)-1):
    print(valores[i], end='  ')
  print(valores[-1], end='')
else:'''
for i in de0ateN:
  ListaN = get_tres(valores, i, janela)
  if(len(ListaN) == janela):
    #print(ListaN)
    #print(len(ListaN) == N)
    #print(max(ListaN))
    #print("TRUE")
    maiores.append(max(ListaN))
#print(maiores)
for i in range(len(maiores)-1):
  print(maiores[i], end='  ')
print(maiores[-1], end='')