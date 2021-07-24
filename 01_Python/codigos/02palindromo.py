### Python program to execute
### main directly
# print ("Always executed")
 
# if __name__ == "__main__":
#     print ("Executed when invoked directly")
# else:
#     print ("Executed when imported")
# https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/#:~:text=If%20you%20import%20this%20script,run%20directly%2C%20and%20not%20imported.

def palindromo(palabra):
    palabra = palabra.replace(" ","").lower()

    # if palabra == palabra[::-1]:
    #     return True
    # else:
    #     return False

    # return True if palabra == palabra[::-1] else False

    return palabra == palabra[::-1]


def run():
    palabra = input("Escribe una frase o palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo:
        print("Es palindromo")
    else:
        print("No es palindromo")


if __name__ == "__main__":
    run()

#crear shortcut ctrl+alt+R

# limite = 1000     # El interprete lo toma como variable
# LIMITE = 1000     # El interprete lo toma como constante

print(type(range(4)))
print(range(5))
print(list(range(6)))
for contador in range(1,4):
    print(contador)