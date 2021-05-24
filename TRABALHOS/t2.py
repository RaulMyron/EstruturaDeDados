n = int(input()) #qtd wookies
carga = list(map(int, input().split()))
s = []

lista_wookies = []

for i in range(n):
  lista_wookies.append([])

if(n == 0):
  print("Os Wookies foram para o lado sombrio da força!")
  print(*carga, sep=' ')
else:

  carga_2 = carga[0:n]

  size = carga[:]
  #print(size)
  size = len(size)

  for i in range(n):
    #print(i)
    #print(size)
    lista_wookies[i].append(carga.pop(0))
    if(i==size-1):
      break


  
  #print(lista_wookies)
  #print(carga)

  #print(carga)
  lista_remove = []

  if(len(carga)>0):
    #print("len: ", end='')
    #print(len(carga))
    for i in carga:
      #print(carga)
      #print("carga:", end='')
      #print(i)
      for wookie_esp in lista_wookies:
        if wookie_esp[-1] >= i:
          #print(i)
          wookie_esp.append(i)
          lista_remove.append(i)
          #carga.pop(carga.index(i))
          #print("brickou")
          break

  lista_wookies_ordenada = sorted(lista_wookies,key=lambda x: sum(x), reverse=True)

  for i in lista_remove:
    carga.remove(i)

  print(*lista_wookies_ordenada, sep=' ')

  if(len(carga)>0):
    print(*carga, sep=' ')
  else:
    print("A força está com os Wookies!")