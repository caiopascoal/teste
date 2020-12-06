from kafka import KafkaProducer
from json import dumps, loads, load
import pandas as pd

import resource
import os

file_name = '/home/ec2-user/test.json'

print(f'File Size is {os.stat(file_name).st_size / (1024 * 1024)} MB')


#producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda
#   K:dumps(K).encode('utf-8'))
#total = 0

#for chunk in pd.read_json('/home/ec2-user/test.json', chunksize=1000, lines=True):
#    print(chunk)
#    total += sum(chunk['x'])
#    for msg in chunk:
#        print(msg)
#        producer.send('quickstart-events',msg)
#        producer.flush()
#print(total)