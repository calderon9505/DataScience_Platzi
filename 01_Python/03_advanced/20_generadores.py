# Un generador es Sugar Sintax para los iteradores.
# Un generador es una función que guarda un estado.

# Generator expression
# No puedo trabajar con listas si tengo demasiados datos
# porque ocuparian demasiado espacio en memoria

my_list = [0,1,4,7,9,10]                # lista clásica
my_second_list = [x*2 for x in my_list] # List comprehension
my_second_gen = (x*2 for x in my_list)  # Generator expression

# ------------------------------------------------------------------------
# Mejorando el iterador de la sucesion de Fibonacci

import time

def fiboGen(max_num: int = None, max_element: int = None) -> int:
    """
    max_num: maximum value in the sequence.
    max_element: maximum number of elements in the sequence.

    """

    a, b, counter = 0, 1, 0
    while (not max_num or a < max_num) and (not max_element or counter < max_element):
        yield a
        a, b = b, a+b
        counter += 1

if __name__ == '__main__':
    # Se instancia la función (como si fuera una clase)
    fibonacci = fiboGen(max_num=10)
    for element in fibonacci:
        print(element)
        time.sleep(.1)
    fibonacci = fiboGen(max_element=10)
    for element in fibonacci:
        print(element)
        time.sleep(.1)
    fibonacci = fiboGen(max_element=10, max_num=10)
    for element in fibonacci:
        print(element)
        time.sleep(.1)