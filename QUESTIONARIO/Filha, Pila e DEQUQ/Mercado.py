lista = []
while True:
  entrada = input().split()
  if(entrada[0] == 'fim'):
    break

  if(entrada[0] == '-'):
    nIndex = lista.index(entrada[1])
    lista.pop(nIndex+1)
    lista.pop(nIndex)
  else:
    lista.append(entrada[0])
    lista.append(entrada[1])

#print(len(lista))

preco = 0

#print(lista)
for i in reversed(range(0, len(lista), 2)):
  #print(i)
  preco += float(lista[i+1])
  print(f'{lista[i]}: R$ {float(lista[i+1]):.2f}')

print('----------------------')
print(f'{int(len(lista)/2)} item(ns): R$ {preco:.2f}')