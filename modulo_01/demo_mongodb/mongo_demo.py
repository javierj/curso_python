__author__ = 'Javier'

from pymongo import MongoClient

class DemoMongo():

    def __init__(self):
        self.host = "localhost"
        self.port = 27017

    def connect(self):
        self.client = MongoClient(self.host, self.port)

    def create_empty_collection(self):
        db = self.client.nueva_db
        col = db.nueva_coleccion

    def create_collection_and_insert_document(self):
        db = self.client.nueva_db
        col = db.nueva_coleccion
        id = col.insert({"Msg":"Hola mundo"})
        result = col.find_one({'_id':id})
        print(result)



if __name__ == '__main__':
    demo = DemoMongo()
    demo.connect()
    demo.create_collection_and_insert_document()
