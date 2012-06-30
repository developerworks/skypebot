# -*- coding: utf8 -*-

import amqplib.client_0_8 as amqp
import settings

def main():
	"""
	Send message to amqp server
	"""
    conn = amqp.Connection(host = settings.host)
    ch = conn.channel()
    ch.access_request(settings.virtual_host, active = True, write = True)
    ch.exchange_declare(exchange = settings.exchange_name, type = settings.routing_type, durable = settings.durable, auto_delete = settings.auto_delete)
    retry = True
    while retry:
        msg_body = raw_input('>')
        msg = amqp.Message(msg_body, content_encoding = 'UTF-8')
        msg.properties['delivery_mode'] = 2
        ch.basic_publish(msg, settings.exchange_name, routing_key = settings.routing_key)

        if msg_body == 'quit':
            retry = False
    ch.close()
    conn.close()
if __name__ == '__main__':
    main()
