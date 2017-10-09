#!/usr/bin/env python

# Universidade Federal de Mato-Grosso - Campus Universitario do Araguaia
# Trabalho de Inteligencia Artificial - 8 Puzzle 
# Professor: Robson Silva Lopes
# Alunos: Vitor Rezende, Guilherme Henrique, Guilherme Santana

# Variaveis Globais
TodasJogadas = []

# Classe para o no de cada jogada
class noPuzzle:
    jogada = [None]*9
    pai = None
    filhos = None
    nivel = 0
    qtdfilhos = 0
    movimento = None
    
    # Construtor
    def __init__(self, jogada, nivel):
        self.jogada = jogada
        self.pai = None
        self.filhos = []
        self.qtdfilhos = 0
        self.nivel = nivel
        self.movimento = "Neutrox"
          
    # Metodo para gerar o filhos de cada no
    def GeraFilhos (self):
        global TodasJogadas, nivel
        # Salvo o local que encontra a peca vazia, aka representada pelo numero 9
        local = self.jogada.index(9)
        # Salvo todas jogadas acontecidas na lista TodasJogadas para evitar que seja gerado nos repetidos
	if ( self.pai == None ):
	  TodasJogadas.append (self.jogada)
      
        # Para cada local, novas jogadas diferentes sao geradas e testadas
        # Tratando caso 0
        if ( local == 0 ):
	  # Primeira jogada do caso 0
	  novaJogada = self.jogada[:]
          novaJogada[0] = novaJogada[1]
          novaJogada[1] = 9
          # Se a novaJogada ainda nao foi efetuada, entao salvaremos ela
          # Checagem eh feita percorrendo a lista de TodasJogadas, comparando-as com a nova
          if novaJogada not in TodasJogadas:
	    TodasJogadas.append(novaJogada)
	    self.qtdfilhos = self.qtdfilhos + 1
	    filho = noPuzzle (novaJogada, self.nivel + 1)
	    filho.pai = self
	    filho.movimento = "1)Direita"
	    self.filhos.append(filho)
	    
          # Segunda jogada do caso 0
          novaJogada = self.jogada[:]
          novaJogada[0] = novaJogada[3]
          novaJogada[3] = 9
          # Se a novaJogada ainda nao foi efetuada, entao salvaremos ela
          # Checagem eh feita percorrendo a lista de TodasJogadas, comparando-as com a nova
          if novaJogada not in TodasJogadas:
	    TodasJogadas.append(novaJogada)
	    self.qtdfilhos = self.qtdfilhos + 1
	    filho = noPuzzle (novaJogada, self.nivel + 1)
	    filho.pai = self
	    filho.movimento = "3)Para Baixo"
	    self.filhos.append(filho)
	        
	# Tratando caso 1    
        if ( local == 1 ):
	  # Primeira jogada do caso 1
	  novaJogada = self.jogada[:]
          novaJogada[1] = novaJogada[0]
          novaJogada[0] = 9
          if novaJogada not in TodasJogadas:
	    TodasJogadas.append(novaJogada)
	    self.qtdfilhos = self.qtdfilhos + 1
	    filho = noPuzzle (novaJogada, self.nivel + 1)
	    filho.pai = self
	    filho.movimento = "0)Esquerda"
	    self.filhos.append(filho)
          
          # Segunda jogada do caso 1
          novaJogada = self.jogada[:]
          novaJogada[1] = novaJogada[2]
          novaJogada[2] = 9
          if novaJogada not in TodasJogadas:
	    TodasJogadas.append(novaJogada)
	    self.qtdfilhos = self.qtdfilhos + 1
	    filho = noPuzzle (novaJogada, self.nivel + 1)
	    filho.pai = self
	    filho.movimento = "1)Direita"
	    self.filhos.append(filho)
          
          # Terceira jogada do caso 1
          novaJogada = self.jogada[:]
          novaJogada[1] = novaJogada[4]
          novaJogada[4] = 9
          if novaJogada not in TodasJogadas:
	    TodasJogadas.append(novaJogada)
	    self.qtdfilhos = self.qtdfilhos + 1
	    filho = noPuzzle (novaJogada, self.nivel + 1)
	    filho.pai = self
	    filho.movimento = "3)Para Baixo"
	    self.filhos.append(filho)  
          
	# Tratando caso 2
        if ( local == 2 ):
	  # Primeira jogada do caso 2
	  novaJogada = self.jogada[:]
          novaJogada[2] = novaJogada[1]
          novaJogada[1] = 9
          if novaJogada not in TodasJogadas:
	    TodasJogadas.append(novaJogada)
	    self.qtdfilhos = self.qtdfilhos + 1
	    filho = noPuzzle (novaJogada, self.nivel + 1)
	    filho.pai = self
	    filho.movimento = "0)Esquerda"
	    self.filhos.append(filho)
          
          # Segunda jogada do caso 2
          novaJogada = self.jogada[:]
          novaJogada[2] = novaJogada[5]
          novaJogada[5] = 9
          if novaJogada not in TodasJogadas:
	    TodasJogadas.append(novaJogada)
	    self.qtdfilhos = self.qtdfilhos + 1
	    filho = noPuzzle (novaJogada, self.nivel + 1)
	    filho.pai = self
	    filho.movimento = "3)Para Baixo"
	    self.filhos.append(filho)   
	    
	# Tratando caso 3
	if ( local == 3 ):
	  # Primeira jogada caso 3
	  novaJogada = self.jogada[:]
          novaJogada[3] = novaJogada[0]
          novaJogada[0] = 9
          if novaJogada not in TodasJogadas:
	    TodasJogadas.append(novaJogada)
	    self.qtdfilhos = self.qtdfilhos + 1
	    filho = noPuzzle (novaJogada, self.nivel + 1)
	    filho.pai = self
	    filho.movimento = "2)Para Cima"
	    self.filhos.append(filho)
          
          # Segunda jogada caso 3
          novaJogada = self.jogada[:]
          novaJogada[3] = novaJogada[4]
          novaJogada[4] = 9
          if novaJogada not in TodasJogadas:
	    TodasJogadas.append(novaJogada)
	    self.qtdfilhos = self.qtdfilhos + 1
	    filho = noPuzzle (novaJogada, self.nivel + 1)
	    filho.pai = self
	    filho.movimento = "1)Direita"
	    self.filhos.append(filho)    
	  
	  # Terceira jogada caso 3
	  novaJogada = self.jogada[:]
          novaJogada[3] = novaJogada[6]
          novaJogada[6] = 9
          if novaJogada not in TodasJogadas:
	    TodasJogadas.append(novaJogada)
	    self.qtdfilhos = self.qtdfilhos + 1
	    filho = noPuzzle (novaJogada, self.nivel + 1)
	    filho.pai = self
	    filho.movimento = "3)Para Baixo"
	    self.filhos.append(filho)     
	    
	# Tratando caso 4    
        if ( local == 4 ):
	    # Primeira jogada caso 4
            novaJogada = self.jogada[:]
            novaJogada[4] = novaJogada[1]
            novaJogada[1] = 9
            if novaJogada not in TodasJogadas:
	      TodasJogadas.append(novaJogada)
	      self.qtdfilhos = self.qtdfilhos + 1
	      filho = noPuzzle (novaJogada, self.nivel + 1)
	      filho.pai = self
	      filho.movimento = "2)Para Cima"
	      self.filhos.append(filho)

            # Segunda jogada caso 4
            novaJogada = self.jogada[:]
            novaJogada[4] = novaJogada[3]
            novaJogada[3] = 9
            if novaJogada not in TodasJogadas:
	      TodasJogadas.append(novaJogada)
	      self.qtdfilhos = self.qtdfilhos + 1
	      filho = noPuzzle (novaJogada, self.nivel + 1)
	      filho.pai = self
	      filho.movimento = "0)Esquerda"
	      self.filhos.append(filho)
            
            # Terceira jogada caso 4
            novaJogada = self.jogada[:]
            novaJogada[4] = novaJogada[5]
            novaJogada[5] = 9
            if novaJogada not in TodasJogadas:
	      TodasJogadas.append(novaJogada)
	      self.qtdfilhos = self.qtdfilhos + 1
	      filho = noPuzzle (novaJogada, self.nivel + 1)
	      filho.pai = self
	      filho.movimento = "1)Direita"
	      self.filhos.append(filho)
            
            # Quarta jogada caso 4
            novaJogada = self.jogada[:]
            novaJogada[4] = novaJogada[7]
            novaJogada[7] = 9
            if novaJogada not in TodasJogadas:
	      TodasJogadas.append(novaJogada)
	      self.qtdfilhos = self.qtdfilhos + 1
	      filho = noPuzzle (novaJogada, self.nivel + 1)
	      filho.pai = self
	      filho.movimento = "3)Para Baixo"
	      self.filhos.append(filho)
               
	# Tratando caso 5    
        if ( local == 5 ):
	   # Primeira jogada caso 5
           novaJogada = self.jogada[:]
           novaJogada[5] = novaJogada[2]
           novaJogada[2] = 9
           if novaJogada not in TodasJogadas:
	     TodasJogadas.append(novaJogada)
	     self.qtdfilhos = self.qtdfilhos + 1
	     filho = noPuzzle (novaJogada, self.nivel + 1)
	     filho.pai = self
	     filho.movimento = "2)Para Cima"
	     self.filhos.append(filho)

           # Segunda jogada caso 5
           novaJogada = self.jogada[:]
           novaJogada[5] = novaJogada[4]
           novaJogada[4] = 9
           if novaJogada not in TodasJogadas:
	     TodasJogadas.append(novaJogada)
	     self.qtdfilhos = self.qtdfilhos + 1
	     filho = noPuzzle (novaJogada, self.nivel + 1)
	     filho.pai = self
	     filho.movimento = "0)Esquerda"
	     self.filhos.append(filho)
           
           # Terceira jogada caso 5
           novaJogada = self.jogada[:]
           novaJogada[5] = novaJogada[8]
           novaJogada[8] = 9
           if novaJogada not in TodasJogadas:
	     TodasJogadas.append(novaJogada)
	     self.qtdfilhos = self.qtdfilhos + 1
	     filho = noPuzzle (novaJogada, self.nivel + 1)
	     filho.pai = self
	     filho.movimento = "3)Para Baixo"
	     self.filhos.append(filho)
           
	    
	# Tratando caso 6
        if ( local == 6 ):
	   # Primeira jogada caso 6
           novaJogada = self.jogada[:]
           novaJogada[6] = novaJogada[3]
           novaJogada[3] = 9
           if novaJogada not in TodasJogadas:
	     TodasJogadas.append(novaJogada)
	     self.qtdfilhos = self.qtdfilhos + 1
	     filho = noPuzzle (novaJogada, self.nivel + 1)
	     filho.pai = self
	     filho.movimento = "2)Para Cima"
	     self.filhos.append(filho)

           # Segunda jogada caso 6
           novaJogada = self.jogada[:]
           novaJogada[6] = novaJogada[7]
           novaJogada[7] = 9
           if novaJogada not in TodasJogadas:
	     TodasJogadas.append(novaJogada)
	     self.qtdfilhos = self.qtdfilhos + 1
	     filho = noPuzzle (novaJogada, self.nivel + 1)
	     filho.pai = self
	     filho.movimento = "1)Direita"
	     self.filhos.append(filho)

	    
	# Tratando caso 7
        if ( local == 7 ):
	   # Primeira jogada caso 7
           novaJogada = self.jogada[:]
           novaJogada[7] = novaJogada[4]
           novaJogada[4] = 9
           if novaJogada not in TodasJogadas:
	     TodasJogadas.append(novaJogada)
	     self.qtdfilhos = self.qtdfilhos + 1
	     filho = noPuzzle (novaJogada, self.nivel + 1)
	     filho.pai = self
	     filho.movimento = "2)Para Cima"
	     self.filhos.append(filho)

           # Segunda jogada caso 7
           novaJogada = self.jogada[:]
           novaJogada[7] = novaJogada[6]
           novaJogada[6] = 9
           if novaJogada not in TodasJogadas:
	     TodasJogadas.append(novaJogada)
	     self.qtdfilhos = self.qtdfilhos + 1
	     filho = noPuzzle (novaJogada, self.nivel + 1)
	     filho.pai = self
	     filho.movimento = "0)Esquerda"
	     self.filhos.append(filho)
            
           # Terceira jogada caso 7
           novaJogada = self.jogada[:]
           novaJogada[7] = novaJogada[8]
           novaJogada[8] = 9
           if novaJogada not in TodasJogadas:
	     TodasJogadas.append(novaJogada)
	     self.qtdfilhos = self.qtdfilhos + 1
	     filho = noPuzzle (novaJogada, self.nivel + 1)
	     filho.pai = self
	     filho.movimento = "1)Direita"
	     self.filhos.append(filho)   
            
        # Tratando caso 8
        if ( local == 8 ):
	   # Primeira jogada caso 8
           novaJogada = self.jogada[:]
           novaJogada[8] = novaJogada[5]
           novaJogada[5] = 9
           if novaJogada not in TodasJogadas:
	     TodasJogadas.append(novaJogada)
	     self.qtdfilhos = self.qtdfilhos + 1
	     filho = noPuzzle (novaJogada, self.nivel + 1)
	     filho.pai = self
	     filho.movimento = "2)Para Cima"
	     self.filhos.append(filho)
  
           # Segunda jogada caso 8
           novaJogada = self.jogada[:]
           novaJogada[8] = novaJogada[7]
           novaJogada[7] = 9
           if novaJogada not in TodasJogadas:
	     TodasJogadas.append(novaJogada)
	     self.qtdfilhos = self.qtdfilhos + 1
	     filho = noPuzzle (novaJogada, self.nivel + 1)
	     filho.pai = self
	     filho.movimento = "0)Esquerda"
	     self.filhos.append(filho)
    #code
    
# Funcao para a busca em largura
def Largura (estado):
    Lista = []				# Lista para implementar a busca
    objetivo = [1,2,3,8,9,4,7,6,5]	# Estado Objetivo que queremos alcancar
  
    while (1):
        # Se o estado for o objetivo, retorne-o
        if (objetivo == estado.jogada):
            return estado
	# Se nao, gere seus filhos
        else:
	    if (estado.qtdfilhos == 0):
	      estado.GeraFilhos()
	      # Na busca em largura, adicionar os filhos de cada no ao FINAL da lista
	      Lista += estado.filhos
        # Se a lista inteira for percorrida e nada tiver sido encontrado retorne falso
        if (Lista == []) :
            return False
        print estado.nivel
        estado = Lista[0]
        del Lista[0]
        
# Funcao para a busca em profundidade         
def Profundidade (estado):
    Lista = []				# Lista para implementar a busca
    objetivo = [1,2,3,8,9,4,7,6,5]	# Estado Objetivo que queremos alcancar
    while (1):
	# Se o estado for o objetivo, retorne-o
        if (objetivo == estado.jogada):
            return estado
	# Se nao, gere seus filhos
        else:
	    if (estado.qtdfilhos == 0):
	      estado.GeraFilhos()
	      # Na busca em profundidade, adicionar os filhos de cada no ao INICIO da lista
	      Lista = estado.filhos + Lista
        # Se a lista inteira for percorrida e nada tiver sido encontrado retorne falso    
        if (Lista == []) :
            return False
        print estado.nivel
        estado = Lista[0]
        del Lista[0]

# Funcao para a busca em profundidade interativa        
def ProfundidadeIterativa (estado, nivelmax):
    Lista = []				# Lista para implementar a busca
    objetivo = [1,2,3,8,9,4,7,6,5]	# Estado Objetivo que queremos alcancar
    nivel = 1
    while (1):
	# Se o estado for o objetivo, retorne-o
        if (objetivo == estado.jogada):
            return estado
	# Se nao, gere seus filhos
        else:
	    if (estado.qtdfilhos == 0):
	      if ( estado.nivel < nivel ): # Na pronfundidade interativa so expande o no se o mesmo nao ultrapassar o limite da busca
		estado.GeraFilhos()
		Lista = estado.filhos + Lista 
            if nivel < nivelmax:
	      nivel = nivel + 1
        # Se a lista inteira for percorrida e nada tiver sido encontrado retorne falso    
        if (Lista == []) :
	  return False
        
        estado = Lista[0]
        del Lista[0]

# Funcao que imprime a arvore gerada
def Imprime (resultado):
  print "*** M E T A ***"
  while resultado.pai:
    print ""
    print resultado.jogada[0:3]
    print resultado.jogada[3:6]
    print resultado.jogada[6:9]
    print ""
    print resultado.movimento
    print 'Jogada Nivel:',+resultado.nivel
    print "###############"
    resultado = resultado.pai
  print resultado.jogada[0:3]
  print resultado.jogada[3:6]
  print resultado.jogada[6:9]
  print "Estado Inicial"
  print "###############"

# Jogadas iniciais do tabuleiro
Facil = [1,3,4,8,6,2,7,9,5]
Medio = [2,8,1,9,4,3,7,6,5]
Dificil = [2,8,1,4,6,3,9,7,5]
Expert = [5,6,7,4,9,8,3,2,1]

# Main
print ("Trabalho de Inteligencia Artificial: Jogo 8 Puzzle - Buscas cegas")
print ("-=- -=- -= Modos de Dificuldade =- -=- -=-")
print Facil[0:3],
print Medio[0:3],
print Dificil[0:3],
print Expert[0:3]  

print Facil[3:6],
print Medio[3:6],
print Dificil[3:6],
print Expert[3:6] 

print Facil[6:9],
print Medio[6:9],
print Dificil[6:9],
print Expert[6:9] 
print "1)Facil   2)Medio   3)Dificil  4)Expert"

modo = int (raw_input ('Defina a jogada inicial com o modo: '))

# Definindo a dificuldade do problema
if modo == 1:
  jogadaInicial = Facil
if modo == 2:
  jogadaInicial = Medio
if modo == 3:
  jogadaInicial = Dificil
if modo == 4:
  jogadaInicial = Expert

print ("         "),
print jogadaInicial[0:3],
print ("       "),
print ("[1, 2, 3]")
print ("INICIO ->"),
print jogadaInicial[3:6],
print ("META ->"),
print ("[8, 9, 4]")
print ("         "),
print jogadaInicial[6:9],
print ("       "),
print ("[7, 6, 5]")
inicio = noPuzzle(jogadaInicial, 0)

busca = int (raw_input ('Defina o tipo de busca: \n1) Busca em Largura \n2) Busca em Profundidade \n3) Busca com Aprofundamento Iterativo\n0) Sair\n'))

if busca == 0:	# Fechar o programa
  print "Finalizando Programa..."
if busca == 1:	# Busca em Largura
  resultado = Largura (inicio)
  if ( resultado == False ):
    print "Busca nao encontrou solucao"
  else:
    Imprime ( resultado )

if busca == 2:	# Busca em Profundidade
  resultado = Profundidade (inicio)
  if ( resultado == False ):
    print "Busca nao encontrou solucao"
  else:
    Imprime ( resultado )

if busca == 3:	# Busca em profundidade iterativa
  limite = int (raw_input ('Digite o limite da busca: '))
  resultado = ProfundidadeIterativa (inicio, limite)
  if resultado == False:
    print "Busca nao encontrou solucao"
  else:
    Imprime ( resultado )
   
if busca > 3:
  print "Opcao Invalida! Finalizando..."