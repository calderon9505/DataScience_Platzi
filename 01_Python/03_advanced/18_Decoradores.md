# Decoradores

Los decoradores son una forma sencilla de llamar **funciones de orden mayor**, es decir, funciones que toman otra función como parámetro y/o retornan otra función como resultado. 

Un decorador básicamente toma una función, le añade alguna funcionalidad y la retorna.
De esta forma un decorador añade capacidades a una función sin modificarla.

**En general**, un decorador es un patrón de software que se utiliza para alterar el funcionamiento de una determinada pieza de código; ya sea una función, o una clase, sin la necesidad de emplear otros mecanismos como la herencia. Un decorador es como un envoltorio con el cual envolvemos una función o una clase.

[Decoradores en Python. codigofacilito](https://www.youtube.com/watch?v=DlGPvq9r6Q4&ab_channel=codigofacilito)

```py
def mayus(func):
    def wrapper(text):
        return func(text).upper()
    return wrapper

@mayus
def myFunc(name):
    return f'{name}, recibiste un mensaje'

>>> myFunc('sebastian')
'SEBASTIAN, RECIBISTE UN MENSAJE'
```

```py
from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print(f'Pasaron {time_elapsed.total_seconds()} segundos')
    return wrapper

@execution_time
def random_func():
    for _ in range(1, 10_000_000):
        pass

@execution_time
def suma(a,b):
    return a+b

random_func()
suma(3,5)
```

# @property

Hace que un método actúe como atributo.

```py
class Clase:
    def __init__(self, atributo):
        self.__mi_atributo = atributo

    @property
    def mi_atributo(self):
        return self.__mi_atributo
    
    @mi_atributo.setter
    def mi_atributo(self, valor):
        if valor != "":
            self.__mi_atributo = valor
        else:
            print("Error está vacío")
    
    @mi_atributo.deleter
    def mi_atributo(self):
        self.__mi_atributo = valor
        print("Atributo eliminado")


mi_clase = Clase("valor_atributo")
mi_clase.mi_atributo # >>> 'valor_atributo'
mi_clase.mi_atributo = "nuevo_valor"
mi_clase.mi_atributo # >>> 'nuevo_valor'
```

``mi_atributo`` NO es un método, por lo que no puede ser llamado con ``()``.

La utilidad de esto tiene que ver con el *encapsulamiento*. Sirve para ocultar el estado interno de los objetos al exterior, para evitar que sean modificados de manera incorrecta. Entonces, ahora llamamos a `mi_clase.mi_atributo` para consultarlo, asignarle un nuevo valor o borrarlo como si de un atributo común se tratara, pero por detrás son métodos que están realizando una serie de comprobaciones.

Al definir la propiedad con ``@property`` el acceso a ese atributo se realiza a través de una función que podría contener código extra, siendo por lo tanto un acceso controlado. El primer método luego de `@property` lo toma automáticamente como getter.

El `setter` es otro decorador que permite definir un método para modificar el atributo.

Resulta lógico pensar que si un determinado atributo pertenece a una clase, si queremos modificarlo debería de tener la “aprobación” de la clase, para asegurarse que ninguna entidad externa está “haciendo cosas raras”.



# @classmethod

Decorador para crear **métodos de clase**. Se puede llamar este método directamente desde la clase sin necesidad de instanciarlo en un objeto.

En lugar de `self` se usa `cls` para referirse a la propia clase no instanciada. 

Pueden acceder a la clase pero NO a la instancia.


# @staticmethod

Decorador para crear **métodos estático**. Se puede llamar este método directamente desde la clase sin necesidad de instanciarlo en un objeto.

No requiere el uso `self` ni de  `cls`.

Se podría hacer los mismo con un método de instancia, pero un método estático resulta util para indicar que no se modificará el estado de la instancia ni de la clase y así evitar malentendidos.