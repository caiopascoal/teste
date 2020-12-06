from kafka import KafkaProducer
from json import dumps, loads, load


producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda
   K:dumps(K).encode('utf-8'))

with open('/home/ec2-user/test.json') as file:
    reader = load(file)
    for msg in reader:
        producer.send('quickstart-events',msg)
        producer.flush()