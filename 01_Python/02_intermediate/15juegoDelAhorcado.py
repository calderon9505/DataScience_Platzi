#https://stackoverflow.com/questions/5893163/what-is-the-purpose-of-the-single-underscore-variable-in-python

# from random import randint
import random
import os
from hangman_ascii import HANGMAN_ASCII

def adjust(word):
    a,b = 'áéíóúüÁÉÍÓÚ','aeiouuAEIOU'
    trans = str.maketrans(a,b)
    return word.translate(trans).upper().strip() #elimina el "\n" al final

def run():

    with open('.\\01_Python\intermediate\data.txt', 'r', encoding='utf-8') as f:
        # randomNumber = randint(0, sum(1 for _ in f))
        words = [line for line in f]
    
    word = [letter for letter in adjust(random.choice(words)) ]
    guess = ["_" for _ in word]

    attempt = 0
    flag = False
    os.system("cls")    # "clear" en unix
    while(word != guess and attempt < len(HANGMAN_ASCII)-1):
        print(HANGMAN_ASCII[attempt])
        print("¡Adivina la palabra!")
        print(''.join(guess))
        letter_guess = adjust(input("Ingresa una letra: "))
        for i, letter in enumerate(word):
            if letter == letter_guess:
                guess[i] = letter_guess
                flag = True
        if flag == False : attempt += 1 
        flag = False
        os.system("cls")

    if (word == guess):
        print("¡Ganaste! La palabra era", ''.join(word))
    else:
        print("¡Perdiste! La palabra era", ''.join(word))
        print(HANGMAN_ASCII[attempt])

if __name__ == "__main__":
    run()