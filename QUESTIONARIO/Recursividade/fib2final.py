def fibonacci(valor):
  if valor == 0:
    return []
  if valor == 1:
    return [0]
  elif valor == 2:
    return [0,1]
  else:
    lista = fibonacci(valor-1)
    lista.append(sum(lista[:-3:-1]))
    return lista

print(fibonacci(10))

#https://www.mygreatlearning.com/blog/fibonacci-series-in-python/