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
def jogador(jogador):
    if(jogador == 0):
        return "x"
    else:
        return "o"
    
def imprimirTabuleiro(tabuleiro):
    for i in range(3):
        print("|".join(tabuleiro[i]))
        if(i<2):
            print("______")

#Verifica se posição indicada esta dentro do tabuleiro
def verificaJogadaValida(indice):
    if(indice < 0 or indice >2):
        print("Indice invalido! Informe um indice entre 0 e 2.")
        return False
    return True

#Verifica se posição do tabuleiro esta ocupada
def verificaPosicaoVazia(tabuleiro, i, j):
    if(tabuleiro[i][j] != vazia):
        print("Indice invalido! Posicao ja ocupada.")
        return False
    return True

#Retorna o tabuleiro que resulta ao fazer a jogada i,j
def resultado(tabuleiro, i, j, njogador):
    tabuleiro[i][j] = jogador(njogador)
    imprimirTabuleiro(tabuleiro)

def aindaPossuiPosicaoVazia(tabuleiro):
    qtdPosicoesOcupadas: 0
    for i in range(3):
        for j in range(3):
            if(tabuleiro[i][j] == vazia):
                qtdPosicoesOcupadas = qtdPosicoesOcupadas + 1
    return qtdPosicoesOcupadas

def quemGanhou(tabuleiro):
    if(aindaPossuiPosicaoVazia(tabuleiro) != 9):
        return vazia
    if(tabuleiro[0][0] != vazia and tabuleiro[0][0] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][2]):
        return tabuleiro[0][0]
    if(tabuleiro[0][2] != vazia and tabuleiro[0][2] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][0]):
        return tabuleiro[0][2]
    for i in range(3):
        if(tabuleiro[i][0] != vazia and tabuleiro[i][0] == tabuleiro[i][1] and tabuleiro[i][1] == tabuleiro[i][2]):
            return tabuleiro[i][0]
    for i in range(3):
        if(tabuleiro[0][i] != vazia and tabuleiro[0][i] == tabuleiro[1][i] and tabuleiro[1][i] == tabuleiro[2][i]):
            return tabuleiro[0][i]
    return "EMPATE"

