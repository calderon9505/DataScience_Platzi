# Polimorfismo

Los objetos puden tomar diferentes formas. Esto quiere decir que objetos de diferentes clases pueden ser accedidos utilizando la misma interfaz, mostrando un comportamiento distinto (tomando diferentes formas) según cómo sean accedidos.

```py
class Animal:
    def hablar(self):
        pass

class Perro(Animal):
    def hablar(self):
        print("Guau!")

class Gato(Animal):
    def hablar(self):
        print("Miau!")
```

En lenguajes como Java (con tipado estático), el polimorfismo hace referencia a que puedo definir un objeto tipo `Animal` y asignarle un objeto tipo `perro` o `gato`. Pero en Java se requiere que haya **herencia** para que funcione el polimorfismo (es decir, que compartan la interfaz).

```py
for mascota in Perro(), Gato():
    mascota.hablar()
```

Python es un lenguaje con **tipado dinámico** que permite el **duck typing**, por lo que no es necesario que los objetos compartan un interfaz, simplemente basta con que tengan los métodos que se quieren llamar. De hecho, la clase `Animal` nisiquieras es usada en este caso.

> If it walks like a duck and it quacks like a duck, then it must be a duck