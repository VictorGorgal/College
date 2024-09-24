from Corrida import Corrida
from Motorista import Motorista
from Passageiro import Passageiro
from SimpleCLI import SimpleCLI


class motoristaCLI(SimpleCLI):
    def __init__(self, motorista_model):
        super().__init__()
        self.motorista_model = motorista_model
        self.add_command("create", self.create_motorista)
        self.add_command("read", self.read_motorista)
        self.add_command("update", self.update_motorista)
        self.add_command("delete", self.delete_motorista)

    def create_motorista(self):
        lista_corridas = []

        quant = int(input("Entre com a quantidade de corridas:"))
        for x in range(quant):
            nome_passageiro = str(input("Entre com o nome do passageiro: "))
            documento = str(input("Entre com o documento do passageiro"))
            passageiro = Passageiro(nome_passageiro, documento)
            nota_corrida = int(input("Entre com a nota da corrida: "))
            distancia_corrida = float(input("Entre com a distancia da corrida: "))
            valor = float(input("Entre com o valor da distancia: "))
            corrida = Corrida(nota_corrida, distancia_corrida, valor, passageiro)

            lista_corridas.append(corrida)

        nota_motorista = int(input("Entre com a nota do motorista: "))
        motorista = Motorista(nota_motorista, lista_corridas)
        self.motorista_model.create_motorista_DAO(motorista)

    def read_motorista(self):
        id = input("Enter the id: ")
        motorista = self.motorista_model.read_motorista(id)

    def update_motorista(self):
        id = input("Enter the id: ")
        lista_corridas = []
        quant = int(input("Entre com a quantidade de corridas: "))
        for x in range(quant):
            nome_passageiro = input("Entre com o nome do passageiro: ")
            documento = input("Entre com o documento do passageiro: ")
            passageiro = Passageiro(nome_passageiro, documento)

            nota_corrida = int(input("Entre com a nota da corrida: "))
            distancia_corrida = float(input("Entre com a distancia da corrida: "))
            valor = float(input("Entre com o valor da distancia: "))
            corrida = Corrida(nota_corrida, distancia_corrida, valor, passageiro)

            lista_corridas.append(corrida)

        nota_motorista = int(input("Entre com a nota do motorista: "))

        motorista = Motorista(nota_motorista, lista_corridas)
        self.motorista_model.update_motorista(id, motorista)

    def delete_motorista(self):
        id = input("Enter the id: ")
        self.motorista_model.delete_motorista(id)

    def run(self):
        print("Welcome to the motorista CLI!")
        print("Available commands: create, read, update, delete, quit")
        super().run()
