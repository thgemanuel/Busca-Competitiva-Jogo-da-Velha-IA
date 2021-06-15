#  Exercício 2: Busca Competitiva  (Jogo da Velha) 
# Aluno: Thiago Emanuel
from minimax import movimentoIA, custo
from estrutura_jogo import final,imprimirTabuleiro, initTabuleiro, leEntrada, ganhador, resultado, verificaPosicaoVazia

jogador = 0
tabuleiro = initTabuleiro()
jganhador = ganhador(tabuleiro)

#funcao iniciar jogo
def iniciaJogo(jogador,tabuleiro):
    imprimirTabuleiro(tabuleiro)
    print("----==----")
    try:
        while final(tabuleiro):
            if jogador == 0:
                i,j = movimentoIA(tabuleiro, jogador)
                #i = leEntrada("Informe o valor da linha: ")
                #j = leEntrada("Informe o valor da coluna: ")
            else:
                i = leEntrada("Informe o valor da linha: ")
                j = leEntrada("Informe o valor da coluna: ")
            if verificaPosicaoVazia(tabuleiro,i,j):
                resultado(tabuleiro,i,j,jogador)
                print("----==----")
                jogador = (jogador+1)%2

        return ganhador(tabuleiro)
    except KeyboardInterrupt:
        print("O jogo foi finalizado! Obrigado!")

#Imprime o resultado final
def resultadoFinal(numerojogador):
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    if numerojogador == 1:
        print("O ganhador é o jogador: 1")
    elif numerojogador == -1:
        print("O ganhador é o jogador: 2")
    else:
        print("O jogo empatou!")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

resultadoFinal(custo(iniciaJogo(jogador,tabuleiro)))
