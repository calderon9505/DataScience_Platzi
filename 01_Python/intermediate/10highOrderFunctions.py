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
# print(odd)
# print(odd_filter)

# Map
my_list = [1,2,3,4,5]
#devolver cada elemento al cuadrado
square = [i**2 for i in my_list]
square_map = list(map(lambda x : x**2, my_list))
# print(square)
# print(square_map)

from functools import reduce
# Reduce
my_list = [2,2,2,2,2]
#reducir los valores de la lista a un unico valor
all_multiplied = reduce(lambda a, b : a*b, my_list)
#"a" es mi variable acumuladora. "b" es el siguiente elemento de la lista
# print(all_multiplied)


# FILTRANDO DATOS
DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():

    # all_python_devs = [worker['name'] for worker in DATA if worker['language'] =='python']
    all_python_devs = list(filter(lambda worker : worker['language'] == 'python', DATA))
    all_python_devs = list(map(lambda worker : worker['name'], all_python_devs))

    # all_platzi_workers = [worker['name'] for worker in DATA if worker['organization'] == 'Platzi']
    all_platzi_workers = list(filter(lambda worker : worker['organization'] == 'Platzi', DATA))
    all_platzi_workers = list(map(lambda worker : worker['name'], all_platzi_workers))

    # adults = [worker['name'] for worker in DATA if worker['age'] > 18]
    adults = list(filter(lambda worker : worker['age'] > 18, DATA))
    adults = list(map(lambda worker : worker['name'], adults))

    # old_people = [worker | {"old" : worker["age"] > 70} for worker in DATA]
    old_people = list(map(lambda worker : worker | {"old" : worker["age"] > 70}, DATA)) 
    # | pipe. solo en python 3.9. Sumar diccionarios.

 
    for worker in old_people:
        print(worker)


if __name__ == '__main__':
    run()