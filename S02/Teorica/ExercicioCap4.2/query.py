from neo4j import GraphDatabase


def limpar_banco(driver):
    query = """
    MATCH (n)
    DETACH DELETE n
    """
    with driver.session() as session:
        session.run(query)


def carregar_dados(driver):
    with open("DB.txt", "r") as file:
        queries = file.read().splitlines()

    with driver.session() as session:
        for query in queries:
            if query.strip():
                session.run(query)


def encontrar_professor(driver, nome):
    query = """
    MATCH (p:Teacher)
    WHERE p.name = $nome
    RETURN p.ano_nasc AS nascimento, p.cpf AS cpf
    """
    with driver.session() as session:
        resultado = session.run(query, nome=nome)
        return [(registro["nascimento"], registro["cpf"]) for registro in resultado]


def encontrar_professor_comeca_com(driver, nome):
    query = """
    MATCH (p:Teacher)
    WHERE p.name STARTS WITH $nome
    RETURN p.name AS name, p.cpf AS cpf
    """
    with driver.session() as session:
        resultado = session.run(query, nome=nome)
        return [(registro["name"], registro["cpf"]) for registro in resultado]


def buscar_cidades(driver):
    query = """
    MATCH (c:City)
    RETURN c.name AS city_name
    """
    with driver.session() as session:
        resultado = session.run(query)
        return [registro["city_name"] for registro in resultado]


def buscar_escolas_por_numero(driver):
    query = """
    MATCH (s:School)
    WHERE s.number >= 150 AND s.number <= 550
    RETURN s.name AS school_name, s.address AS address, s.number AS number
    """
    with driver.session() as session:
        resultado = session.run(query)
        return [(registro["school_name"], registro["address"], registro["number"]) for registro in resultado]


def encontrar_professores_idade_extremos(driver):
    query = """
    MATCH (p:Teacher)
    RETURN MAX(p.ano_nasc) AS ano_nascimento_mais_jovem, MIN(p.ano_nasc) AS ano_nascimento_mais_velho
    """
    with driver.session() as session:
        resultado = session.run(query)
        return [(registro["ano_nascimento_mais_jovem"], registro["ano_nascimento_mais_velho"]) for registro in resultado]


def media_populacao_cidades(driver):
    query = """
    MATCH (c:City)
    RETURN AVG(c.population) AS media_populacao
    """
    with driver.session() as session:
        resultado = session.run(query)
        return resultado.single()["media_populacao"]


def encontrar_cidade_por_cep(driver, cep):
    query = """
    MATCH (c:City)
    WHERE c.cep = $cep
    RETURN REPLACE(c.name, 'a', 'A') AS nome_modificado
    """
    with driver.session() as session:
        resultado = session.run(query, cep=cep)
        return resultado.single()["nome_modificado"]


def obter_terceira_letra_nome(driver):
    query = """
    MATCH (p:Teacher)
    RETURN substring(p.name, 2, 1) AS terceiro_caractere
    """
    with driver.session() as session:
        resultado = session.run(query)
        return [registro["terceiro_caractere"] for registro in resultado]


uri = "neo4j+s://eac924e9.databases.neo4j.io"
usuario = "neo4j"
senha = "0DkfVBawdR-xQkiuZau6E_1QDWhxU8F6Md_uawYDbWk"

driver = GraphDatabase.driver(uri, auth=(usuario, senha))

limpar_banco(driver)
carregar_dados(driver)

print(encontrar_professor(driver, 'Renzo'))
print(encontrar_professor_comeca_com(driver, 'M'))
print(buscar_cidades(driver))
print(buscar_escolas_por_numero(driver))
print(encontrar_professores_idade_extremos(driver))
print(media_populacao_cidades(driver))
print(encontrar_cidade_por_cep(driver, '37540-000'))
print(obter_terceira_letra_nome(driver))

driver.close()
