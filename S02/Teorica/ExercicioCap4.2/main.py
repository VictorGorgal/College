from neo4j import GraphDatabase


class Database:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        if self.driver:
            self.driver.close()

    def execute_query(self, query, parameters=None):
        with self.driver.session() as session:
            result = session.run(query, parameters)
            return [record for record in result]


class TeacherCRUD:
    def __init__(self, database):
        self.db = database

    def create(self, name, ano_nasc, cpf):
        query = """
        CREATE (:Teacher {name: $name, ano_nasc: $ano_nasc, cpf: $cpf})
        """
        self.db.execute_query(query, {'name': name, 'ano_nasc': ano_nasc, 'cpf': cpf})
        print(f"Professor {name} criado com sucesso.")

    def read(self, name):
        query = """
        MATCH (t:Teacher {name: $name})
        RETURN t.name AS name, t.ano_nasc AS ano_nasc, t.cpf AS cpf
        """
        result = self.db.execute_query(query, {'name': name})
        if result:
            return result[0]
        else:
            print(f"Professor {name} não encontrado.")
            return None

    def update(self, name, newCpf):
        query = """
        MATCH (t:Teacher {name: $name})
        SET t.cpf = $newCpf
        RETURN t.name AS name, t.cpf AS cpf
        """
        result = self.db.execute_query(query, {'name': name, 'newCpf': newCpf})
        if result:
            print(f"CPF do professor {name} atualizado para {newCpf}.")
        else:
            print(f"Professor {name} não encontrado para atualização.")

    def delete(self, name):
        query = """
        MATCH (t:Teacher {name: $name})
        DETACH DELETE t
        """
        self.db.execute_query(query, {'name': name})
        print(f"Professor {name} deletado com sucesso.")


uri = "neo4j+s://eac924e9.databases.neo4j.io"
usuario = "neo4j"
senha = "0DkfVBawdR-xQkiuZau6E_1QDWhxU8F6Md_uawYDbWk"

db = Database(uri, usuario, senha)
teacher_crud = TeacherCRUD(db)

try:
    while True:
        print("1. Criar professor")
        print("2. Ler professor")
        print("3. Atualizar professor")
        print("4. Deletar professor")
        print("5. Sair")

        opcao = input("Digite o número da opção: ")

        if opcao == '1':
            name = input("Nome do professor: ")
            ano_nasc = int(input("Ano de nascimento: "))
            cpf = input("CPF: ")
            teacher_crud.create(name, ano_nasc, cpf)

        elif opcao == '2':
            name = input("Nome do professor para pesquisa: ")
            teacher = teacher_crud.read(name)
            if teacher:
                print(f"Nome: {teacher['name']}, Ano de Nascimento: {teacher['ano_nasc']}, CPF: {teacher['cpf']}")

        elif opcao == '3':
            name = input("Nome do professor para atualização: ")
            new_cpf = input("Novo CPF: ")
            teacher_crud.update(name, new_cpf)

        elif opcao == '4':
            name = input("Nome do professor para deletar: ")
            teacher_crud.delete(name)

        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

finally:
    db.close()
