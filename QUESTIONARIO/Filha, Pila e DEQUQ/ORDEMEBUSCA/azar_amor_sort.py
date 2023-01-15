n, k = [int(i) for i in input().split()]
numeros = []
for i in range(n):
    numero = int(input())
    negativo = 0
    modulo = numero % k
    if numero < 0:
        modulo = -(-numero % k)
        negativo = 1
    if (numero % 2) == 0:
        par = 1
    else:
        par = 0

    numeros.append([numero,modulo,par, negativo]) #
numeros.sort(key=lambda x: (x[1], x[2], x[0] if x[2] == 1 else -x[0]),reverse=True)
final = []
for numero in numeros:
    final.append(numero[0])
print(*final)