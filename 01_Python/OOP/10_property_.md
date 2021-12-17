# Decorador Property

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
            print("Modificando el valor")
            self.__mi_atributo = valor
        else:
            print("Error está vacío")

mi_clase = Clase("valor_atributo")
mi_clase.mi_atributo # 'valor_atributo'
mi_clase.mi_atributo = "nuevo_valor"
mi_clase.mi_atributo # 'nuevo_valor'
```

``mi_atributo`` NO es un método, por lo que no puede ser llamado con ``()``.

La utilidad de esto tiene que ver con el *encapsulamiento*. Sirve para ocultar el estado interno de los objetos al exterior, para evitar que sean modificados de manera incorrecta.

El uso de ``__`` antes de ``mi_atributo`` hace que Python *oculte* dicho atributo y que no pueda ser accedido como el resto de atributos.

```
mi_clase.__mi_atributo # Error!
```

Al definir la propiedad con ``@property`` el acceso a ese atributo se realiza a través de una función que podría contener código extra, siendo por lo tanto un acceso controlado.

El `setter` es otro decorador que permite definir un método para modificar el atributo.

Resulta lógico pensar que si un determinado atributo pertenece a una clase, si queremos modificarlo debería de tener la “aprobación” de la clase, para asegurarse que ninguna entidad externa está “haciendo cosas raras”.