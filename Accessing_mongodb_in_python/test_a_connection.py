import pymongo
# def mongo_connect():
#    try:
#        conn = pymongo.MongoClient()
#        print "Mongo is connected!"
#        return conn
#    except pymongo.errors.ConnectionFailure, e:
#        print "Could not connect to MongoDB: %s" % e
 
# conn = mongo_connect()
# db = conn['twitter_stream']
# print db  # Database(MongoClient('localhost', 27017), u'twitter_stream')

# Note that the database won’t show in Mongo Management Studio until we have added some data.

def mongo_connect():
   try:
       conn = pymongo.MongoClient()
       print "Mongo is connected!"
       return conn
   except pymongo.errors.ConnectionFailure, e:
       print "Could not connect to MongoDB: %s" % e
 
conn = mongo_connect()
db = conn['twitter_stream']
coll = db.my_collection
print db.collection_names()  # []