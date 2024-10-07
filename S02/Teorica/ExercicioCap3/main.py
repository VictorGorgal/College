"""

1)
    CREATE (joao:Pessoa:Engenheiro {nome: "João", sexo: "M", idade: 45})
    CREATE (maria:Pessoa:Medica {nome: "Maria", sexo: "F", idade: 42})
    CREATE (ana:Pessoa:Estudante {nome: "Ana", sexo: "F", idade: 18})
    CREATE (bruno:Pessoa:Estudante {nome: "Bruno", sexo: "M", idade: 20})
    CREATE (cachorro:Pet:Cachorro {nome: "Rex", idade: 5, raça: "Labrador"})
    CREATE (gato:Pet:Gato {nome: "Felix", idade: 3, cor: "Preto"})

2)
    CREATE (joao)-[:PAI_DE]->(ana)
    CREATE (maria)-[:MAE_DE]->(ana)
    CREATE (joao)-[:PAI_DE]->(bruno)
    CREATE (joao)-[:DONO_DE {desde: 2018}]->(cachorro)
    CREATE (maria)-[:DONO_DE {desde: 2020}]->(gato)
    CREATE (ana)-[:IRMA_DE]->(bruno)

"""

from neo4j import GraphDatabase


def encontrar_filhos(driver, nome_pai):
    query = """
    MATCH (pessoa:Pessoa)-[:PAI_DE]->(filho:Pessoa)
    WHERE pessoa.nome = $nome_pai
    RETURN filho.nome AS nome_do_filho
    """
    with driver.session() as session:
        resultado = session.run(query, nome_pai=nome_pai)
        return [registro["nome_do_filho"] for registro in resultado]


def encontrar_pets(driver, nome_dono):
    query = """
    MATCH (pessoa:Pessoa)-[:DONO_DE]->(pet:Pet)
    WHERE pessoa.nome = $nome_dono
    RETURN pet.nome AS nome_do_pet
    """
    with driver.session() as session:
        resultado = session.run(query, nome_dono=nome_dono)
        return [registro["nome_do_pet"] for registro in resultado]


def encontrar_irmaos(driver, nome):
    query = """
    MATCH (pessoa:Pessoa)-[:IRMA_DE]->(irmao:Pessoa)
    WHERE pessoa.nome = $nome
    RETURN irmao.nome AS nome_do_irmao
    """
    with driver.session() as session:
        resultado = session.run(query, nome=nome)
        return [registro["nome_do_irmao"] for registro in resultado]


def limpar_banco(driver):
    query = """
    MATCH (n)
    DETACH DELETE n
    """
    with driver.session() as session:
        session.run(query)


uri = "neo4j+s://-.databases.neo4j.io"
usuario = "neo4j"
senha = "-"

driver = GraphDatabase.driver(uri, auth=(usuario, senha))

# limpar_banco(driver)
print("Filhos de João:", encontrar_filhos(driver, "João"))
print("Pets de Maria:", encontrar_pets(driver, "Maria"))
print("Irmãos de Ana:", encontrar_irmaos(driver, "Ana"))

driver.close()
