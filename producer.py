# importing the required libraries
from time import sleep
from json import dumps
from kafka import KafkaProducer
import logging

# initializing the Kafka producer
my_producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    api_version=(0, 11, 5),
    value_serializer=lambda x: dumps(x).encode('utf-8')
)
logging.basicConfig(level=logging.DEBUG)
# generating the numbers ranging from 1 to 500
for n in range(500):
    my_data = {'num': n}
    my_producer.send('testnum', value=my_data)
    print("here")
    sleep(5)
