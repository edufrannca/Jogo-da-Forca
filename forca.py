import random

def desenhar_forca(erros):
    """
    Desenha a forca na tela com base no número de erros.

    Argumentos:
        erros: O número de erros acumulados pelo jogador.
    """
    estagios = [
        """
          _______
         |       |
         |       
         |      
         |     
         |     
         |     
        =========
        """,
        """
          _______
         |       |
         |       O
         |      
         |     
         |     
         |     
        =========
        """,
        """
          _______
         |       |
         |       O
         |       |
         |      
         |     
         |     
        =========
        """,
        """
          _______
         |       |
         |       O
         |      /|
         |      
         |     
         |     
        =========
        """,
        """
          _______
         |       |
         |       O
         |      /|\\
         |      
         |     
         |     
        =========
        """,
        """
          _______
         |       |
         |       O
         |      /|\\
         |      / 
         |     
         |     
        =========
        """,
        """
          _______
         |       |
         |       O
         |      /|\\
         |      / \\
         |     
         |     
        =========
        """
    ]
    print(estagios[erros])

def verificar_letra(palavra, letra, letras_usadas, palavra_revelada):
    """
    Verifica se a letra digitada pelo jogador está na palavra e atualiza o estado do jogo.

    Argumentos:
        palavra: A palavra secreta que o jogador deve adivinhar.
        letra: A letra digitada pelo jogador.
        letras_usadas: Uma lista contendo as letras já utilizadas pelo jogador.
        palavra_revelada: A palavra secreta com as letras reveladas até o momento.

    Retorna:
        True se a letra estiver na palavra, False caso contrário.
    """
    acertou = letra in palavra
    if acertou:
        for i in range(len(palavra)):
            if palavra[i] == letra:
                palavra_revelada[i] = letra
    else:
        letras_usadas.append(letra)
    return acertou

def mostrar_jogo(palavra_revelada, letras_usadas, erros):
    """
    Exibe o estado atual do jogo na tela.

    Argumentos:
        palavra_revelada: A palavra secreta com as letras reveladas até o momento.
        letras_usadas: Uma lista contendo as letras já utilizadas pelo jogador.
        erros: O número de erros acumulados pelo jogador.
    """
    print("Palavra: " + " ".join(palavra_revelada))
    print("Letras usadas: " + ", ".join(letras_usadas))
    desenhar_forca(erros)

def iniciar_jogo():
    """
    Inicializa e executa o jogo da forca.
    """
    # Carregar uma lista de palavras
    with open("palavras.txt", "r") as arquivo:
        palavras = arquivo.readlines()

    # Selecionar uma palavra aleatória
    palavra_secreta = random.choice(palavras).strip().upper()

    # Inicializar variáveis do jogo
    palavra_revelada = ["_" for _ in range(len(palavra_secreta))]
    letras_usadas = []
    erros = 0

    # Loop principal do jogo
    while True:
        mostrar_jogo(palavra_revelada, letras_usadas, erros)

        # Pedir uma letra ao jogador
        letra = input("Digite uma letra: ").upper()

        if letra in letras_usadas:
            print("Você já digitou essa letra!")
            continue

        acertou = verificar_letra(palavra_secreta, letra, letras_usadas, palavra_revelada)

        if acertou:
            # Verificar se a palavra foi completamente revelada
            if "_" not in palavra_revelada:
                mostrar_jogo(palavra_revelada, letras_usadas, erros)
                print("Parabéns, você acertou a palavra!")
                break
        else:
            erros += 1

            # Verificar se o jogador perdeu
            if erros == 6:
                mostrar_jogo(palavra_revelada, letras_usadas, erros)
                print("Você perdeu! A palavra era:", palavra_secreta)
                break

# Iniciar o jogo
iniciar_jogo()
