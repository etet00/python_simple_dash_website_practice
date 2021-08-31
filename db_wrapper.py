from setting import DB_USERNAME
from setting import DB_PASSWORD
from pymongo import MongoClient
# from pprint import pprint

CONNECTION = "mongodb+srv://{}:{}@cluster0.f5nmm.mongodb.net/post?retryWrites=true&w=majority".format(
    DB_USERNAME, DB_PASSWORD)

# CONNECTION = "mongodb+srv://yoshi:Jx2rbQXpORMX3D6U@cluster0.wf5gy.mongodb.net/air?retryWrites=true&w=majority"


class DBWrapper:
    def __init__(self):
        self.client = MongoClient(CONNECTION)
        self.db = self.client.face_book_crawler

    def get_data(self, site):
        # filter = {"p_content":{"$regex":".*颱風.*"}}
        condition = {"p_location": site}
        # posts = self.db.post.find().sort([('_id', -1)]).limit(3)
        posts = self.db.post.find(condition).limit(3)
        # print(posts["p_content"])
        return list(posts)

        # for post in posts:
        #     print(post["p_location"])
