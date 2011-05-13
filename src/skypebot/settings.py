# -*- coding: utf8 -*-

import logging

# RabbitMQ Settings

host = 'localhost'
port = 5672
virtual_host = '/'

exchange_name = 'x.fetch.debugging'
queue_name = 'q.fetch.debugging'
routing_key = 'r.fetch.debugging'
routing_type = 'direct'

durable = True
auto_delete = False
prefetch_count = 1
no_ack = True

# Who will recive the debugging informations
# If you wannt add more participants,you can append it below
participants = []
participants.append('bluest.org')
#participants.append('alnany')
#participants.append('vuleetu')
#participants.append('bizrsolson')


# create logger
logger = logging.getLogger('FETCHIO')
logger.setLevel(logging.DEBUG)
# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# add formatter to ch
ch.setFormatter(formatter)
# add ch to logger
logger.addHandler(ch)
