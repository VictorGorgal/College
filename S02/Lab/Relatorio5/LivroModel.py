from bson.objectid import ObjectId


class LivroModel:
    def __init__(self, database):
        self.db = database

    def create_book(self, titulo, autor, ano, preco):
        try:
            res = self.db.collection.insert_one({
                'titulo': titulo,
                'autor': autor,
                'ano': ano,
                'preco': preco
            })
            print(f'Livro criado: {res.inserted_id}')
            return res.inserted_id
        except Exception as e:
            print(f'Erro: {e}')
            return None

    def read_book_by_id(self, id):
        try:
            res = self.db.collection.find_one({'_id': ObjectId(id)})
            print(f'Livro encontrado: {res}')
            return res
        except Exception as e:
            print(f'Erro: {e}')
            return None

    def update_book(self, id, titulo, autor, ano, preco):
        try:
            res = self.db.collection.update_one(
                {'_id': ObjectId(id)},
                {'$set': {
                    'titulo': titulo,
                    'autor': autor,
                    'ano': ano,
                    'preco': preco}
                }
            )
            print(f'Livro atualizado')
            return res.modified_count
        except Exception as e:
            print(f'Erro: {e}')
            return None

    def delete_book(self, id):
        try:
            res = self.db.collection.delete_one({'_id': ObjectId(id)})
            print(f'Livro excluido')
            return res.deleted_count
        except Exception as e:
            print(f'Erro: {e}')
            return None
