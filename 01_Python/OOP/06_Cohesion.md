# Cohesión

La cohesión hace referencia al grado de relación entre los elementos de un módulo.

Las funciones deben realizar tareas únicas y bien definidas. Cuantas más cosas diferentes haga una función sin relación entre sí, más complicado será el código de entender.

La **Cohesión fuerte** debe ser nuestro objetivo. Indica que existe una alta relación entre los elementos del módulo.

> Normalmente **acoplamiento débil** se relaciona con cohesión fuerte o alta.

```py
# Cohesión débil. Hace muchas cosas.
def suma():
    num1 = float(input("Dame primer número"))
    num2 = float(input("Dame segundo número"))
    suma = num1 + num2
    print(suma)
```

```py
# Cohesión fuerte. Conciso. Reutilizable. Mantenible.
def suma(numeros):
    total = 0
    for i in numeros:
        total = total + i
    return total
```