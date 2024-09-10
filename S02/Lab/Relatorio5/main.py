from LivroModel import LivroModel
from database import Database

db = Database(database='livraria', collection='livros')
db.resetDatabase()
livroModel = LivroModel(db)

while True:
    print('Cadastrar livro [1]')
    print('Buscar livro [2]')
    print('Atualizar livro [3]')
    print('Excluir livro [4]')

    sel = input()
    if sel == '1':
        print('Cadastrar livro:\n')
        titulo = input('Insira o título: ')
        autor = input('Insira o autor: ')
        ano = int(input('Insira o ano: '))
        preco = float(input('Insira o preco: '))
        livroModel.create_book(titulo, autor, ano, preco)
    elif sel == '2':
        print('Buscar livro:\n')
        idLivro = input('Insira o id do livro desejado: ')
        livroModel.read_book_by_id(idLivro)
    elif sel == '3':
        print('Atualizar livro:\n')
        idLivro = input('Insira o id do livro: ')
        titulo = input('Insira o título: ')
        autor = input('Insira o autor: ')
        ano = int(input('Insira o ano: '))
        preco = float(input('Insira o preco: '))
        livroModel.update_book(idLivro, titulo, autor, ano, preco)
    elif sel == '4':
        print('Excluir livro:\n')
        idLivro = input('Insira o id do livro: ')
        livroModel.delete_book(idLivro)
    else:
        print('Opção inválida')
