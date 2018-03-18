import json
from kafka import KafkaConsumer
from mongodb.mongodb_connect import *

consumer = KafkaConsumer("titanic-topic", bootstrap_servers='localhost:9092', group_id="titanic-group")

# kafka database creation
db = get_db().titanic

# passenger collection creation
passenger_collection = db.passenger
for data in consumer:
    passenger = json.loads(data.value.decode())
    resp = passenger_collection.insert_one(passenger)
    print(passenger)


