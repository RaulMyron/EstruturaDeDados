qtd = int(input())

lista = [1,1]

def fat(valor):
  global lista
  if(len(lista)>valor):
    return lista[0:valor+1]
  else:
    for i in range((len(lista)),valor+1):
      #print("i:", i)
      #print("newvalue:", i*lista[i-1])
      if(i>6):
        lista.append(i*lista[i-1]%2357)
      else:
        lista.append(i*lista[i-1])
  return lista[0:valor+1]

for i in range(qtd):
  valor = int(input())
  print(*fat(valor), sep = " ")
