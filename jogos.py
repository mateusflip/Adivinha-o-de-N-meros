import forca
import adivinhacao
def escolhe_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")


    print("(1) Forca (2) Adivinhação")
    jogo = int(input("Qual Jogos Deseja Jogar?"))



    if(jogo == 1):
        print("Jogo da Forca")
        forca.jogar()
    else:
        print("Jogo da Adivinhação")
        adivinhacao.jogar()
if(__name__ == "__main__"): #Fazendo o código rodar tanto individualmente quanto por esse menu que criamos#
    escolhe_jogo()