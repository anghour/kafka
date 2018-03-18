from kafka import KafkaProducer
import json


import pandas as pd

import time

producer = KafkaProducer(bootstrap_servers="localhost:9092")

data = pd.read_csv('local_data/train.csv')

json_data = json.loads(data.to_json(orient='records'))

print(len(json_data))

for passenger in json_data:
    producer.send("titanic-topic", json.dumps(passenger).encode())
    print('SENT PASSENGER => {}'.format(passenger))

    time.sleep(0.001)
