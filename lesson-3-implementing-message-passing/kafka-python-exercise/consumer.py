from kafka import KafkaConsumer


TOPIC_NAME = 'order'

consumer = KafkaConsumer(TOPIC_NAME)
for message in consumer:
    print (message)
