#altura ideal = 1,80m  (prefere tanto faz)
#peso ideal = 75kg (prefere o mais leve)
#se tem dois iguais, pelo sobrenome e depois pelo primeiro nome

n = int(input())
pretendentes = []

for i in range(n):
    nome, sobrenome, altura, peso = input().split()
    
    altura = int(altura)
    peso = int(peso)
    
    altura = abs(altura - 180)
    peso = peso-75
    
    mais_leve = 0
    
    if peso > 0:
        mais_leve = 1
        
    pretendentes.append([sobrenome, nome, altura, peso, mais_leve])
    
pretendentes.sort(key=lambda x: (x[2],x[4], -x[3] if x[3] < 0 else x[3], x[0], x[1]),)

for pessoa in pretendentes:
    print(f'{pessoa[0]}, {pessoa[1]}')