from pymongo import MongoClient
from bson.objectid import ObjectId

import Motorista


class MotoristaDAO:
    def __init__(self, database):
        self.db = database

    def create_motorista_DAO(self, motorista: Motorista):
        try:
            motorista_doc = {
                "nota_motorista": int(motorista.nota),
                "corridas": [{
                    "nota": int(corrida.nota),
                    "distancia": float(corrida.distancia),
                    "valor": float(corrida.valor),
                    "passageiro": {
                        "nome": corrida.passageiro.nome,
                        "documento": corrida.passageiro.documento
                    }
                } for corrida in motorista.corridas]
            }

            res = self.db.collection.insert_one(motorista_doc)
            print(f"Motorista created with id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"An error occurred while creating motorista: {e}")
            return None

    def read_motorista(self, id: str):
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            print(f"motorista found: {res}")
            return res
        except Exception as e:
            print(f"An error occurred while reading motorista: {e}")
            return None

    def update_motorista(self, id: str, motorista: list):
        try:
            motorista_doc = {
                "$set": {
                    "nota_motorista": int(motorista.nota_motorista),
                    "corridas": [{
                        "nota": int(corrida.nota_corrida),
                        "distancia": float(corrida.distancia),
                        "valor": float(corrida.valor),
                        "passageiro": {
                            "nome": corrida.passageiro.nome,
                            "documento": corrida.passageiro.documento
                        }
                    } for corrida in motorista.corrida]
                }
            }

            res = self.db.collection.update_one({"_id": ObjectId(id)}, motorista_doc)
            print(f"motorista updated: {res.modified_count} document(s) modified")
            return res.modified_count
        except Exception as e:
            print(f"An error occurred while updating motorista: {e}")
            return None

    def delete_motorista(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"motorista deleted: {res.deleted_count} document(s) deleted")
            return res.deleted_count
        except Exception as e:
            print(f"An error occurred while deleting motorista: {e}")
            return None
