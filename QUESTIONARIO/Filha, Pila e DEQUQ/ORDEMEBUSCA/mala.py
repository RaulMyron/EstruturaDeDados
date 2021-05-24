from collections import Counter

N = int(input())

pessoas = []
tamanho = []

for i in range(N):
  nome = input()
  pessoas.append(nome)

pessoas.sort()

for i in pessoas:
  tamanho.append(len(i))

#print(Counter(tamanho))
x = dict(Counter(tamanho))
#print(x)

valor_max_nome = -1
for key in reversed(sorted(x)):
  #print("%s: %s" % (key, x[key]))
  if(x[key]==1):
    valor_max_nome = key
    break
  
if(valor_max_nome==-1):
  print("Que mala suerte!")
else:
  indexA = tamanho.index(valor_max_nome)
  print(pessoas[indexA])




