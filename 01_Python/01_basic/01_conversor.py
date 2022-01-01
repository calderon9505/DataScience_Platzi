# Pedir datos desde la terminal
# pesos = float(input("Ingrese pesos colombianos: "))

# Dos formas distintas de usar el print
# print("Tienes $" + str(round(pesos/3875 , 2)) + " dolares")
# print("Tienes $", round(pesos/3875 , 2), " dolares")

# 9//2          Cociente
# 9%2           Residuo
# 9**2          Potencia

# def funcion_prueba(x):
#     print(f"funcion de prueba {x}")
# funcion_prueba("texto 1")
# funcion_prueba(2948)

nombre = " sebastiam " # contiene espacios basura
nombre = nombre.strip().capitalize().replace("m","n") #orden correcto
# upper()            convertir a mayusculas
# strip()            elimina espacios iniciales y finales
print(nombre + "\t" + str(len(nombre)))
print(nombre[::-1])

