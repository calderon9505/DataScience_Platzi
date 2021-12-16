class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad

    # Método genérico pero con implementación particular
    def hablar(self):
        # Método vacío
        pass

    # Método genérico pero con implementación particular
    def moverse(self):
        # Método vacío
        pass

    # Método genérico con la misma implementación
    def describeme(self):
        print("Soy un Animal del tipo", type(self).__name__)

class Perro(Animal):
    def __init__(self, especie, edad, dueño):
        super().__init__(especie, edad)
        self.dueño = dueño
    def hablar(self):
        print("Guau!")
    def moverse(self):
        print("Caminando con 4 patas")
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

mi_perro = Perro('mamífero', 7, 10)
mi_perro.describeme()
print(mi_perro.especie)
print(mi_perro.edad)
print(mi_perro.dueño)