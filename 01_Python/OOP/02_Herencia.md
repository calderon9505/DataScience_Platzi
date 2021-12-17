# Herencia

Proceso mediante el cual se puede crear una clase hija que hereda de una clase padre, compartiendo sus métodos y atributos. Además de ello, una clase hija puede sobreescribir los métodos o atributos, o incluso definir unos nuevos.

```python
# Clase padre
class Animal:
    pass

# Clase hija
class Perro(Animal):
    pass
```

Para ver de quien hereda: ``Perro.__bases__``

Para ver quienes heredan : ``Animal.__subclasses__()``

## Ejemplo de uso

```py
class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad

    def hablar(self):
        pass

    def moverse(self):
        pass

    def describeme(self):
        print("Soy un Animal del tipo", type(self).__name__)
```

```py
class Perro(Animal):
    def __init__(self, especie, edad, dueño):
        super().__init__(especie, edad)
        self.dueño = dueño
    def hablar(self):
        print("Guau!")
    def moverse(self):
        print("Caminando con 4 patas")

class Vaca(Animal):
    def hablar(self):
        print("Muuu!")
    def moverse(self):
        print("Caminando con 4 patas")

class Abeja(Animal):
    def hablar(self):
        print("Bzzzz!")
    def moverse(self):
        print("Volando")

    # Nuevo método
    def picar(self):
        print("Picar!")
```

```py
mi_perro = Perro('mamífero', 7, 10)
mi_vaca = Vaca('mamífero', 23)
mi_abeja = Abeja('insecto', 1)

mi_perro.describeme()
print(mi_perro.especie)
print(mi_perro.edad)
print(mi_perro.dueño)
```

La función ``super()`` permite acceder a los métodos de la clase padre desde una de las clases hijas.

Se puede heredar de múltiples clases y se puede heredar de una clase que ya heredaba de otra clase superior.

Si llamo a un *método* que tienen en común la clase hija y las clases padres, se busca primero el *método* en la propia clase y se va subiendo (o de izquierda a derecha en la herencia múltiple) hasta la clase padre que contenga el método. ``Clase.__mro__`` para consultar el orden de búsque de los métodos.

> todas las clases en Python heredan de una clase genérica **object**, aunque no lo especifiquemos explícitamente.