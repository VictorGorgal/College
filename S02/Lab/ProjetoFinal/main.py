from pymongo import MongoClient
from bson.objectid import ObjectId


class Livraria:
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client['livraria']
        self.books_collection = self.db['livros']
        self.authors_collection = self.db['autores']
        self.reset_database()

    def reset_database(self):
        self.books_collection.delete_many({})
        self.authors_collection.delete_many({})

    def menu(self):
        while True:
            print("\nMenu Principal")
            print("1. Autores")
            print("2. Livros")
            print("3. Sair")
            choice = input("Selecione uma opção: ")

            if choice == "1":
                self.manage_authors()
            elif choice == "2":
                self.manage_books()
            elif choice == "3":
                print("Saindo...")
                break
            else:
                print("Opção invalida!")

    def manage_authors(self):
        while True:
            print("\nAutores")
            print("1. Criar autor")
            print("2. Ler autores")
            print("3. Atualizar autor")
            print("4. Deletar autor")
            print("5. Voltar")
            choice = input("Selecione uma opção: ")

            if choice == "1":
                self.create_author()
            elif choice == "2":
                self.read_authors()
            elif choice == "3":
                self.update_author()
            elif choice == "4":
                self.delete_author()
            elif choice == "5":
                break
            else:
                print("Opção invalida!")

    def manage_books(self):
        while True:
            print("\nLivros")
            print("1. Criar livros")
            print("2. Ler livros")
            print("3. Atualizar livros")
            print("4. Deletar livros")
            print("5. Voltar")
            choice = input("Selecione uma opção: ")

            if choice == "1":
                self.create_book()
            elif choice == "2":
                self.read_books()
            elif choice == "3":
                self.update_book()
            elif choice == "4":
                self.delete_book()
            elif choice == "5":
                break
            else:
                print("Opção invalida!")

    def create_author(self):
        nome = input("Insira o nome do autor: ")
        idade = int(input("Insira idade do autor: "))
        autor_id = self.authors_collection.insert_one({"nome": nome, "idade": idade}).inserted_id
        print(f"Autor criado com ID: {autor_id}")

    def read_authors(self):
        autores = self.authors_collection.find()
        for autor in autores:
            print(f"ID: {autor['_id']}, Name: {autor['nome']}, Age: {autor['idade']}")

    def update_author(self):
        autor_id = input("Insira id do autor a ser atualizado: ")
        nome = input("Insira novo nome: ")
        idade = input("Insira nova idade: ")
        if idade != '':
            idade = int(idade)
        else:
            idade = 0

        data = {}
        if nome:
            data['nome'] = nome
        if idade:
            data['idade'] = idade

        result = self.authors_collection.update_one({"_id": ObjectId(autor_id)}, {"$set": data})
        if result.modified_count > 0:
            print("Sucesso")
        else:
            print("Autor nao encontrado")

    def delete_author(self):
        autor_id = input("Insira id do autor a ser excluído: ")
        result = self.authors_collection.delete_one({"_id": ObjectId(autor_id)})
        if result.deleted_count > 0:
            print("Sucesso")
        else:
            print("Autor nao encontrado")

    def create_book(self):
        nome = input("Insira nome do livro: ")
        autor_id = input("Insira id do autor: ")
        nota = float(input("Insira nota do livro: "))

        if not self.authors_collection.find_one({"_id": ObjectId(autor_id)}):
            print("Autor nao encontrado")
            return

        book_id = self.books_collection.insert_one({
            "nome": nome,
            "id_autor": ObjectId(autor_id),
            "nota": nota
        }).inserted_id
        print(f"Livro criado com ID: {book_id}")

    def read_books(self):
        livros = self.books_collection.find()
        for livro in livros:
            autor = self.authors_collection.find_one({"_id": livro["id_autor"]})
            print(f"ID: {livro['_id']}, Nome: {livro['nome']}, Autor: {autor['nome']}, Nota: {livro['nota']}")

    def update_book(self):
        livro_id = input("Insira ID do livro a ser atualizado: ")
        nome = input("Insira novo nome: ")
        autor_id = input("Insira novo id do autor: ")
        nota = input("Insira nova nota: ")
        if nota != '':
            nota = float(nota)
        else:
            nota = 0

        data = {}
        if nome:
            data['nome'] = nome
        if autor_id:
            if self.authors_collection.find_one({"_id": ObjectId(autor_id)}):
                data['autor_id'] = ObjectId(autor_id)
            else:
                print("Autor nao encontrado")
                return
        if nota:
            data['nota'] = nota

        result = self.books_collection.update_one({"_id": ObjectId(livro_id)}, {"$set": data})
        if result.modified_count > 0:
            print("Sucesso")
        else:
            print("Livro nao encontrado")

    def delete_book(self):
        livro_id = input("Insira ID do livro a ser excluído: ")
        result = self.books_collection.delete_one({"_id": ObjectId(livro_id)})
        if result.deleted_count > 0:
            print("Sucesso")
        else:
            print("Livro nao encontrado")


if __name__ == "__main__":
    cli = Livraria()
    cli.menu()
