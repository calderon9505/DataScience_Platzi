# Encapsulamiento

Es el ocultamiento de los estados internos de una clase al exterior. Hace que los atributos o métodos internos de una clase no se puedan acceder ni modificar desde fuera, sino que tan solo el propio objeto pueda acceder a ellos.

> Python por defecto no oculta los atributos y métodos de una clase al exterior.

Los atributos y métodos que inician con ``_`` indica que una variable está destinada a uso interno. El interprete de Python no lo aplica como privado, sino que es una **sugerencia** para el programador.

Los atributos y métodos que inician con ``__`` son privados e inaccesibles desde el exterior. Los atributos públicos son accesibles así estén definidos dentro de un método privado.

> Pero... la realidad es que en Python no existen variables netamente privadas, siempre son accesibles de una u otra forma.

```py
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

print(mi_clase.atr_ins_pub_met_pri)
# print(mi_clase.__atr_ins_pri_met_pri) # Error!
print(mi_clase.atr_ins_pub_met_pub)
# print(mi_clase.__atr_ins_pri_met_pub) # Error!

print(dir(mi_clase))
```

Con `dir` se listan los atributos y métodos de la clase, incluso los ocultos.

Se puede hacer "trampa" para permitir que los atributos y métodos privados sean accesibles externamente. Aunque no se vea a simple vista, sí que están pero con un nombre distinto. Pero esto *NO es una buena idea*.

```py
mi_clase._Clase__atr_cla_pri
mi_clase._Clase__metodo_privado()
```