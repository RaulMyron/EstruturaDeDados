def decompress(zipado):
  alfa = '-ABCDEFGHIJKLMNOPQRSTUVWXYZ'

  ValorIndex = zipado
  resto = ValorIndex%32
  sobra = ValorIndex//32

  if(resto == 0):
    return ''
  else:
    return alfa[resto] + decompress(sobra)
