from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers=['54.237.114.47:9092'], api_version=(0,10))
producer.send('quickstart-events', b'a')
#producer.flush()