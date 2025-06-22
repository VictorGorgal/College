from sympy import symbols, Eq, solve

I1, I2, I3 = symbols('I1 I2 I3')
c = 524 % 10
V1 = 10 + 2 * c
V2 = 5 + 2 * c

eq1 = Eq(-V1 + 25*I1 - 10*I2, 0)
eq2 = Eq(10*I2 - 20*I3 + V2, 0)
eq3 = Eq(I1, I2 + I3)

solution = solve([eq1, eq2, eq3], (I1, I2, I3))

for i, v in solution.items():
    print(f"{i} = {v.evalf()} A")
