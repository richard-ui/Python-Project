import os
import pymongo
if os.path.exists("env.py"):
    import env


MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "myDatabase"
COLLECTION = "food"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


conn = mongo_connect(MONGO_URI)

coll = conn[DATABASE][COLLECTION]

documents = coll.find()

""" Insert multipe documents """
# new_docs = [{
#     "first": "terry",
#     "last": "pratchett",
#     "dob": "28/04/1948",
#     "gender": "m",
#     "hair_color": "not much",
#     "occupation": "writer",
#     "nationality": "british"
# }, {
#     "first": "george",
#     "last": "rr martin",
#     "dob": "20/09/1948",
#     "gender": "m",
#     "hair_color": "white",
#     "occupation": "writer",
#     "nationality": "american"
# }]
# coll.insert_many(new_docs)

""" Find documents with 'first' name set to 'douglas' """
# documents = coll.find({"first": "douglas"})

""" Delete documents with 'first' name set to 'douglas' """
# coll.remove({"name": "ice cream"})
# documents = coll.find()

""" Update a single document (first one only) """
# coll.update_one(
#     {"name": "ice cream"},
#     {"$set": {"price": "6.0"}}
# )
# documents = coll.find({"name": "ice cream"})

""" Update all documents """
coll.update_many(
    {"name": "ice cream"},
    {"$set": {"price": "6.0"}}
)
documents = coll.find({"name": "ice cream"})

for doc in documents:
    print(doc)