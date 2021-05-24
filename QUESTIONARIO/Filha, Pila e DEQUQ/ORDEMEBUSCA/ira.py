N = int(input())

notas = []

for i in range(N):
  notas.append(float(input()))

notas.sort(reverse=True)

for i in notas:
  print(f'{i:.2f}')




