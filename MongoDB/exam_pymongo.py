from pymongo import MongoClient

from pprint import pprint

print("Connexion à la base de données")

print("Question a")
client = MongoClient(
    host="127.0.0.1",
    port = 27017,
    username = "admin",
    password = "pass"
)

print("Question b")
print(client.list_database_names())

print("Question c")
sample = client["sample"]
print(sample.list_collection_names())

print("Question d")
from pprint import pprint
pprint(sample["books"].find_one())

print("Question e")
number_document = len(list(sample["books"].find()))
print("Le nombre de documents dans la collection books est: {}".format(number_document))

print("Exploration de la base")
print("Question a")
col = sample["books"]
print("le nombre de livres avec de plus de 400 pages est {}".format(
    len(
        list(
            col.find(
                {
                    "pageCount":{"$gt":400}  
                }
            )
        )
    ))
)
print("le nombre de livres avec de plus de 400 pages et qui sont publiés est {}".format(
    len(
        list(
            col.find(
                {
                    "$and": [
                        {"pageCount":{"$gt":400}}, 
                        {"status":"PUBLISH"}  
                    ]
                }
            )
        )
    ))
)

print("Question b")
import re
exp = re.compile("Android")
print("Le nombre delivres ayant le mot clé Android dans leur description est {}".format(
     len(
         list(
            col.aggregate([
                {"$match":{"$or":[{"shortDescription":exp}, {"longDescription":exp}]}}
                ]
            )
         )
     )


    )
)

print("Question c")
print(col.find().distinct("categories"))

print("Question d")
import re
exp_Python = re.compile("Python")
exp_Java = re.compile("Java")
exp_Cplusplus = re.compile("C\+\+")
exp_Scala = re.compile("Scala")
print("Le nombre de livres qui contiennent des noms de langages suivant dans leur description longue : Python, Java, C++, Scala est {}".format(
     len(
         list(
            col.aggregate([
                {"$match":{"$or":[{"longDescription":exp_Python}, {"longDescription":exp_Java},{"longDescription":exp_Cplusplus},{"longDescription":exp_Scala}]}}
                ]
            )
         )
     )


    )
)

print("Question e")
pprint(
    list(
        col.aggregate(
            [
                { 
                    "$unwind" : "$categories"                   
                },
                {
                     "$group":{"_id":"$categories", 
                               "maximumPagesPerCategories":{"$max":"$pageCount"}, 
                               "minimumPagesPerCategories":{"$min":"$pageCount"},
                               "averagePagesPerCategories":{"$avg":"$pageCount"}
                              }
                }
            ]
        )
    )
)

print("Question f")

pprint(
    list(
        col.aggregate([
            {
                "$project":
                    {
                        "_id":1,
                        "title":"$title",
                        "year":{"$year":"$publishedDate"},
                        "month":{"$month":"$publishedDate"},
                        "day":{"$dayOfMonth":"$publishedDate"}
                    }
            },
            {
                "$match":{
                            "year":{"$gt":2009}
                        }
            },
            {
                "$limit":20
            }
           
        ])
    )
)

print("Question g")
pprint(
    list(
        col.aggregate([
            {
                "$project":
                    {
                        "title":"$title",
                        "date":"$publishedDate",
                        "author1":{"$arrayElemAt":["$authors",0]},
                        "author2":{"$arrayElemAt":["$authors",1]},
                        "author3":{"$arrayElemAt":["$authors",2]},
                        "author4":{"$arrayElemAt":["$authors",3]}
                    }
            },
            {
                "$sort":{"date":-1}
            },
            {
                "$limit":20
            }
        ])
    )
)
print("Question h")
pprint(
    list(
        col.aggregate([

            {
                "$project":
                    {
                        "author1":{"$arrayElemAt":["$authors",0]}
                    }
            },
            {
                "$group":{"_id":"$author1","nb_articles":{"$sum":1}}
            },
            {
                "$match":{"_id":{"$exists":True, "$ne":None}}
            },

            {
                "$sort":{"nb_articles":-1}
            },
            {
                "$limit":10
            }
             
           
        ])
    )
)
