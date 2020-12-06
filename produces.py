from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:9092')

producer.send('quickstart-events','/home/ec2-user/test.json')
producer.flush()