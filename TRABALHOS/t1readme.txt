A partir de agora focaremos na implementação do problema. Recapitulando o que precisa ser feito:

Você irá ajudar Mando em duas tarefas específicas. A primeira é decodificar a lista de missões disponíveis. A segunda é selecionar o subconjunto de missões que maximizem o retorno em Beskar (estamos falando de maximizar o retorno financeiro), dada a quantidade de tempo que Mando tem disponível.

Ambas tarefas serão implementadas e avaliadas nesta questão. Para isso, preste atenção no que está sendo solicitado abaixo.


Primeira Tarefa - Decodificação da Lista de Missões
Para ser possível decodificar a lista de missões, as seguintes assinaturas de funções precisam ser implementadas exatamente seguindo a descrição apresentada abaixo.

def adicionar_alfabeto(deque, alfabeto) - esta função adiciona ao objeto deque, do tipo Deque, cada caractere contido no parâmetro alfabeto (tipo string). A sequencia de caracteres adicionadas em deque deve seguir exatamente a mesma sequência contida no parâmetro alfabeto. Utilize os métodos já implementados na classe Deque para manipular esta estrutura de dados.

def decifrar(deque, texto_cifrado, chave) - esta função recebe como parâmetro o texto_cifrado e utilizando o parâmetro chave (deslocamento) aplica o algoritmo de decifração apresentado. Neste ponto, o parâmetro deque é a estrutura de dados do tipo Deque que contém o alfabeto utilizado para cifragem do texto_cifrado. Você deve utilizar os métodos estudados na estrutura do tipo Deque, de forma a ser possível navegar pelo alfabeto armazenado. Note que no processo de remover sistematicamente o elemento da cabeça (front) e adicioná-lo na calda (rear), você estará movendo os elementos do alfabeto armazenados na estrutura para a direita. O processo de remover sistematicamente o elemento da calda (rear) e adicioná-lo na cabeça (front), você estará movendo os elementos do alfabeto para a esquerda. Todo o elemento removido do objeto deque precisa ser novamente inserido. Ao final, o objeto deque, recebido como parâmetro da função, precisa continuar a ter todos os elementos originais do dicionário previamente armazenados.


Entrada
A função adicionar_alfabeto(deque, alfabeto) tem como parâmetro o objeto deque do tipo Deque. Inicialmente, o objeto deque não possui valor armazenado. O parâmetro alfabeto é uma string, sendo 1≤len(alfabeto)≤149, contendo o alfabeto que será utilizado pela função decifrar(). É assegurado que não há caracteres duplicados no alfabeto informado.

A função decifrar(deque, texto_cifrado, chave) tem como parâmetro o objeto deque do tipo Deque, sendo 1≤len(alfabeto)≤149, inicializado com alfabeto a ser utilizado no processo de decriptação. O parâmetro texto_cifrado representa o texto a ser decifrado pela função decifrar(). Sendo 0<len(texto_cifrado). O parâmetro chave representa a quantidade de posições de deslocamento a ser aplicado no algoritmo de decifração. Onde, 0≤ chave.


Saída
A função adicionar_alfabeto() não retorna nenhum valor. Somente o conteúdo do objeto deque é alterado conforme descrição apresentada.

A função decifrar() retorna uma string contendo o conteúdo de texto_cifrado, agora decifrado.



Segunda Tarefa - Selecionar Subconjunto de Missões
Uma vez implementadas as funções da primeira tarefa, você está pronto para ajudar Mando a definir o subconjunto de Missões que maximizem o seu ganho.

Seja o problema definido por:

Dado um conjunto I={1,2,3,...,N} de missões, onde cada missão i∈I possui uma duração de tempo Wi horas e um valor de recompensa de Vi gramas de Beskar associados. Dado uma Janela de tempo disponível de W horas, selecione um subconjunto S∈I de missões, tal que ∑i∈SWi≤W e ∑i∈SVi é máximo.

Entrada
Para esta tarefa, a implementação da descrição da entrada e da solução DEVERÃO ser implementadas no escopo da função selecionar_subconjunto_missoes(). É possível a implementação de sub-funções desde que elas, OBRIGATORIAMENTE, sejam invocadas dentro da função selecionar_subconjunto_missoes(). Códigos implementados fora do escopo desta função irão gerar erros nos casos de testes.

A entrada é composta por várias linhas. A primeira linha possui um inteiro W (0≤W≤1000) que indica a quantidade de horas que Mando tem disponível para participar das missões. A próxima linha possui um inteiro M, que pode assumir somente os valores 0 ou 1. O valor 1 indica que as missões pertencentes ao conjunto solução S devem ser apresentadas, conforme descrito na seção Saída. O valor 0 indica que elas não devem ser apresentadas. A próxima linha possui um inteiro O (0≤O≤3), que representa o índice da coluna em que deve ser iniciada a sequencia para a aplicação do algoritmo de ordenação crescente (ordenação crescente seguindo critério de múltiplas colunas), sendo elas:

O = 0 -- Iniciar a ordenação da resposta pela coluna que representa o nome da missão, seguido por duração, valor e nível de dificuldade (0, 1, 2, 3);
O = 1 -- Iniciar a ordenação da resposta pela coluna que representa a duração da missão, seguido por nome, valor e nível de dificuldade (1, 0, 2, 3);
O = 2 -- Iniciar a ordenação da resposta pela coluna que representa a o valor da missão, seguido por nome, duração e nível de dificuldade (2, 0, 1, 3);
O = 3 -- Iniciar a ordenação da resposta pela coluna que representa o nível de dificuldade da missão, seguido por nome, duração e valor (3, 0, 1, 2);
A próxima linha possui um valor string A (0<len(A)≤149), que representa o alfabeto utilizado pela função cifrar e deve ser utilizado na função de decifrar(). É assegurado que não há caracteres duplicados no alfabeto informado. A próxima linha possui um valor inteiro C (0≤ C) que indica a quantidade de posições de deslocamento a ser aplicado no algoritmo de decriptação (chave). A próxima linha possui um valor inteiro N (0≤N≤50) que indica o número de missões cifradas que serão informadas. A seguir, as próximas N linhas possuem, cada uma, uma string i que representa uma missão cifrada. O conteúdo da string i encontra-se delimitado entre colchetes "[texto_cifrado]". É importante notar que os colchetes são apenas delimitadores e não fazem parte do conteúdo a ser decifrado.

Exemplo:

print(texto_cifrado)

"[d53vQurQ3z99r5Lu:8rtr5L'r258L4z'v2Quzwzt:2uruv]"

O texto_cifrado a ser decifrado (sem áspas):

print(decifrar(d, "d53vQurQ3z99r5Lu:8rtr5L'r258L4z'v2Quzwzt:2uruv", chave))

Nome_da_missao,duracao,valor,nivel_dificuldade
Após a decodificação do texto_cifrado, cada missão i é formada pelos seguintes parâmetros separados por vírgula.

Nome_da_missão - string de texto, com 0<len(nome_da_missao)
duração - valor inteiro, com 0<duracao≤30, representa Wi.
valor - valor inteiro, com 0<valor≤331, representa Vi.
nivel_dificuldade - string que pode assumir um dos valores: hard, medium e easy.
Exemplo:

print(decifrar(d, "Johw0lyg8Cg olgThukhsvyphuB87B979Bohyk", chave))

Chapter 1: The Mandalorian,10,202,hard


Saída
A saída é formada por multiplas linhas.  Deve ser apresentado o conjunto solução S, tal que S∈I, ∑i∈SWi≤W e ∑i∈SVi é máximo. As missões pertencentes ao conjunto solução S devem ser apresentadas uma por linha e estarem ordenadas segundo o parâmetro de entrada O, caso o parâmetro de entrada de M for M==1. Em seguida, deve ser apresentado o tempo disponível para Mando após descontado os tempos Wi referentes as missões que fazem parte do conjunto solução S. Por fim, deve ser apresentado o valor em Beskar que será obtido por Mando ao realizar as missões selecionadas no conjunto solução S.

É importante destacar que o parâmetro de entrada M diz respeito somente a apresentação das missões pertecentes ao conjunto solução S. Os demais valores de saída devem ser apresentados independete do valor de M.

O formato em que essas informações devem ser informadas estão definidos nos casos de teste exemplo abaixo.

For example:

Test	Input	Result
d = Deque()
adicionar_alfabeto(d, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
print(f'Alfabeto: {d}')
print(f'Tamanho: {len(str(d))}')
Alfabeto: ABCDEFGHIJKLMNOPQRSTUVWXYZ
Tamanho: 26
d = Deque()
adicionar_alfabeto(d, ' ')
print(f'Alfabeto: {d}')
print(f'Tamanho: {len(str(d))}')
Alfabeto:  
Tamanho: 1
d = Deque()
adicionar_alfabeto(d, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
texto_cifrado = 'DBTB'
print(f'texto_plano: {decifrar(d, texto_cifrado, 1)}')
print(f'{str(d)}')
print(f'{len(str(d))}')
texto_plano: CASA
ABCDEFGHIJKLMNOPQRSTUVWXYZ
26
d = Deque()
adicionar_alfabeto(d, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
texto_cifrado = 'ECUC'
print(f'texto_plano: {decifrar(d, texto_cifrado, 2)}')
print(f'{str(d)}')
print(f'{len(str(d))}')
texto_plano: CASA
ABCDEFGHIJKLMNOPQRSTUVWXYZ
26
selecionar_subconjunto_missoes()
1000
1
0
ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz0123456789,;:'()_
19
2
[l0xsg4wsZ7w;st6ws:0xsfx)MECMDFDM0t,w]
[l0xsWt6vxs7ysW,tz76;MDDMFDFM5xw1'5]
The Dance of Dragons, 11, 313, medium
The Old Gods and the New, 20, 131, hard
Tempo restante: 969
Valor: 444
selecionar_subconjunto_missoes()
1000
0
0
ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz0123456789,;:'()_
19
2
[V0t8:x,sDEOsl0xsk1xzxMEFMFJM5xw1'5]
[e7v316zu1,wMFMEGDM5xw1'5]
