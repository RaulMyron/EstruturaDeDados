N = int(input())

def converte(nota):
  if(nota == "SS"):
    return 10
  elif(nota == "MS"):
    return 8.9
  elif(nota=="MM"):
    return 6.9
  elif(nota=="MI"):
    return 4.9
  elif(nota=="II"):
    return 2.9
  else:
    return 0

lista = []
for i in range(N):
  nota, aluno = input().split(" ", 1)
  lista.append([converte(nota), aluno, nota])
  lista = sorted(lista, key = lambda x: (-x[0], x[1]))

for i in (lista):
  print(i[2], i[1])