n = int(input())

for i in range(n):
    palavra_estudada = input()
    copia_palavra = palavra_estudada[:]
    verifica_letra_palavra = True
    for a in range(3):
        palavra_analisada = input()
        for letra in palavra_analisada:
            #print('letra', letra)
            
            if letra not in copia_palavra:
                verifica_letra_palavra = False
                break
            else:
                #print('tem a letra, removendo...')
                copia_palavra = copia_palavra.replace(letra,'',1)
                #print('copia palavra', copia_palavra)
    
    #print('saí do loop', palavra_estudada,'copia_palavra', copia_palavra, 'len', len(copia_palavra),'verifica_letra_palavra',verifica_letra_palavra)
    if(len(copia_palavra)>=1 and verifica_letra_palavra==True):
        arranjado = copia_palavra[:]
        arranjado = [*set(arranjado)]
        strarranjada = ''.join(sorted(arranjado))
        print(f'Bora ralar: {strarranjada}')
    elif(len(copia_palavra)==0 and verifica_letra_palavra==True):
        print("It's in the box")
    elif verifica_letra_palavra == False:
        print('You died!')
