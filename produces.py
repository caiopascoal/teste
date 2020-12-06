from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:9092')

with open('/home/ec2-user/test.json') as file:
    producer.send('quickstart-events', file.flush())
    producer.flush()