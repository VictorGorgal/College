from sympy import Symbol, Eq, sqrt, solve, cos, exp

x = Symbol('x')
c = 524 % 10

eq1 = Eq(2 * cos(4 * (c + 1) * x), -5)
eq2 = Eq(5*sqrt(x) - 4 * x**2 + x/2, c)
eq3 = Eq(exp(x+1) + exp(x-2) + exp(x), c+4)

sol_eq1 = solve(eq1, x)
sol_eq2 = solve(eq2, x)
sol_eq3 = solve(eq3, x)

print("Soluções 1:", sol_eq1)
print("Soluções 2:", sol_eq2)
print("Soluções 3:", sol_eq3)
