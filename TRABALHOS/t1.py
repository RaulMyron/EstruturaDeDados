class Deque:
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return self.__items == []

    def add_front(self, item):
        self.__items.append(item)

    def add_rear(self, item):
        self.__items.insert(0, item)

    def remove_rear(self):
        return self.__items.pop(0)

    def remove_front(self):
        return self.__items.pop()

    def size(self):
        return len(self.__items)

    def __str__(self):
        sdeque = ''
        for i in self.__items:
            sdeque += i
        return sdeque

def adicionar_alfabeto(deque, alfabeto):
  for i in alfabeto:
    deque.add_front(i)
  return None

def decifrar(deque, texto_cifrado, chave):
  
  alfab = str(deque)

  decifrado = ''

  #iteração + lista
  for i in range(len(texto_cifrado)):
    decifrado += str(   alfab[alfab.index(texto_cifrado[i])-chave]   )

  #vo rotar por letra n 

  return decifrado

#tempo disponivel x tempo total das missões (maior valor possivel)
def selecionar_subconjunto_missoes():

  def valor_max(missoes, Wmax):
    return sum([i[2] for i in missoes]) if sum([i[1] for i in missoes]) <= Wmax else 0
  
  temp = {}

  def mochila(missoes, Wmax):
    if not missoes:
        return ( )
      
    if (missoes, Wmax) not in temp:

      original = missoes[0]
      resto = missoes[1:]

      usar = (original,) + mochila(resto, Wmax - original[1])
      nao_usar = mochila(resto, Wmax)

      if valor_max(usar, Wmax) > valor_max(nao_usar, Wmax):
        conj_solucao = usar
      else:
        conj_solucao = nao_usar

      temp[(missoes, Wmax)] = conj_solucao
  
    return temp[(missoes, Wmax)]

  def tipo_print(O, solucoes):
    #zero = "0123"
    #um = "1023"
    #dois = "2013"
    #tres = "3012"
    #defi = ''

    if O == 0:
      #defi = zero
      solucoes = sorted(solucoes, key = lambda x: (x[0],x[1],x[2],x[3]))
    elif O == 1:
      #defi = um
      solucoes = sorted(solucoes, key = lambda x: (x[1],x[0],x[2],x[3]))
    elif O == 2:
      #defi = dois
      solucoes = sorted(solucoes, key = lambda x: (x[2],x[0],x[1],x[3]))
    elif O == 3:
      #defi = tres
      solucoes = sorted(solucoes, key = lambda x: (x[3],x[0],x[1],x[2]))

    #print("defi", defi)
    #print(solucoes)
    for i in solucoes:
      print(i[0], i[1], i[2], i[3], sep=", ")
    
    return None

  Wmax = int(input())
  M = int(input())
  O = int(input())
  
  alfab = str(input())
  alfabDeque = Deque()
  adicionar_alfabeto(alfabDeque, alfab)

  chave = int(input())
  N = int(input())

  missoes = ()

  for i in range(N):
    missao = (decifrar(alfabDeque, str(input())[1:-1], chave))
    nome_missao_local, duracao_local, valor_local, dificuldade_local = missao.split(",")
    duracao_local = int(duracao_local)
    valor_local = int(valor_local)
    missoes += ((nome_missao_local, duracao_local, valor_local, dificuldade_local),)

  solucoes = mochila(missoes, Wmax)

  valor = 0

  for i in solucoes:
    valor+=i[1]

  Trestante = Wmax-valor

  if(M == 1):
    tipo_print(O, solucoes)

  print ("Tempo restante:", Trestante)
  print ("Valor:", valor_max(solucoes, Wmax))
  

selecionar_subconjunto_missoes()
