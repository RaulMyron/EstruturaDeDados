def fat(valor):
  if(valor==0):
    return 1
  if(valor == 1):
    return 1
  else:
    return valor * fat(valor-1)

def fatorial(valor):
  return fat(valor)%2357

print(fatorial(int(input())))
