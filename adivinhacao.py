total_tentativas = 3
import random
numero_adivinhacao = random.randrange(1, 101) #Gera um número aleatório de 1 a 100, lembrando que ele exclui o ultimo parametro que é o 101#
print("o número da adivinhação é ", numero_adivinhacao)

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
    print("Você acertou")
    break
  else:
      if(menor):
        print("Você errou, o número é maior")
      elif(maior):
        print("Você errou, o número é menor")

