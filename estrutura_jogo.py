#  Exercício 2: Busca Competitiva  (Jogo da Velha) 
# Aluno: Thiago Emanuel

# posição não marcada
vazia = " "

#Inicializar tabuleiro
def initTabuleiro():
    tabuleiro = [
        [vazia, vazia, vazia],
        [vazia, vazia, vazia],
        [vazia, vazia, vazia],
    ]
    return tabuleiro

#Retorna X ou O
def jogador(tabuleiro):
    for i in range(3):
        for j in range(3):
            if(tabuleiro[i][j] == 1):
                return "X"
            else:
                return "O"

#Retorna todas as jogadas disponíveis
def acoes(tabuleiro):
    for i in range(3):
        for j in range(3):
            if(tabuleiro[i][j] == vazia):
                print("Posicao: ".join(tabuleiro[i][j].join(" disponível!")))

#Retorna o tabuleiro que resulta ao fazer a jogada i,j
def resultado(tabuleiro, acao):

#Retorna o ganhador, se houver
def ganhador(tabuleiro):

#Retorna Verdadeiro se o jogo acabou, Falso caso contrário
def final(tabuleiro):

#Retorna 1 se X ganhou, -1 se 0 ganhou, 0 caso contrário.
def custo(tabuleiro):

#Retorna a jogada ótima para o jogador atual
def minimax(tabuleiro):

def maxValor(tabuleiro):
def minValor(tabuleiro):