# https://realpython.com/python-type-checking/
# https://sinclert.github.io/python-types/

# Unlike how types work in most other statically typed languages,
# type hints by themselves don’t cause Python to enforce types.
# As the name says, type hints just suggest types.

# Característica de Python 3.6
# A esto se le llama Annotations

# ----------------------------------------------------------------

myvar_entero: int = 5
myvar_cadena: str = 'Hola'
myvar_bool: bool = True

# La funcion "suma" recibe dos enteros y retorna un entero.
def suma(a: int, b: int) -> int:
    return a+b

print(suma(4,3))

# ----------------------------------------------------------------

# Estructuras de datos en lugar de datos primitivos.
# Se usa el módulo "typing" para definir tipos de datos complejos
# en lugar de variables simples.

# A partir de Python 3.9 se puede hacer con las
# palabras claves de ese tipo ¿cómo?
# Para Python entre 3.6 y 3.9 se hace así:

from typing import Dict, Tuple, List

myList: List[int] = [1,2,3,4,5]

myTuple: Tuple[int, float, int] = (1, 0.5, 99)

myDict: Dict[str, int] = {
	"argentina": 1,
	"mexico": 34,
	"colombia": 45,
}

# Diccionarios dentro de una lista
countries: List[Dict[str, str]] = [
	{
		"name" : "Argentina",
		"people" : "45000",
	},
	{
		"name" : "México",
		"people" : "9000000",
	},
	{
		"name" : "Colombia",
		"people" : "99999999999",
	}
]

# Combinación compleja de estructuras
CoordinatesType = List[Dict[str, Tuple[int, int]]]
# CoordinatesType es un alias
coordinates: CoordinatesType = [
	{
		"coord1": (1,2),
		"coord2": (3,5)
	},
	{
		"coord1": (0,1),
		"coord2": (2,5)
	}
]

# ----------------------------------------------------------------

# El módulo "mypy" es el que permite trabajar con tipado estático.
# $ mypy program.py
# This command makes mypy type check your program.py file and 
# print out any errors it finds. Mypy will type check your code 
# statically: this means that it will check for errors without 
# ever running your code, just like a linter.


# Con Optional[], se puede retornar alguna tipo de variable
# específico o None.

