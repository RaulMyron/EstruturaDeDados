def fibonacci(valor):
  lista = [0, 1]
  if(valor == 1):
    return [0]
  elif(valor == 2):
    return [0,1]
  else:
    for i in range(2, valor):
      lista.append(lista[i-1] + lista[i-2])
  return lista