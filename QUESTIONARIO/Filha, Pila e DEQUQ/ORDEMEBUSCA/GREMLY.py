#Quantidade de pontos
#Quantidade de vitórias
#Saldo de gols
#Gols marcados
#Gols sofridos
#Nome do time (ordem alfabética) ??? unfair


#import operator

feirao = []
total = 0

for i in range(20):
  entrada = input()
  #print(entrada)
  nome, gols = entrada.split(" ", 1)

  gols = gols.split()
  #print(gols)
  
  fez = 0
  tomou = 0
  vitoria = 0
  saldo = 0
  pontos = 0

  contador = 0
  for i in gols:
    temp_fez = int(gols[contador][0])
    temp_tomou = int(gols[contador][2])
    fez+=temp_fez
    tomou+=temp_tomou
    #print(temp_fez, temp_tomou)

    if(temp_fez==temp_tomou):
      pontos+=1
      total+=1
    elif(temp_fez>temp_tomou):
      vitoria+=1
      pontos+=3
      total+=3
    
    contador+=1

  saldo = fez-tomou  
  #print(vitoria)
  #print(fez, tomou, pontos)



  feirao.append([str(nome), pontos, vitoria, saldo, fez, tomou])

feirao = sorted(feirao, key = lambda x: (-x[1],-x[2],-x[3],-x[4],-x[5],x[0]))

#feirao = sorted(feirao, key=operator.itemgetter(1, 2, 3, 4, 5, 0), reverse=True)

totalmedia =total/20
print("Media de pontos: %.2f" %totalmedia)
print(f'Liberadores: {feirao[0][0]}, {feirao[1][0]}, {feirao[2][0]}, {feirao[3][0]}')
print(f'Rebaixados: {feirao[-1][0]}, {feirao[-2][0]}, {feirao[-3][0]}, {feirao[-4][0]}')
