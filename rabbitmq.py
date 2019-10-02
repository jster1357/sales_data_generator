#!/usr/bin/env python
import pika

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost',32769,'/',credentials))
channel = connection.channel()
channel.queue_declare(queue='wires')
