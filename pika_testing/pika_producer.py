# coding=utf-8
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')
for i in range(0,3):
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body=('Hello World!'+str(i)))
    print(" [x] Sent 'Hello World!'"+str(i))
connection.close()
