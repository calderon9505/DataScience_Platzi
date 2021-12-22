# https://recursospython.com/guias-y-manuales/listas-y-tuplas/

#LISTAS                             #Dinamicas, flexibles, side effects
numeros = [1,5,9]                   
objetos = ['hola', 4.5, 3, True]    #objetos[2] acceder a elementos de lista

# objetos.append(False)               #añade elemento al final
# objetos.pop()                       #elimina elemento final
# objetos.pop(0)                      #elimina por indice
# del objetos[1]                      #elimina elemento por indice. del a[:]
# objetos.insert(1, 2)                #insert(index, element)
# objetos.sort                        #ordenar de menor a mayor
# objetos.remove(3)                   #remover por valor

# si defino a = [1,2] y despues digo que b = a
# Tanto "a" como "b" apuntan a la misma direccion de memoria
# id(a) == id(b) >>> True
# a is b >>> True
# "b = list[a]" realiza un clon. Ahora sí son independientes.
# "b = a[:]" tambien es un clon.


#TUPLAS                             # Estáticas, eficientes, inmutables.
mi_tupla = (1, 2, 3, 4, 'hola')     # se accede por indice mi_tupla[2]
b = (5,)                            # Es una tupla de un elemento
c = (5)                             # es un entero

# Puedo reasignar la tupla
# mi_tupla = (1, 2, 3, 4, 'chao')
# No esto alteralo el valor sino que 
# esto hace que apunte a una dirección de memoria diferente


# TRANSFORMACION
# a = tuple(b)
# b = list(a)

