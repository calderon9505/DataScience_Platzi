# pesos = float(input("Ingrese pesos colombianos: "))
# print("Tienes $" + str(round(pesos/3875 , 2)) + " dolares")
# print("Tienes $", round(pesos/3875 , 2), " dolares")

# if pesos > 1000:
#     pass
# else:
#     pass

# >>> type(True)    <class 'bool'>
# >>> type("hola")  <class 'str'>
# >>> type(3.2)     <class 'float'>
# >>> type((5,2))   <class 'tuple'>
# >>> type([5,2])   <class 'list'>

# >>> 9//2          4 Cociente
# >>> 9**2          81 Potencia

# '''texto(string) en
# varias lineas'''

# def funcion_prueba(x):
#     print(f"funcion de prueba {x}")
# funcion_prueba("texto 1")
# funcion_prueba(2948)

nombre = " sebastiam " #espacios basura
nombre = nombre.strip().capitalize().replace("m","n") #orden correcto
# upper()            convertir a mayusculas
# strip()            elimina espacios iniciales y finales
print(nombre + "\t" + str(len(nombre)))
print(nombre[::-1])

