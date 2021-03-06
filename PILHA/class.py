from __future__ import annotations
from typing import List, Any
from copy import deepcopy

class Stack:
  def __init__(self) -> None:
    self.__data: List[Any] = []
    self.__index = 0
  #pode ser post
  def append(self, item: Any) -> None:
    self.__data.append(item)

  #pop index do topo, APENAS
  def pop(self) -> Any:
    return self.__data.pop()

  #peek verifica vazio ou n
  def peek(self) -> Any:
    if not self.__data:
      return []
    return self.__data[-1]
  
  #realiza print
  def __repr__(self) -> str:
    return f'{self.__class__.__name__}({self.__data})'
  
  #iterations
  def __iter__(self) -> Stack:
    self.__index = len(self.__data)
    return self
  
  #next
  def __next__(self) -> Any:
    if self.__index == 0:
      raise StopIteration
    self.__index-=1
    return self.__data[self.__index]

  def __bool__(self) -> bool:
    return bool(self.__data)

if __name__ == "__main__":
  stack = Stack()

  stack.append('A')
  stack.append('B')
  stack.append('c')

  top_item = stack.pop()

  print(stack, top_item)

  print("FOR")
  for item in stack:
    print(item)
    
  '''while stack:
    print(stack.pop())'''

  stack_copia = deepcopy(stack)
  
  print("WHILE")

  while stack_copia:
    print(stack_copia.pop())
  
  print(stack)