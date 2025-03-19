import json
from flask import Flask, jsonify, request, Response
from kafka import KafkaProducer

from .services import retrieve_orders, create_order

TOPIC_NAME = 'computers'
KAFKA_SERVER = 'localhost:9092'
producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)

app = Flask(__name__)


@app.route('/health')
def health():
    return jsonify({'response': 'Hello World!'})


@app.route('/api/orders/computers', methods=['GET', 'POST'])
def computers():
    if request.method == 'GET':
        return jsonify(retrieve_orders())
    elif request.method == 'POST':
        request_body = request.json
        #print(request_body)
        producer.send(TOPIC_NAME, bytes(str(request_body), 'utf-8'))
        producer.flush()
        #return jsonify(create_order(request_body))
        return Response(status=202)
    else:
        raise Exception('Unsupported HTTP request type.')

@app.route('/api/v2/orders/computers', methods=['GET', 'POST'])
def computersV2():
    if request.method == 'GET':
        return jsonify(retrieve_orders())
    elif request.method == 'POST':
        request_body = request.json
        #print(request_body)
        producer.send(TOPIC_NAME, bytes(str(request_body), 'utf-8'))
        producer.flush()
        #return jsonify(create_order(request_body))
        return Response(status=202)
    else:
        raise Exception('Unsupported HTTP request type.')


if __name__ == '__main__':
    app.run()

