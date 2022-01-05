# Sets
# Colección desordenada de elementos únicos e inmutables

my_set = {'Hola', 0, 1, True, False, 2, 3, 3} # True = 1 y False = 0
print('my_set:', my_set)

# Set vacio vs Diccionario vacio
empty_dict = {}
empty_set = set()

# Añadir elementos al set
empty_set.add('sebastian')
empty_set.update('Hola')    # char by char
empty_set.update(['Hola'])  # whole string
empty_set.update([1,2,3], (3,4,5), {5,6,7})
print(empty_set)

# Remover elementos del set
empty_set.discard(1)
empty_set.remove(2)
# remove genera error al intentar borrar
# un elemento inexistente. discard no.
empty_set.pop()
# pop borra elemento aleatorio
empty_set.clear()
# clear borrar todos los elementos del set.

# Operaciones entre conjuntos
my_set_1 = {1,2,3}
my_set_2 = {3,4,5}
print(my_set_1 | my_set_2)  # union "my_set_1.union(my_set_2)"
print(my_set_1 & my_set_2)  # intersection "my_set_1.intersection(my_set_2)"
print(my_set_1 - my_set_2)  # diferencia "my_set_1.difference(my_set_2)"
print(my_set_1 ^ my_set_2)  # diferencia simétrica "my_set_1.symmetric_difference(my_set_2)"