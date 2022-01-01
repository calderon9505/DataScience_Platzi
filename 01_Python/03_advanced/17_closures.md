# Closure

Técnica para recordar valores que están en **scopes** superiores, incluso si dicho scope superior sea borrado.

* se debe tener una **nested function**

* La **nested fuction** debe referenciar un valor de un scope superior

* La función que envuelve la **nested fuction** debe retorna la **nested fuction**.

```py
def make_multiplier(x):
	def multiplier(n):
		return x*n
	return multiplier

times10 = make_multiplier(10)
times4 = make_multiplier(4)

print(times10(3)) # 30
print(times4(5)) #20
print(times10(times4(2))) # 80
```