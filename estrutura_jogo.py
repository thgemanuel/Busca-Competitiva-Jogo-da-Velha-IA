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
def labelJogador(jogador):
    if(jogador == 0):
        return "x"
    else:
        return "o"
        
#imprime tabuleiro
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

#le entrada do jogador
def leEntrada(entrada):
    try:
        indice = int(input(entrada))
        if(verificaJogadaValida(indice)):
            return indice
        else: 
            leEntrada(entrada)
    except:
        return leEntrada(entrada)
            
#Retorna todas as jogadas disponíveis
def acoes(tabuleiro):
    for i in range(3):
        for j in range(3):
            if(tabuleiro[i][j] == vazia):
                print("Posicao disponível: ",i," ",j)

#Verifica se posição do tabuleiro esta ocupada
def verificaPosicaoVazia(tabuleiro, i, j):
    if(tabuleiro[i][j] != vazia):
        print("Indice invalido! Posição ja ocupada.")
        acoes(tabuleiro)
        return False
    return True

#Retorna o tabuleiro que resulta ao fazer a jogada i,j
def resultado(tabuleiro, i, j, njogador):
    tabuleiro[i][j] = labelJogador(njogador)
    imprimirTabuleiro(tabuleiro)

#verifica se ainda possui posicao vazia no tabuleiro
def aindaPossuiPosicaoVazia(tabuleiro):
    for i in range(3):
        for j in range(3):
            if(tabuleiro[i][j] == vazia):          
                return True
    return False

#verifica quem ganhou, se deu empate ou o ainda possui posicão vazia
def quemGanhou(tabuleiro):
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

#Retorna Verdadeiro se o jogo acabou, Falso caso contrário
def final(tabuleiro):
    if(not aindaPossuiPosicaoVazia(tabuleiro) and (quemGanhou(tabuleiro) != "x" or quemGanhou(tabuleiro) != "o")):
        return False
    return True

