from kafka import KafkaConsumer
consumer = KafkaConsumer('quickstart-events', bootstrap_servers='localhost:9092', api_version=(0,10))
for msg in consumer:
    print(msg)