class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

pesos = Stack()

pes = -1
while pes != 0:
  pes = int(input())
  pesos.push(pes)

pesos.pop()

wanted = int(input())

totalPeso = 0
totalTirados = 0
for i in range(pesos.size()):
  na_mao = pesos.pop()
  print(f'Peso retirado: {na_mao}')
  totalPeso += na_mao
  if(na_mao!=wanted):
    totalTirados+=1
  elif(na_mao==wanted):
    totalTirados+=1
    break

print("Anilhas retiradas: %d" %totalTirados)
print(f'Peso total movimentado: {totalPeso}')
