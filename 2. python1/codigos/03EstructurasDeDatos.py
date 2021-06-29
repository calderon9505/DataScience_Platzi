# https://recursospython.com/guias-y-manuales/listas-y-tuplas/

#LISTAS
numeros = [1,5,9]
objetos = ['hola', 4.5, 3, True]
# print(objets[2])

objetos.append(False)
# objetos.pop(0) #elimina por indice
objetos.pop() #elimina elemento final
# del objetos[0] #elimina elemento por indice. del a[:]
# print(objetos)
objetos.insert(1, 2) # insert(index, element)

#ordenar menor mayor
objetos.pop()
objetos.pop(0)
objetos.sort
# print(objetos)

# remover por valor
objetos.remove(3)
# print(objetos)


#TUPLAS
mi_tupla = (1, 2, 3, 4, 'hola')
# print(mi_tupla)
#las tuplas son objetos estaticos 
# (No se puede usar append)
#las listas son dinamicas
#las tuplas son más eficientes
# las tuplas son inmutables
# se accede por indice mi_tupla[2]
b = (5,)  # Es una tupla de un elemento
c = (5) # es un entero

# a = tuple(b)
# b = list(a)

