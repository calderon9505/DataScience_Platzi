# Interfaces

Conjunto de métodos que tiene que tener un objeto para que pueda cumplir una determinada función. Es decir, define cómo es un objeto y lo que se puede hacer con él.

> Las interfaces no poseen código asociado, pues se centra en el **qué** y no el **cómo**.

Una clase implementa una interfaz cuando añade código a los métodos que no lo tenían (métodos abstractos).

> Implementar un interfaz consiste en pasar del **qué** se hace al **cómo** se hace.

## Interfaces informales

Son simples clases que no implementan los métodos.

```py
class Mando:
    def subir_volumen(self):
        pass
    def bajar_volumen(self):
        pass
```

Mediante herencia se implementa la interfaz.

```py
class MandoSamsung(Mando):
    def subir_volumen(self):
        print("Samsung->Subir")
    def bajar_volumen(self):
        print("Samsung->Bajar")
```

Las interfaces informales **no obligan** a implementar todos los métodos.


## Interfaces formales

Se definen en Python utilizando el módulo por defecto ABC (Abstract Base Classes). Simplemente definen una forma de crear interfaces (a través de metaclases) en los que se definen unos métodos (pero no se implementan) y donde se fuerza a las clases que usan ese interfaz a implementar los métodos.

```py
from abc import ABC

class Mando(ABC):
	pass
```

El módulo ABC se asocia con las metaclases (Tema para futuro estudio: Sebastian)

```py
from abc import ABCMeta
class Mando(metaclass=ABCMeta):
    pass
```

Usando el decorador ``@abstractmethod`` se forzará a las clases que implementen la interfaz a codificar dicho método.

```py
from abc import abstractmethod
from abc import ABCMeta

class Mando(metaclass=ABCMeta):

    @abstractmethod
    def subir_volumen(self):
        pass

    @abstractmethod
    def bajar_volumen(self):
        pass
```

> no se puede crear un objeto de una clase interfaz ya que sus métodos no están implementados.