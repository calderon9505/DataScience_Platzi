# Bases de la Programación Orientada a Objetos

## Atributos

* **Atributos de instancia**: Pertenecen a la instancia de la clase o al objeto. Son atributos particulares de cada instancia, en nuestro caso de cada perro.
* **Atributos de clase**: Se trata de atributos que pertenecen a la clase, por lo tanto serán comunes para todos los objetos.

``` python
class Perro:

    especie = 'mamífero'

    def __init__(self, nombre, raza):
        print(f"Creando perro {nombre}, {raza}")

        self.nombre = nombre
        self.raza = raza

    def ladra(self):
        print("Guau")

    def camina(self, pasos):
        print(f"Caminando {pasos} pasos")

mi_perro = Perro("Toby", "Bulldog")
```

La variable *especie* es un **atributo de clase.** Dado que es un atributo de clase, no es necesario crear un objeto para acceder al atributo: ``` Perro.especie```, aunque igual se puede: ``` mi_perro.especie```.

el metodo ```__init__``` es el **Constructor** de la clase.

el ```self``` que se pasa como parámetro de entrada es una variable que representa la instancia de la clase. Deberá estar ahí siempre en cuaquier función que haga referencia a una instancia. Con ellos se definen los **atributos de instancia**


## Metodos

```python
class Clase:
    def metodo(self, arg1, arg2):
        return 'Método normal', self

    @classmethod
    def metodoDeClase(cls):
        return 'Método de clase', cls

    @staticmethod
    def metodoEstatico():
        return "Método estático"
```

> El uso de "self" es totalmente arbitrario. Se trata de una convención acordada por los usuarios de Python, usada para referirse a la instancia que llama al método, pero podría ser cualquier otro nombre. Lo mismo ocurre con "cls"

* **Métodos de instancia**

Reciben como primer parámetro de entrada el ``self`` que hace referencia a la instancia que llama al método.

los métodos de instancia pueden acceder y modificar los atributos del objeto, pueden acceder a otros métodos y, dado que desde el objeto self se puede acceder a la clase con ``self.class``, también pueden modificar el estado de la clase.

* **Métodos de clase**. ``@classmethod``

A diferencia de los métodos de instancia, los métodos de clase reciben como argumento ``cls``, que hace referencia a la clase. Por lo tanto, pueden acceder a la clase pero NO a la instancia.

Se pueden llamar sobre la clase: ``Clase.metodoDeClase()`` o sobre el objeto: ``mi_clase.metodoDeClase()``

los métodos de clase NO pueden acceder a los atributos de la instancia, pero sí pueden modificar los atributos de la clase.

* **Métodos estáticos**. ``@staticmethod``

NO aceptan como parámetro ni la instancia ni la clase, por lo tanto No puede modificar sus estados. Se podría hacer los mismo con un método de instancia, pero un método estático resulta util para indicar que no se modificará el estado de la instancia ni de la clase y así evitar malentendidos.

Se puede acceder a este método desde el objeto y desde la clase.