class Passageiro:
    def __init__(self, nome, documento):
        self.nome = nome
        self.documento = documento

    def __str__(self):
        print(f'(Nome: {self.nome}, Documento: {self.documento})')
