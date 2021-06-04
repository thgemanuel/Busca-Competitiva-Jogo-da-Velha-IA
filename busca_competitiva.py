#  Exercício 2: Busca Competitiva  (Jogo da Velha) 
# Aluno: Thiago Emanuel
from estrutura_jogo import final,vazia,imprimirTabuleiro, initTabuleiro, leEntrada, quemGanhou, resultado, verificaPosicaoVazia

jogador = 0
tabuleiro = initTabuleiro()
jganhador = quemGanhou(tabuleiro)

#funcao iniciar jogo
def iniciaJogo(jogador,tabuleiro):
    imprimirTabuleiro(tabuleiro)
    print("----==----")
    while(final(tabuleiro)):
        if(jogador == 0):
            i = leEntrada("Informe o valor da linha: ")
            j = leEntrada("Informe o valor da coluna: ")
        else:
            i = leEntrada("Informe o valor da linha: ")
            j = leEntrada("Informe o valor da coluna: ")
        if(verificaPosicaoVazia(tabuleiro,i,j)):
            resultado(tabuleiro,i,j,jogador)
            print("----==----")
            jogador = (jogador+1)%2

    return quemGanhou(tabuleiro)

#Retorna 1 se X ganhou, -1 se 0 ganhou, 0 caso contrário.
def custo(resultadofinal):
    if(resultadofinal == "x"):
        return 1
    elif(resultadofinal == "o"):
        return -1
    return 0

#Retorna o ganhador, se houver
def ganhador(numerojogador):
    print("xxxxxxxxxxxxxxxxxx")
    if(numerojogador == 1):
        print("O ganhador é o jogador: 1")
    elif(numerojogador == -1):
        print("O ganhador é o jogador: 2")
    else:
        print("O jogo empatou!")
    print("xxxxxxxxxxxxxxxxxx")

ganhador(custo(iniciaJogo(jogador,tabuleiro)))
