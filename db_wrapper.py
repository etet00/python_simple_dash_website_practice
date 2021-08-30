from pymongo import MongoClient
# from pprint import pprint


class DBWrapper:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.face_book_crawler

    def get_data(self, site):
        # filter = {"p_content":{"$regex":".*颱風.*"}}
        filter = {"p_location": site}
        # posts = self.db.post.find().sort([('_id', -1)]).limit(3)
        posts = self.db.post.find(filter).limit(3)
        # print(posts["p_content"])
        return list(posts)

        # for post in posts:
        #     print(post["p_location"])
