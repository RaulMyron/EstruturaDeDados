from collections import Counter
contador = Counter()

def Fib(valor):
  contador[valor]+=1
  if(valor==0):
    return 0
  elif(valor==1):
    return 1
  else:
    return Fib(valor-1) + Fib(valor-2)

valor = int(input())

Fibo = Fib(valor)
values = (contador.values())
soma = 0
for i in values:
  soma+=i

print(f'Fib({valor}) = {Fibo} ({soma} chamadas)')