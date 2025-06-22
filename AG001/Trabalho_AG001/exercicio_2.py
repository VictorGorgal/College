from sympy import integrate, diff, Symbol, Rational

t = Symbol('t')
c = 524 % 10

v_t = 6 * (c + 1) * t**Rational(1, 5) - 3 * (c + 1) * t**2 + t / (c + 3) - 4
x_t = integrate(v_t, t)
a_t = diff(v_t, t)

x_2 = x_t.subs(t, 2).evalf()
x_5 = x_t.subs(t, 5).evalf()
delta_x = x_5 - x_2

print("Equação do Deslocamento:", x_t)
print("Deslocamento de t = 2s a t = 5s:", delta_x)
print("Equação da Aceleração:", a_t)
