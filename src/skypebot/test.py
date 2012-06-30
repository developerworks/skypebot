# -*- coding: utf8 -*-

import Skype4Py
import pika
import settings

class Fetching:
    def __init__(self):
        settings.logger.info("INIT")
        self.connection = None
        self.channel = None

    """
    Send a message to Skype
    @param self: 
    @param message:  A message to send to skype client on current system.
    """
    def sendToSkype(self, message):
        ''

    def run(self):
        settings.logger.info("RUN")
        # Connect to rabbitmq server
        self.connection = pika.AsyncoreConnection(
                pika.ConnectionParameters(settings.host, settings.port, settings.virtual_host
                )
        )
        settings.logger.debug("Build a connection to rabbitmq by %s, %s, %s" % (settings.host, settings.port, settings.virtual_host))

        self.channel = self.connection.channel()

        settings.logger.debug("get a channel")

        # Create exchange if not exist
        self.channel.exchange_declare(exchange = settings.exchange_name, type = settings.routing_type, durable = settings.durable)
        settings.logger.debug("Exchange %s declared", settings.exchange_name)
        # Create queue if not exist
        self.channel.queue_declare(
                queue = settings.queue_name,
                durable = settings.durable,
                auto_delete = settings.auto_delete
                )
        settings.logger.debug("Queue %s declared." % settings.queue_name)
        # Binding exchange and queue with routing key
        self.channel.queue_bind(exchange = settings.exchange_name, queue = settings.queue_name, routing_key = settings.routing_key)
        settings.logger.debug("Binding queue %s to exchagge %s with routing key %s" % (settings.queue_name, settings.exchange_name, settings.routing_key))

        self.channel.basic_qos(prefetch_count = settings.prefetch_count)
        self.channel.basic_consume(self.callback, queue = settings.queue_name, no_ack = settings.no_ack)
        pika.asyncore_loop()

    def callback(self, ch, method, properties, body):
        settings.logger.info("calling callback function .....")
        if settings.participants.count > 0:

            # Attrach to skype
            settings.logger.debug("Initialize the skype object")
            self.skype = Skype4Py.skype.Skype()
            self.client = self.skype.Client
            if not self.client.IsRunning:
                settings.logger.debug("Skype is not runing, starting .....")
                self.client.Start(Minimized = True, Nosplash = True)
                settings.logger.debug("Skype started.")

            self.skype.OnAttachmentStatus = self.OnAttach
            self.skype.OnMessageStatus = self.OnMessageStatus
            self.skype.Attach()

            for p in settings.participants:
                self.skype.SendMessage(p, body)
                settings.logger.debug("MESSAGE SENT: [%s] %s" % (p, body,))

    def OnAttach(self, status):
        if status == Skype4Py.apiAttachAvailable:
            self.skype.Attach()
        if status == Skype4Py.apiAttachSuccess:
            ''
    def OnMessageStatus(self, message, status):
        if status == Skype4Py.cmsReceived:''
        elif status == Skype4Py.cmsRead:''
        elif status == Skype4Py.cmsSending:''
        elif status == Skype4Py.cmsSent:''
        elif status == Skype4Py.cmsUnknown:''

if __name__ == '__main__':
    f = Fetching()
    f.run()
