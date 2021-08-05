#try, except, raise and finally 

def palindromo(palabra):
    try:
        if len(palabra) == 0: raise ValueError('No empty string')
        palabra = palabra.replace(" ","").lower()
        return palabra == palabra[::-1]
    except ValueError as ve:
        print(ve)
        return False
    finally:
        print('finally')
        #se suele usar para cerrar archivos, cerrar conexiones
        #o liberar recursos externos


def run2():
    palabra = input("Escribe una frase o palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo:
        print("Es palindromo")
    else:
        print("No es palindromo")


def divisors(num):
   try:
      if num < 1: raise ValueError("Only natural numbers")
      return [i for i in range (1, num+1) if num%i == 0]
   except ValueError as ve:
      return ve


def run():
   try:
      num = int(input("Ingrese un numero: "))
      print(divisors(num))
   except ValueError:
      print("Debes ingresar un número")

if __name__ == "__main__":
    run()