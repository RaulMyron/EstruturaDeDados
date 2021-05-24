from datetime import timedelta

N = int(input())

def converte(x):
  secs, millis = map(int, x.split('.'))
  return timedelta(seconds=secs, milliseconds=millis)

tempo = []

for i in range(N):
  nome = input()
  tempos = input().split()
  #print(tempos)
  res = sum(map(converte, tempos), timedelta())
  timeo, MM = str(res).split(".")
  H, M, S = timeo.split(":")
  if(M != 00):
    time_real = str(int(M)) + ":" + S + "." + MM[0:3]
  else:
    str(int(S)) + "." + MM[0:3]
  #print(nome)
  #print(time_real)
  tempo.append([nome, time_real])

#print(tempo)

tempo = sorted(tempo, key=lambda x: x[1])

for i in range(len(tempo)):
  print(f'{i+1}. {tempo[i][0]} ({tempo[i][1]})')