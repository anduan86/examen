from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

import os

load_dotenv()

class MongoConecction:
    def __init__(self):
        user = os.getenv('MONGO_USER')
        passw = os.getenv('MONGO_PASS')
        uri = f"mongodb+srv://{user}:{passw}@cluster0.g4gozmk.mongodb.net/?retryWrites=true&w=majority"

        self.client = MongoClient(uri,server_api=ServerApi('1'))
    def test_connection(self):
        try:
            self.client.admin.command('ping')
            print("Conectado")
        except Exception as e:
            print(e)
if __name__ == '__main__':
    db().test_connection()


class MongoConnection:
    pass