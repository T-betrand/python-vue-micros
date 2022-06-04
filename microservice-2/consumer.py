import pika, Json

params = pika.URLParameters('amqps://hkgfggtk:K3l4jg-klZusjlbOHVcIJcGA_LFJCt62@sparrow.rmq.cloudamqp.com/hkgfggtk')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')


def callback(ch, method, prperties, body):
    print('Received from admin')
    print(body)
    data = Json.loads(body)
    print(data)


channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started consumming')

channel.start_consuming()

channel.close()