total_tentativas = 3
rodada = 1

while(rodada <= total_tentativas):
  numero_adivinhacao = 34

  print("Essa é a sua tentativa {} de {}".format(rodada, total_tentativas))

  numero_str = input("Digite um número para acertar ")
  numero = int(numero_str)

  print("Seu número é ", numero)

  acertou = (numero == numero_adivinhacao)
  menor = (numero < numero_adivinhacao)
  maior = (numero > numero_adivinhacao)

  if (acertou):
    print("Você acertou")
  else:
      if(menor):
        print("Você errou, o número é maior")
      elif(maior):
        print("Você errou, o número é menor")

  rodada = rodada + 1