import re

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

palavras = Stack()
Numeros = Stack()

frase = input().split()

for i in frase:
  if(re.search(r'\d', i)):
    Numeros.push(i)
  else:
    palavras.push(i)

print("Palavras:")

while palavras.size():
  print(palavras.pop())

print("\nNumeros:")

while Numeros.size():
  print(Numeros.pop())