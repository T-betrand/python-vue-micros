import pika, time

params = pika.URLParameters('amqps://hkgfggtk:K3l4jg-klZusjlbOHVcIJcGA_LFJCt62@sparrow.rmq.cloudamqp.com/hkgfggtk')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(db, method, prperties, body):
    print('Received in admin')
    print(body)
    


channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started consumming')

channel.start_consuming()

channel.close()