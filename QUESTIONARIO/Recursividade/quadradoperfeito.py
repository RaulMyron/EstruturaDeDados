def quadrado_perfeito(valor):
  if(valor == 0):
    return print(f'0 ** 2 == 0')

  def soma(lista, lista2):
    if(len(lista)==1):
      print(lista2[0])
      print("---------------")
      return print(f'{valor} ** 2 == {lista[0]}')

    #print(lista2)
    print(f'{lista2[0]} + soma({lista[1:]})')

    lista[1]+=lista[0]
    lista.pop(0)

    soma(lista, lista2[1:]) 
  
  lista = []
  for i in range(valor):
    lista.append(2*(i+1)-1)
  #print(lista)
  soma(lista, lista.copy())

quadrado_perfeito(int(input()))