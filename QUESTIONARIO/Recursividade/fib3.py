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

print(f'fibonacci({valor}) = {Fibo}.')

x = dict(contador)
#print(x)
contador = 0

if(valor == 1):
  print('0 chamada(s) a fibonacci(0).')
  for i in sorted (x.keys()):
    print(f'{x[i]} chamada(s) a fibonacci({i}).')
else:
  for i in sorted (x.keys()):
    print(f'{x[i]} chamada(s) a fibonacci({i}).')
