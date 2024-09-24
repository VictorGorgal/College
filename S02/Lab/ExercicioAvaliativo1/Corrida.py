class Corrida:
    def __init__(self, nota, distancia, valor, passageiro):
        self.nota = nota
        self.distancia = distancia
        self.valor = valor
        self.passageiro = passageiro

    def __str__(self):
        print(f'Nota: {self.nota}')
        print(f'Distancia: {self.distancia}')
        print(f'Valor: {self.valor}')
        print(f'Passageiro: {self.passageiro}')
