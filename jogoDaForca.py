# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

    # Método Construtor
    def __init__(self, word):
        self.word = word
        self.letras_certas = []
        self.letras_erradas = []
        self.word_game = ""
        for i in range(len(self.word)):
            self.word_game += "_ "


    # Método para adivinhar a letra
    def guess(self, letter):

        if self.word.count(letter) == 1:
            index = self.word.index(letter)
            if index > 0:
                self.word_game = self.word_game[:(index * 2)] + letter + self.word_game[(index * 2) + 1:]
            else:
                self.word_game = self.word_game[:index] + letter + self.word_game[index + 1:]

            self.letras_certas.append(letter)

        elif self.word.count(letter) > 1:

            for i in range(len(self.word)):
                if letter == self.word[i]:
                    if self.word.index(self.word[i]) > 0:
                        self.word_game = self.word_game[:(i * 2)] + letter + self.word_game[(i * 2) + 1:]
                    else:
                        self.word_game = self.word_game[:i] + letter + self.word_game[i + 1:]

                self.letras_certas.append(letter)
        else:
            self.letras_erradas.append(letter)

    # Método para verificar se o jogo terminou
    def hangman_over(self):
        return len(board) == len(self.letras_erradas)

    # Método para verificar se o jogador venceu
    def hangman_won(self):
        return self.word_game.count("_") == 0

    # Método para não mostrar a letra no board
    def hide_word(self):
        print("Nada")

    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        if not self.hangman_won() and not self.hangman_over():
            print(board[len(self.letras_erradas)])
            print("Palavra: %s" %self.word_game)
            print("Letras certas: " + ", ".join(self.letras_certas))
            print("Letras erradas: " + ", ".join(self.letras_erradas))
            return True
        else:
            return False



# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    with open("palavras.txt", "r") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()


# Função Main - Execução do Programa
def main():
    # Objeto
    game = Hangman(rand_word())

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    # Verifica o status do jogo
    while game.print_game_status():

        print("Informe um letra: ")
        game.guess(input())




    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won():
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.word)

    print('\nFoi bom jogar com você! Agora vá estudar!\n')


# Executa o programa
if __name__ == "__main__":
    main()
