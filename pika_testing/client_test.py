# coding=utf-8
import pika
import threading

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print(" [x] inside recd Received %r" % body)

q = []

queue = channel.basic_get(
   queue='hello', auto_ack=True)
print('this is what queue contains')
for i in queue:
    print (i)
q.append(queue)
print(queue[2])

while queue[2] != None:
    queue = channel.basic_get(
            queue='hello', auto_ack=True)
    q.append(queue[2])
    print(queue[2])
print("..........................")
