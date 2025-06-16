class SimplexSolver:
    def __init__(self, c, A, b):
        """
        c: Coeficientes da função objetivo (maximização).
        A: Coeficientes das restrições (<=).
        b: Termos independentes das restrições.
        """
        self.original_c = c
        self.A = [row + [0] * i + [1] + [0] * (len(b) - i - 1) for i, row in enumerate(A)]
        self.b = b
        self.num_vars = len(c)
        self.num_constraints = len(b)
        self.tableau = self._build_tableau(c)
        self.basic_vars = [self.num_vars + i for i in range(self.num_constraints)]

    def _build_tableau(self, c):
        tableau = [row + [bi] for row, bi in zip(self.A, self.b)]
        last_row = [-ci for ci in c] + [0] * self.num_constraints + [0]
        tableau.append(last_row)
        return tableau

    def _pivot(self, row: int, col: int):
        pivot_element = self.tableau[row][col]
        self.tableau[row] = [v / pivot_element for v in self.tableau[row]]
        for r in range(len(self.tableau)):
            if r != row:
                ratio = self.tableau[r][col]
                self.tableau[r] = [
                    self.tableau[r][i] - ratio * self.tableau[row][i]
                    for i in range(len(self.tableau[0]))
                ]

    def solve(self):
        while True:
            last_row = self.tableau[-1][:-1]
            if all(c >= 0 for c in last_row):
                break
            col = last_row.index(min(last_row))
            ratios = []
            for i in range(self.num_constraints):
                if self.tableau[i][col] > 0:
                    ratios.append(self.tableau[i][-1] / self.tableau[i][col])
                else:
                    ratios.append(float('inf'))
            if all(r == float('inf') for r in ratios):
                raise Exception("Solução ilimitada.")
            row = ratios.index(min(ratios))
            self.basic_vars[row] = col
            self._pivot(row, col)

    def get_solution(self):
        solution = [0.0] * (self.num_vars + self.num_constraints)
        for i, var in enumerate(self.basic_vars):
            solution[var] = self.tableau[i][-1]
        return solution[:self.num_vars], self.tableau[-1][-1]

    def get_shadow_prices(self):
        return self.tableau[-1][self.num_vars:self.num_vars + self.num_constraints]

    def analyze_variation(self, delta_b):
        new_rhs = []
        for i in range(self.num_constraints):
            temp = 0
            for j in range(self.num_constraints):
                temp += self.tableau[i][j+len(self.original_c)] * delta_b[j]

            temp += self.tableau[i][-1]
            new_rhs.append(temp)

        if all(new_rhs[i] >= 0 for i in range(len(new_rhs))):
            shadow_prices = self.get_shadow_prices()
            delta_z = sum(shadow_prices[i] * delta_b[i] for i in range(self.num_constraints))
            new_z = self.tableau[-1][-1] + delta_z
            return True, new_z, shadow_prices
        else:
            return False, self.tableau[-1][-1], []


if __name__ == "__main__":
    # Exemplo:
    # Max z = 3x + 5y
    # s.a.
    #   x +  y <= 4
    #   2x + 3y <= 9

    c = [80, 70, 100, 16]
    A = [
        [1, 1, 1, 4],
        [0, 1, 1, 2],
        [3, 2, 4, 0],
    ]
    b = [250, 600, 500]

    solver = SimplexSolver(c, A, b)
    solver.solve()

    sol, z = solver.get_solution()
    print("Solução ótima:", sol)
    print("Valor ótimo:", z)
    print("Preços sombra:", solver.get_shadow_prices())

    # Variação desejada em b
    delta_b = [250, 0, 0]
    viavel, novo_z, shadow_prices = solver.analyze_variation(delta_b)
    print("Alterações viáveis?", viavel)
    if viavel:
        print("Novo lucro ótimo:", novo_z)
        print("Preços-sombra válidos:", shadow_prices)
    else:
        print("Alterações tornam a solução inviável.")
