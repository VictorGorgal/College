from sympy import symbols, integrate, exp, ln

x = symbols('x')
c = 524 % 10

f_x = exp(3*x + c) - 4*ln(x**2) + 5*x - c

area = integrate(f_x, (x, 2, 8)).evalf()

print("Área:", area)
