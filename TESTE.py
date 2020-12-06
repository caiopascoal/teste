#import json

#with open('D:/download/yelp_academic_dataset_review.json','r') as file:
#    data = json.load(file)
#    print(data[0])

from kafka import KafkaConsumer
consumer = KafkaConsumer('quickstart-events', bootstrap_servers=['54.237.114.47:9092'], api_version=(0,10))
for msg in consumer:
    print("Topic Name=%s,Message=%s" % (msg.topic, msg.value))