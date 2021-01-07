import random

def jogar():
    print('*'*34 )
    print('Bem Vindo ao Jogo da Adivinhação!')
    print('*'*34)

    # Definir um número aleatoriamente
    numero_secreto = random.randrange(1,101)

    # Saber o numero de tentativas
    total_de_tentativas = 0
    pontos = 1000

    print('Qual nível de dificuldade')
    print('(1) Fácil (2) Médio (3) Difícil')

    # Definir a dificuldade usando condição if/elif/else
    nivel = int(input('Defina o nível: '))
    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    # Laço para imprimir quantas tentativas precisou para acertar
    for rodada in range(1, total_de_tentativas+1):
        print(f'Tentativa {rodada} de {total_de_tentativas}')

        chute_str = input('Digite um número entre 1 e 100: ')
        # Transformar uma string em um inteiro
        chute = int(chute_str)

        # Se digitar um número fora de 1 e 100
        if(chute < 1 or chute > 100):
            print('Você deve digitar um número entre 1 e 100!')
            # Usar o continue para voltar ao começo do laço for, assim sem quebrar o laço
            continue
        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print('Você acertou e fez {} pontos!'.format(pontos))
            # Break para quebrar o laço e finalizar
            break
        # Calcular a perda de pontos a cada tentativa errada
        else:
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            if(maior):
                print('O seu chute foi maior que o número secreto!')
                if(rodada == total_de_tentativas):
                    print('O número secreto era {}. Você fez {}.'.format(numero_secreto, pontos))
                elif(menor):
                    print('O seu chute foi menor que o número secreto!')
                    if(rodada == total_de_tentativas):
                        print('O número secreto era {}. Você fez {}.'.format(numero_secreto, pontos))
    print('____FIM DE JOGO____')
if(__name__ == '__main__'):
    jogar()