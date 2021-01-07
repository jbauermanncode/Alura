#Importar forca e adivinhacao
import forca
import adivinhacao

def escolhe_jogo():
    print('*'*25 )
    print('***Escolha o seu jogo!***')
    print('*'*25)

    print('(1) Forca (2) Adivinhação')

    jogo = int(input('Digite 1 ou 2 para escolher um jogo: '))

    if(jogo == 1):
        print('Jogo da Forca')
        #função jogar de adivinhação
        forca.jogar()
    elif(jogo == 2):
        print('Jogo de Adivinhação')
        adivinhacao.jogar()

# Para saber se o arquivo é o principal ou não
if(__name__=='__main__'):
    escolhe_jogo()




