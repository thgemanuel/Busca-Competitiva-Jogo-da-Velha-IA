#  Exercício 2: Busca Competitiva  (Jogo da Velha) 
# Aluno: Thiago Emanuel
from estrutura_jogo import acoes, labelJogador, ganhador, vazia

#Retorna 1 se X ganhou, -1 se 0 ganhou, 0 caso contrário.
def custo(resultadofinal):
    if resultadofinal == "x":
        return 1
    elif resultadofinal == "o":
        return -1
    return 0

#Retorna o movimento da IA
def movimentoIA(tabuleiro, jogador):
    posicoes = acoes(tabuleiro)
    melhor_valor = None
    melhormovimento = None
    for posicao in posicoes:
        tabuleiro[posicao[0]][posicao[1]] = labelJogador(jogador)
        valor = minimax(tabuleiro,jogador)
        tabuleiro[posicao[0]][posicao[1]] = vazia
        if melhor_valor is None :
            melhor_valor = valor
            melhormovimento = posicao
        elif jogador == 0 :
            if valor > melhor_valor:
                melhor_valor = valor
                melhormovimento = posicao
        elif jogador == 1 :
            if valor < melhor_valor:
                melhor_valor = valor
                melhormovimento = posicao
    
    return melhormovimento[0], melhormovimento[1]


#Retorna a jogada ótima para o jogador atual
def minimax(tabuleiro, jogador):
    jganhador = ganhador(tabuleiro)
    if jganhador:
        return custo(jganhador)
    
    jogador = (jogador + 1)%2

    posicoes = acoes(tabuleiro)
    melhor_valor = None

    for posicao in posicoes:
        tabuleiro[posicao[0]][posicao[1]] = labelJogador(jogador)
        valor = minimax(tabuleiro,jogador)
        tabuleiro[posicao[0]][posicao[1]] = vazia
        if melhor_valor is None:
            melhor_valor = valor
        elif jogador == 0 :
            if valor > melhor_valor:
                melhor_valor = valor
        elif jogador == 1:
            if valor < melhor_valor:
                melhor_valor = valor
        #print("aquixxxxxxxxx--- minimax ----xxxxxxxxxx")

    return melhor_valor

