import pymongo


personnages = [
   { "name" : "Dagger", "ATK": 23, "DEF": 6, "PV": 105},
   { "name" : "Blake", "ATK": 19, "DEF": 9, "PV": 95},
   { "name" : "Ranger", "ATK": 17, "DEF": 15, "PV": 120},
   { "name" : "Ace", "ATK": 25, "DEF": 3, "PV": 70},
   { "name" : "Duke", "ATK": 14, "DEF": 12, "PV": 110},
   { "name" : "Phoenix", "ATK": 22, "DEF": 8, "PV": 85},
   { "name" : "Cobra", "ATK": 18, "DEF": 7, "PV": 90},
   { "name" : "Hawk", "ATK": 20, "DEF": 5, "PV": 80},
   { "name" : "Field", "ATK": 16, "DEF": 13, "PV": 90},
   { "name" : "Striker", "ATK": 15, "DEF": 10, "PV": 100}
]

monstres = [
   { "name" : "Nocthrax", "ATK": 25, "DEF": 15, "PV": 200},
   { "name" : "Thirvaan", "ATK": 18, "DEF": 10, "PV": 100},
   { "name" : "Bruthenkar", "ATK": 22, "DEF": 12, "PV": 150},
   { "name" : "Malavreth", "ATK": 28, "DEF": 18, "PV": 180},
   { "name" : "Sylvakra", "ATK": 15, "DEF": 7, "PV": 90}
]


# Création de la base de donnée et des collections
client = pymongo.MongoClient("mongodb://localhost:27017")
database = client["JEU_MONSTRE"]

def init_db():
    collection_monstres = database["MONSTRES"]
    collection_personnages = database["PERSONNAGES"]
    collection_scores = database["SCORES"]

   #vide la base de données
    collection_personnages.drop()
    collection_monstres.drop()
    collection_scores.drop()


    #Insertion des données dans les différéntes collections
    collection_monstres.insert_many(monstres, bypass_document_validation = True)
    collection_personnages.insert_many(personnages, bypass_document_validation = True)

if __name__ == "__main__":
    init_db()
