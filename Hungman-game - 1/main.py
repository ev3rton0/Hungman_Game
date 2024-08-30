import random
from bonecos import mostrar_boneco

def print_jogo():
    return """
  _    _ _    _ _   _  _____ __  __          _   _         _____          __  __ ______ 
 | |  | | |  | | \ | |/ ____|  \/  |   /\   | \ | |       / ____|   /\   |  \/  |  ____|
 | |__| | |  | |  \| | |  __| \  / |  /  \  |  \| | ____ | |  __   /  \  | \  / | |__   
 |  __  | |  | | . ` | | |_ | |\/| | / /\ \ | . ` | ____ | | |_ | / /\ \ | |\/| |  __|  
 | |  | | |__| | |\  | |__| | |  | |/ ____ \| |\  |      | |__| |/ ____ \| |  | | |____ 
 |_|  |_|\____/|_| \_|\_____|_|  |_/_/    \_\_| \_|       \_____/_/    \_\_|  |_|______|
                                                                                        
                                                                                        """

def main():
    print(print_jogo())

    palavras_forca = ['Banana','Melancia','Azeitona','Tomate','Laranja','Limao','Abacaxi']
    palavra_selecionada = random.choice(palavras_forca)
    palavra_selecionada = palavra_selecionada.lower()

    # Listas para armazenar as letras corretas, erradas, e o progresso da palavra
    letras_certas = []
    letras_erradas = []
    letras_exibidas = ['_' for _ in palavra_selecionada]
    print('->','_ ' * len(palavra_selecionada))
    print(" ")

    vidas = 6  # Definindo o número de vidas

    # Loop principal do jogo
    while vidas > 0:
        tentativa = input("\nDigite o chute: ").lower().strip()

        # Verifica se a letra já foi tentada
        if tentativa in letras_certas or tentativa in letras_erradas:
            print("Você já tentou essa letra, tente outra.\n")
            continue

        if tentativa in palavra_selecionada:
            letras_certas.append(tentativa)
            for indice, letra in enumerate(palavra_selecionada):
                if letra == tentativa:
                    letras_exibidas[indice] = tentativa
            print(f"Acertou! A letra '{tentativa}' está na palavra.\n")
        else:
            letras_erradas.append(tentativa)
            vidas -= 1
            print(f"Errou! Você tem {vidas} vidas restantes.\n")
            mostrar_boneco(vidas)  # Chama a função para mostrar o boneco

        # Exibe o progresso da palavra
        print(' '.join(letras_exibidas))
        print('Letras erradas -> ',' '.join(letras_erradas))

        # Verifica se o jogador acertou todas as letras
        if '_' not in letras_exibidas:
            print("\n========================================")
            print("     ___________  ")
            print("   '._==_==_=_.' ")
            print("   .-\\:      /-. ")
            print("  | (|:.     |) |")
            print("   '-|:.     |-' ")
            print("     \\::.    /   ")
            print("      '::. .'    ")
            print("        ) (      ")
            print("      _.' '._    ")
            print("     `\"\"\"\"\"`")
            print("Parabéns! Você acertou a palavra!")
            break
    else:
        print("\n=================================\n")
        mostrar_boneco(0)  # Mostra o boneco completo quando as vidas chegam a 0
        print(f'Você foi ENFORCADO! A palavra era: -> {palavra_selecionada} <-')

if __name__ == "__main__":
    main()