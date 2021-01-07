def jogar():
    print('*'*34 )
    print('Bem Vindo ao Jogo da Forca!')
    print('*'*34)

    palavra_secreta = 'banana'
    letras_acertadas = ['_', '_', '_', '_', '_', '_']

    enforcou = False
    acertou = False

    # Para o jogador saber quantas letras compõem a palavra_secreta
    print(letras_acertadas)

    # Enquanto True
    while(not enforcou and not acertou):
        chute = input('Digite uma letra: ')
        chute = chute.strip()

        # Para saber a posição da letra na palavra_secreta
        index = 0
        # Um laço for para percorrer todas as letras da palavra_secreta inclusive letras que se repetem e colocar a letra na posição pertencente
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
            index = index + 1
        print(letras_acertadas)
        
        print('jogando...')
    
    print('Fim de jogo!')
  
if(__name__ == '__main__'):
    jogar()

