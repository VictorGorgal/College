from sympy import Limit, Symbol, sqrt, S

x = Symbol('x')
c = 524 % 10
func1 = ((c + 1) * x - (c + 1)) / (sqrt(x) - 1)
func2 = ((c + 1) * x**4 + 3 * x**2 - 2) / (4 - x**4)

resultado1 = Limit(func1, x, 0).doit()
resultado2 = Limit(func2, x, S.Infinity).doit()
resultado3 = Limit(func2, x, -S.Infinity).doit()

print("Resultado 1:", resultado1)
print("Resultado 2:", resultado2)
print("Resultado 3:", resultado3)
