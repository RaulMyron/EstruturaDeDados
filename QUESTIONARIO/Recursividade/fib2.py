from collections import Counter
contador = Counter()
def fibonacci(valor):
  def fib(valor):
    if(valor==0):
      #contador[valor] = 0
      return 0
    elif(valor==1):
      #contador[valor] = 1
      return 1
    else:
      valor2 = fib(valor-1) + fib(valor-2)
      contador[valor]=valor2
      return contador[valor]

  if(valor==1):
    return [0]
  elif(valor==2):
    return [0, 1]
  
  fib(valor)

  x = list(contador.values())
  x.insert(0, 1)
  x.insert(0, 0)


  return x[0:valor]

print(fibonacci(30))

