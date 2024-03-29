import pika, json, time
from main import Product, db

params = pika.URLParameters('amqps://hkgfggtk:K3l4jg-klZusjlbOHVcIJcGA_LFJCt62@sparrow.rmq.cloudamqp.com/hkgfggtk')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')


def callback(ch, method, properties, body):
    print('Received in admin')
    data = json.loads(body)
    print(data)

    if properties.content_type == 'product_created':
        product = Product(id=data['id'], title=data['title'], image=data['image'])
        db.session.add(product)
        db.session.commit()
        print('Product Created')

    elif properties.content_type == 'product_updated':
        product = Product.query.get(data['id'])
        product.title = data['title']
        product.image = data['image']
        db.session.commit()
        print('Product Updated')

    elif properties.content_type == 'product_deleted':
        product = Product.query.get(data)
        db.session.delete(product)
        db.session.commit()
        print('Product Deleted')



channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started consumming')

channel.start_consuming()

channel.close()