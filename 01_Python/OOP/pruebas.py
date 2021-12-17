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

##############################################

class Clase:
    atr_cla_pub = "Hola"
    __atr_cla_pri = "Hola"
    
    def metodo_publico(self):
        print("Metodo publico ejecutado")
        self.atr_ins_pub_met_pub = 333
        self.__atr_ins_pri_met_pub = 444

    def __metodo_privado(self):
        print("Metodo privado ejecutado")
        self.atr_ins_pub_met_pri = 111
        self.__atr_ins_pri_met_pri = 222

    def acceso_metodo_privado(self):
        self.__metodo_privado()

mi_clase = Clase()
print(mi_clase.atr_cla_pub)
# print(mi_clase.__atr_cla_pri) # Error!

mi_clase.metodo_publico()
# mi_clase.__metodo_privado() # Error!
mi_clase.acceso_metodo_privado()

print(mi_clase.atr_ins_pub_met_pri) # Error!
# print(mi_clase.__atr_ins_pri_met_pri) # Error!
print(mi_clase.atr_ins_pub_met_pub) # Error!
# print(mi_clase.__atr_ins_pri_met_pub) # Error!

print(dir(mi_clase))

mi_clase._Clase__atr_cla_pri
mi_clase._Clase__metodo_privado()