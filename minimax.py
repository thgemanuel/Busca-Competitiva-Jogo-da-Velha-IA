from busca_competitiva import custo
from estrutura_jogo import acoes, aindaPossuiPosicaoVazia, labelJogador, quemGanhou, vazia

#Retorna o movimento da IA
def movimentoIA(tabuleiro, jogador):
    posicoes = acoes(tabuleiro)
    melhor_valor = None
    melhormovimento = None
    for posicao in posicoes:
        tabuleiro[posicao[0]][posicao[1]] = labelJogador(jogador)
        valor = minimax(tabuleiro,jogador)
        tabuleiro[posicao[0]][posicao[1]] = vazia
        if(melhor_valor == None):
            melhor_valor = valor
            melhormovimento = posicao
        elif(jogador == 0):
            if(valor > melhor_valor):
                melhor_valor = valor
                melhormovimento = posicao
        elif(jogador == 1):
            if(valor < melhor_valor):
                melhor_valor = valor
                melhormovimento = posicao

    return melhormovimento[0], melhormovimento[1]


#Retorna a jogada ótima para o jogador atual
def minimax(tabuleiro, jogador):
    jganhador = custo(quemGanhou(tabuleiro))
    if(jganhador == 0):
        if(not aindaPossuiPosicaoVazia(tabuleiro)):
            return "O jogo empatou!"
    elif(jganhador == 1 or jganhador == -1):
        return quemGanhou(tabuleiro)

    jogador = (jogador + 1)%2

    posicoes = acoes(tabuleiro)
    melhor_valor = None

    for posicao in posicoes:
        tabuleiro[posicao[0]][posicao[1]] = labelJogador(jogador)
        valor = minimax(tabuleiro,jogador)
        tabuleiro[posicao[0]][posicao[1]] = vazia
        if(melhor_valor == None):
            melhor_valor = valor
        elif(jogador == 0):
            if(valor > melhor_valor):
                melhor_valor = valor
        elif(jogador == 1):
            if(valor < melhor_valor):
                melhor_valor = valor

    return melhor_valor

