# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import random

AHORCADO = ['''
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


lista = ['mesa', 'silla', 'hielo', 'futbol', 'pan']


def print_hangman():
    pass

def findrandomword():
    secret_word = random.choice(lista)
    #print(secret_word)
    return secret_word



def find_character(caracter, secretword, currentword):

    if caracter in secretword:
        if caracter in letras_correcta:
            print(f'La letra {caracter} ya la has dicho')
        else:
            letras_correcta.append(caracter)
            for i in range(len(secretword)):
                if secretword[i] == caracter:
                    currentword = currentword[:i] + secretword[i] + currentword[i+1:]
    else:
        if caracter in letras_incorrectas:
            print(f'La letra {caracter} ya la has dicho')
            pass
        else:
            letras_incorrectas.append(caracter)
    return currentword


if __name__ == '__main__':

    play = 'y'
    name = input('Enter your name: ')
    while play == 'y':


        letras_correcta = []
        letras_incorrectas = []
        secret_word = findrandomword()

        print(f'Hello {name}, this is the word you need to guess')
        intento = '_'*len(secret_word)
        print(intento)
        print(AHORCADO[0])

        while not (len(letras_incorrectas) < 6) or ('_' in intento):

            character = input('choose a letter: ').lower()

            intento = find_character(character, secret_word, intento)
            print(intento)
            print(AHORCADO[len(letras_incorrectas)])

            if len(letras_incorrectas) == 6:
                print('Game over!')
                print(AHORCADO[6])
                break
        else:
            print('Congratulations word found!')

        play = input('Quieres jugar otra vez?(y/n): ')
