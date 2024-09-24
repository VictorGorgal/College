class Motorista:
    def __init__(self, nota, corridas):
        self.corridas = corridas
        self.nota = nota

    def __str__(self):
        print(f'Nota: {self.nota}')
        print(f'Corridas:')
        for corrida in self.corridas:
            print(corrida)
            print(f'-----')
