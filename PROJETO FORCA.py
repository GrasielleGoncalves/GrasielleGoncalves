import random

def main():
    palavras = ["python", "programacao", "desenvolvimento", "tecnologia"]
    palavra = random.choice(palavras)
    tentativas = 6
    letras_certas = set()
    letras_erradas = set()

    print("Bem-vindo ao jogo da forca!")
    print("_ " * len(palavra))

    while tentativas > 0:
    
        progresso = [letra if letra in letras_certas else "_" for letra in palavra]
        print("\nPalavra:", " ".join(progresso))
        
        if "_" not in progresso:
            print("\nParabéns! Você acertou a palavra:", palavra)
            break
        
        letra = input("Digite uma letra: ").lower()

        
        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, digite apenas uma letra.")
            continue

        if letra in letras_certas or letra in letras_erradas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        if letra in palavra:
            letras_certas.add(letra)
            print("Boa! A letra está na palavra.")
        else:
            letras_erradas.add(letra)
            tentativas -= 1
            print(f"Errado! Você tem {tentativas} tentativa(s) restante(s).")
            print("Letras erradas até agora:", ", ".join(letras_erradas))
    
    if "_" in progresso:
        print("\nVocê perdeu! A palavra era:", palavra)

if __name__ == "__main__":
    main()
