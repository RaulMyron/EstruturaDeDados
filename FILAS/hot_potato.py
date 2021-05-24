class Queue:
  def __init__(self):
      self.items = []

  def isEmpty(self):
      return self.items == []

  def enqueue(self, item):
      self.items.insert(0,item)

  def dequeue(self):
      return self.items.pop()

  def size(self):
      return len(self.items)

def hotPotato(namelist, num):
  simqueue = Queue()

  #coloca todas os items da lista na queue
  for name in namelist:
    simqueue.enqueue(name)

  #enquanto a lista existir
  while simqueue.size() > 1:
    #coloca o primeiro no final
    for i in range(num):
      print(i)
      simqueue.enqueue(simqueue.dequeue())
    #tira um
    simqueue.dequeue()

  return simqueue.dequeue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))