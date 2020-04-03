import random
def jogar():

        total_tentativas = 0
        pontos = 1000


        numero_adivinhacao = random.randrange(1, 101) #Gera um número aleatório de 1 a 100, lembrando que ele exclui o ultimo parametro que é o 101#
        print("o número da adivinhação é ", numero_adivinhacao)

        #Deficindo a dificuldade que a pessoa quer jogar#
        print("Digite uma Dificuladde: 1- Fácil 2- Médio 3 - Dificíl")
        nivel = int(input("Quero jogar na dificuldade:"))

        if(nivel == 1):
            total_tentativas = 20
        elif(nivel == 2):
                total_tentativas = 10
        elif(nivel == 3):
            total_tentativas = 5

        #Jogo em sí#

        for rodada in range(1, total_tentativas + 1): #o for nao reconhe o ultimo termo, por isso temos que comar mais um#
          print("Essa é a sua tentativa {} de {}".format(rodada, total_tentativas))
          numero = int(input("Digite um número de 1 a 100 "))

          print("Seu número é ", numero)
          if (numero < 1 or numero > 100):
              print("Numero inválido, você deve digitar um número de 1 a 100")
              continue # Encerra a interação do laço indo pro proximo#

          acertou = (numero == numero_adivinhacao)
          menor = (numero < numero_adivinhacao)
          maior = (numero > numero_adivinhacao)

          if (acertou):
            print("Você acertou o numero secreto é {} e a sua pontuacao {} !".format(numero_adivinhacao, pontos))
            break
          else:
              pontos_perdidos = abs(numero_adivinhacao - numero)
              pontos = pontos - pontos_perdidos

              if(menor):
                print("Você errou, o número é maior")
                if(total_tentativas == rodada):
                        print("Você não acertou, o número secreto era {} e a sua pontuação foi de {}".format(numero_adivinhacao, pontos))
              elif(maior):
                print("Você errou, o número é menor")
                if(total_tentativas == rodada):
                      print("Você não acertou, o numero secreto era {} e a sua pontuação foi de {} pontos".format(numero_adivinhacao, pontos))
        print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
