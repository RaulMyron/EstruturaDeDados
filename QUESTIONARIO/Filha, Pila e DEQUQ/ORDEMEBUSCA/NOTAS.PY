N = int(input())

notas = []

for i in range(N):
  notas.append(float(input()))

notas.sort()

print(f'{notas[0]:.2f}')

mediana = len(notas)//2

print(f'{notas[mediana]:.2f}')

print(f'{notas[-1]:.2f}')





