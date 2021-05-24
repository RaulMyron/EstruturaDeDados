def escolha_premiada(valores, qtd, soma):
	if (soma == 0):
		return True
	if (qtd == 0):
		return False
	return escolha_premiada(valores, qtd-1, soma) or escolha_premiada(valores, qtd-1, soma-valores[qtd-1])

valores = list(map(int, input().split()))
sorteado = int(input())

if escolha_premiada(valores, len(valores), sorteado):
  print("E possivel ganhar.")
else:
	print("Impossivel ganhar.")