#funciones que reciben como parametros a otras funciones
def saludo(func):
    func()

def hola():
    print("hola")

saludo(hola)

# Filter
#filter retorna un iterador
my_list = [1,4,5,6,9,13,19,21]
#filtrar los elementos impares
odd = [i for i in my_list if i%2]
odd_filter = list(filter(lambda x : x%2 != 0, my_list))
#filter is a high order function
print(odd)
print(odd_filter)

# Map
my_list = [1,2,3,4,5]
#devolver cada elemento al cuadrado
square = [i**2 for i in my_list]
square_map = list(map(lambda x : x**2, my_list))
print(square)
print(square_map)

from functools import reduce
# Reduce
my_list = [2,2,2,2,2]
#reducir los valores de la lista a un unico valor
all_multiplied = reduce(lambda a, b : a*b, my_list)
#"a" es mi variable acumuladora. "b" es el siguiente elemento de la lista
print(all_multiplied)