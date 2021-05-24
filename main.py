def verifica(pessoas_mussum, pessoas):
  contador = 0
  verifica_inamizade = True
  for mussum_amigos in pessoas_mussum:
    for pessoas_co in pessoas:
      if(mussum_amigos == pessoas_co):
        contador+=1
        print(mussum_amigos)
        print(pessoas_co)
        print("opa")
      if(pessoas_co == "Mussum"):
        verifica_inamizade = False
  return contador, verifica_inamizade

n = int(input())

if(n==1):
  print("Cacildis! Cade elis?")
else:
  #mussum data
  ide_1, a_1, pessoas_1 = input().split(" ", 2)
  a = int(a_1)
  pessoas_1 = (pessoas_1.split())

  amigo = []

  for i in range(n-1):
    ide, a, pessoas = input().split(" ", 2)
    a = int(a)
    pessoas = (pessoas.split())
    #print(pessoas)
    x = verifica(pessoas_1, pessoas)
    if(x[0]>=2 and x[1]==True):
      amigo.append(ide)

  if amigo: 
    amigo.sort()
    #print('----------')
    for i in amigo:
      print(i)
  else:
    print('Cacildis! Cade elis?')