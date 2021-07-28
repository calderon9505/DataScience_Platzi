#Lambda Functions (no tienen nombre/identificador)
# lambda argumentos : expresion
#en python las funciones anonimas solo pueden tener una linea de codigo
#No requiere de la palabra clave "return"

palindrome = lambda string : string == string[::-1]
#palindrome es el identificador PERO NO es de la funcion, es de una variable que contiene
#un objeto de tipo funcion

print(palindrome('ana'))