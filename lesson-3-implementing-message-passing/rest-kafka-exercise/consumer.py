from kafka import KafkaConsumer


TOPIC_NAME = 'computers'

consumer = KafkaConsumer(TOPIC_NAME)
for message in consumer:
    print (message)
