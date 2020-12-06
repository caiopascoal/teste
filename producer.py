from kafka import KafkaProducer
import os



producer = KafkaProducer(bootstrap_servers='localhost:9092')
file_name = '/home/ec2-user/test.json'

print(f'File Size is {os.stat(file_name).st_size / (1024 * 1024)} MB')

txt_file = open(file_name)
count = 0
for line in txt_file:
    print(line)
    producer.send('test',line.encode('UTF-8'))
    producer.flush()

txt_file.close()

print(f'Number of Lines in the file is {count}')