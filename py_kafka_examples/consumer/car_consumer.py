import json
from kafka import KafkaConsumer
from jsonpickle import encode, decode
from mongodb.mongodb_connect import *

consumer = KafkaConsumer("car-topic", bootstrap_servers='localhost:9092', group_id="car-group")

# kafka database creation
db = get_db().kafka

# car collection get or create
car_collection = db.car
for data in consumer:
    document = json.loads(data.value.decode())
    car = decode(document)
    resp = car_collection.insert_one(car.__dict__)
    print(car.__dict__)


