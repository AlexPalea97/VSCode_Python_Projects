import pymongo
from pymongo import MongoClient


# eseguo la connessione con mongodb
client = MongoClient('localhost', 27017)

# creo un database e lo chiamo testdb
db = client.testdb

# creo la collection persone
persone_coll = db.persone

persone_coll.create_index([('nome', pymongo.ASCENDING)])
persone_coll.create_index([('cognome', pymongo.ASCENDING)])
persone_coll.create_index([('computer', pymongo.ASCENDING)])

# creo un documento
data1 = {
    'nome':'Alex',
    'cognome':'Palea',
    'età': 25,
    'computer': ['lenovo', 'apple']
}

# inseriamo il documento in mongodb
persone_coll.insert_one(data1)


# creo un documento
data2 = {
    'nome':'John',
    'cognome':'Locke',
    'età': 33,
    'computer': ['asus']
}

# inseriamo il documento in mongodb
persone_coll.insert_one(data2)


# creo un documento
data3 = {
    'nome':'Jessy',
    'cognome':'Owens',
    'età': 27,
    'computer': ['dell', 'apple']
}

# inseriamo il documento in mongodb
persone_coll.insert_one(data3)


d1 = persone_coll.find_one()
print(d1)

print('==========')
comp_model = persone_coll.find({'computer': 'apple'})
for pc in comp_model:
    print(pc)

print('==========')
change = persone_coll.update_one({'nome': 'John'}, {'$set': {'età': 34}})
d1_changed = persone_coll.find_one({'nome': 'John'})
print(d1_changed)

print('==========')
selected_data = persone_coll.find_one({'nome': {'$gt': 'Alex'}})
print(selected_data)