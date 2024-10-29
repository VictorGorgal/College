# Exercício Avaliativo 4 - Banco de dados orientado à colunas e Cassandra

"""
Estoque da Montadora

Um fabricante de automóveis contratou você para desenvolver um sistema de banco de dados distribuído usando o Cassandra para as linhas de montagem de toda a corporação, onde cada máquina pudesse acessar a base de dados e buscar as peças de maneira correta para ser montada nos respectivos modelos de veículos. Para isso, você deverá criar a tabela estoque no sistema DataStax ASTRA e inserir as colunas usando o arquivo auxiliar disponibilizado junto com essa atividade.

Questão 1: Siga os itens listados abaixo:

Faça a inserção de uma nova peça com os dados abaixo:

id: 5
nome: Pistao
carro: Mustang
estante: 4
nível: 1
quantidade: 167

Faça a inserção de uma nova peça com os dados abaixo:

id: 4
nome: Suspencao
carro: Argo
estante: 1
nível: 1
quantidade: 3500

Questão 2: Escreva o comando CQL utilizado para cada item abaixo:

Faça uma busca no banco de dados que retorno todos os dados do item com nome 'Pistão';
Faça uma busca no banco que calcule a média aritmética da quantidade de todas as colunas armazenadas na tabela;
Faça uma busca que retorne quantas colunas tem armazenadas na tabela;
Busque a maior e a menor quantidade de peças usando as alias "maior quantidade" e "menor quantidade" para a tabela estoque.
Faça uma busca que retorne os atributos nome, carro e quantidade, onde a estante seja igual a 3;
Faça uma busca que retorne a média aritmética da quantidade onde o nível seja igual a 1;
Faça uma busca retornando todos os atributos onde a estante seja menor do que 3 e o nível seja maior do que 4.


Questão 3: Elabore um script Python que seja capaz de fazer uma consulta mostrando nome, estante e quantidade do carro fornecido pelo usuário.

"""

import json

from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra.query import dict_factory


class CassandraConnector:
    def __init__(self):
        self.cassandra_session = None

    def get_cassandra_connector(self):
        if self.cassandra_session is None:
            cloud_config = {
                "secure_connect_bundle": "secure-connect-montadora.zip"
            }
            with open("montadora-token.json") as f:
                secrets = json.load(f)

            CLIENT_ID = secrets["clientId"]
            CLIENT_SECRET = secrets["secret"]

            auth_provider = PlainTextAuthProvider(CLIENT_ID, CLIENT_SECRET)
            cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
            self.cassandra_session = cluster.connect()
            self.cassandra_session.row_factory = dict_factory
            self.cassandra_session.set_keyspace("montadora")
        return self.cassandra_session


class AutoPart:
    def __init__(self, id, name, car, shelf, level, amount):
        self.id = id
        self.name = name
        self.car = car
        self.shelf = shelf
        self.level = level
        self.amount = amount

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "car": self.car,
            "shelf": self.shelf,
            "level": self.level,
            "amount": self.amount
        }


class AutoPartDAO:
    def __init__(self):
        connector = CassandraConnector()
        self.session = connector.get_cassandra_connector()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS estoque (
            id int PRIMARY KEY,
            nome text,
            carro text,
            estante int,
            nivel int,
            quantidade int
        );
        """
        self.session.execute(query)

    def add_part(self, part):
        query = """
        INSERT INTO estoque (id, nome, carro, estante, nivel, quantidade)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        self.session.execute(query, (part.id, part.name, part.car, part.shelf, part.level, part.amount))

    def get_part(self, name):
        query = "SELECT * FROM estoque WHERE nome = %s ALLOW FILTERING"
        rows = self.session.execute(query, (name,))
        for row in rows:
            print(row)

    def get_average_amount(self):
        query = "SELECT AVG(quantidade) AS media_quantidade FROM estoque"
        row = self.session.execute(query).one()
        print(f"Média de quantidade: {row['media_quantidade']}")

    def get_total_amount(self):
        query = "SELECT COUNT(*) AS total_itens FROM estoque"
        row = self.session.execute(query).one()
        print(f"Total de itens: {row['total_itens']}")

    def get_max_min(self):
        query = """
        SELECT MAX(quantidade) AS "maior quantidade", MIN(quantidade) AS "menor quantidade"
        FROM estoque
        """
        row = self.session.execute(query).one()
        print(f"Maior quantidade: {row['maior quantidade']}, Menor quantidade: {row['menor quantidade']}")

    def get_parts_from_shelf(self, shelf):
        query = "SELECT nome, carro, quantidade FROM estoque WHERE estante = %s ALLOW FILTERING"
        rows = self.session.execute(query, (shelf,))
        for row in rows:
            print(row)

    def get_average_amount_from_level(self, level):
        query = "SELECT AVG(quantidade) AS media_nivel FROM estoque WHERE nivel = %s ALLOW FILTERING"
        row = self.session.execute(query, (level,)).one()
        print(f"Média de quantidade no nível {level}: {row['media_nivel']}")

    def get_parts_from_shelf_and_level(self, shelf, level):
        query = "SELECT * FROM estoque WHERE estante < %s AND nivel > %s ALLOW FILTERING"
        rows = self.session.execute(query, (shelf, level))
        for row in rows:
            print(row)

    def get_parts_of_car(self, car):
        query = "SELECT nome, estante, quantidade FROM estoque WHERE carro = %s ALLOW FILTERING"
        rows = self.session.execute(query, (car,))
        for row in rows:
            print(row)


# Executa as funções com os dados fornecidos no exercício
if __name__ == "__main__":
    dao = AutoPartDAO()
    dao.create_table()

    # Questão 1
    part1 = AutoPart(id=5, name='Pistao', car='Mustang', shelf=4, level=1, amount=167)
    part2 = AutoPart(id=4, name='Suspencao', car='Argo', shelf=1, level=1, amount=3500)
    dao.add_part(part1)
    dao.add_part(part2)

    # Questão 2
    dao.get_part("Pistao")
    dao.get_average_amount()
    dao.get_total_amount()
    dao.get_max_min()
    dao.get_parts_from_shelf(3)
    dao.get_average_amount_from_level(1)
    dao.get_parts_from_shelf_and_level(3, 4)

    # Questão 3
    car_name = input("Digite o nome do carro: ")
    dao.get_parts_of_car(car_name)
