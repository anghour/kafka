from kafka import KafkaProducer
from models.models import *
import json
from jsonpickle import encode, decode
import time


producer = KafkaProducer(bootstrap_servers="localhost:9092")

car = Car("VOLVO", 10)

while True:
    producer.send("car-topic", json.dumps(encode(car)).encode())
    time.sleep(1)