import random
def main():
    numeroAleatorio = random.randint(0, 100)
    tentativas_maximas = 10
    tentativas = 0
    print("Ola! Adivinhe um numero")
    print("Você tem 10 tentativas")

    while tentativas < tentativas_maximas:

        try:
            palpite = int(input(f"tentativa {tentativas +1}: Digite o seu palpite:"))
   
            if  palpite == numeroAleatorio:
                print("Parabéns! Você acertou")
                break
            elif palpite > numeroAleatorio:
                print("Errado! Tente um numero menor")
            else:
                print("Errado!Tente um numero maior")
            tentativas +=1
        except ValueError:
                print("Entrada Invalida, tente novamente com algum numero inteiro")

    if tentativas == tentativas_maximas:
                print(f"Suas tentativas acabaram. O número era {numeroAleatorio}.")


if __name__ == "__main__":
    main()
