class SimplexSolver:
    def __init__(self, c, A, b):
        """
        c: Coeficientes da função objetivo (maximização).
        A: Coeficientes das restrições (<=).
        b: Termos independentes das restrições.
        """
        self.funcao_objetivo = c
        self.restricoes = [linha + [0] * i + [1] + [0] * (len(b) - i - 1) for i, linha in enumerate(A)]
        self.termos_independentes = b
        self.num_variaveis = len(c)
        self.num_restricoes = len(b)
        self.tabela = self._construir_tabela(c)
        self.variaveis_basicas = [self.num_variaveis + i for i in range(self.num_restricoes)]

    def _construir_tabela(self, c):
        tabela = [linha + [bi] for linha, bi in zip(self.restricoes, self.termos_independentes)]
        linha_objetivo = [-ci for ci in c] + [0] * self.num_restricoes + [0]
        tabela.append(linha_objetivo)
        return tabela

    def _pivoteamento(self, linha: int, coluna: int):
        elemento_pivo = self.tabela[linha][coluna]
        self.tabela[linha] = [v / elemento_pivo for v in self.tabela[linha]]

        for r in range(len(self.tabela)):
            if r == linha:
                continue

            fator = self.tabela[r][coluna]
            self.tabela[r] = [
                self.tabela[r][i] - fator * self.tabela[linha][i]
                for i in range(len(self.tabela[0]))
            ]

    def resolver(self):
        while True:
            ultima_linha = self.tabela[-1][:-1]

            if all(c >= 0 for c in ultima_linha):
                break

            coluna_pivo = ultima_linha.index(min(ultima_linha))
            razoes = []
            for i in range(self.num_restricoes):
                if self.tabela[i][coluna_pivo] > 0:
                    razoes.append(self.tabela[i][-1] / self.tabela[i][coluna_pivo])
                else:
                    razoes.append(float('inf'))

            if all(r == float('inf') for r in razoes):
                raise Exception("Solução ilimitada.")

            linha_pivo = razoes.index(min(razoes))
            self.variaveis_basicas[linha_pivo] = coluna_pivo
            self._pivoteamento(linha_pivo, coluna_pivo)

    def get_solucao(self):
        solucao = [0.0] * (self.num_variaveis + self.num_restricoes)

        for i, var in enumerate(self.variaveis_basicas):
            solucao[var] = self.tabela[i][-1]

        return solucao[:self.num_variaveis], self.tabela[-1][-1]

    def get_precos_sombra(self):
        return self.tabela[-1][self.num_variaveis:self.num_variaveis + self.num_restricoes]

    def analisar_variacao(self, delta_b):
        novos_rhs = []
        for i in range(self.num_restricoes):
            temp = 0
            for j in range(self.num_restricoes):
                temp += self.tabela[i][j + len(self.funcao_objetivo)] * delta_b[j]
            temp += self.tabela[i][-1]
            novos_rhs.append(temp)

        if all(novos_rhs[i] >= 0 for i in range(len(novos_rhs))):
            precos_sombra = self.get_precos_sombra()
            delta_z = sum(precos_sombra[i] * delta_b[i] for i in range(self.num_restricoes))
            novo_z = self.tabela[-1][-1] + delta_z
            return True, novo_z, precos_sombra

        return False, 0, []


if __name__ == "__main__":
    # Exemplo:
    # Max z = 80x1 + 70x2 + 100x3 + 16x4
    # s.a.
    #    x1 +  x2 +  x3 + 4x4 <= 250
    #          x2 +  x3 + 2x4 <= 600
    #   3x1 + 2x2 + 4x3       <= 500

    c = [80, 70, 100, 16]
    A = [
        [1, 1, 1, 4],
        [0, 1, 1, 2],
        [3, 2, 4, 0],
    ]
    b = [250, 600, 500]

    solver = SimplexSolver(c, A, b)
    solver.resolver()

    sol, z = solver.get_solucao()
    print("Solução ótima:", sol)
    print("Valor ótimo:", z)
    print("Preços sombra:", solver.get_precos_sombra())

    # dx5 = -25
    # dx6 = -60
    # dx7 = -50
    delta_b = [-25, -60, -50]
    viavel, novo_z, shadow_prices = solver.analisar_variacao(delta_b)
    print("Alterações viáveis?", viavel)
    if viavel:
        print("Novo lucro ótimo:", novo_z)
        print("Preços-sombra válidos:", shadow_prices)
    else:
        print("Alterações tornam a solução inviável.")
