# https://recursospython.com/guias-y-manuales/listas-y-tuplas/

#LISTAS                             #las listas son dinamicas
numeros = [1,5,9]                   
objetos = ['hola', 4.5, 3, True]    #objetos[2] acceder a elementos de lista

# objetos.append(False)               #añade elemento al final
# objetos.pop()                       #elimina elemento final
# objetos.pop(0)                      #elimina por indice
# del objetos[1]                      #elimina elemento por indice. del a[:]
# objetos.insert(1, 2)                #insert(index, element)
# objetos.sort                        #ordenar de menor a mayor
# objetos.remove(3)                   #remover por valor
# print(objetos)


#TUPLAS                             # las tuplas son estaticas (No se puede usar append)
mi_tupla = (1, 2, 3, 4, 'hola')     # se accede por indice mi_tupla[2]
b = (5,)                            # Es una tupla de un elemento
c = (5)                             # es un entero
                                    # las tuplas son más eficientes
                                    # las tuplas son inmutables
# print(mi_tupla)

# a = tuple(b)
# b = list(a)

