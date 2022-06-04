import pika, json

params = pika.URLParameters('amqps://hkgfggtk:K3l4jg-klZusjlbOHVcIJcGA_LFJCt62@sparrow.rmq.cloudamqp.com/hkgfggtk')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    # channel.basic_publish(exchange='', routing_key='main', body='hello main')
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)
