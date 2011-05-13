# Getting the real-time debugging info by Skype4Py,Log4php,RabbitMQ

When our web application have error ocurred,i must be logged inserver,and 

	tail -f /var/log/daily_$date.log |grep 'somthing'

to find if there is error information about it.

And a new method to getting the debugging message from skype, or from
other instant message client ?

Right, we are using Skype now, because our team use it to commulicate
with each other. You can use others like xmpp clients,and so on.

## Setp1. Install required python modules

-   pika (or py-amqp)
-   logging
-   Skype4Py

You can install those modules by setuptools,about setuptools details you
can see the article [Charming Python: Hatch Python eggs with
setuptools](http://www.ibm.com/developerworks/linux/library/l-cppeak3/index.html)

	easy_install pika
	easy_install logging
	easy_install Skype4Py
	
## Setp2. Adding LoggerAppenderRabbitMQ to log4php/appenders directory

## Step3. Setting the log4php.properties file

This is a example:

	; DailyFile
	log4php.appender.dailyfile                          = LoggerAppenderDailyFile
	log4php.appender.dailyfile.layout                   = LoggerLayoutPattern
	;log4php.appender.dailyfile.threshold               = INFO
	
	; For details of Conversion Character
	; See http://logging.apache.org/log4php/apidocs/log4php/layouts/LoggerLayoutPattern.html
	
	log4php.appender.dailyfile.layout.ConversionPattern = "%d{ISO8601} [%p] [%c] %m : %l%n"
	log4php.appender.dailyfile.datePattern              = Ymd
	log4php.appender.dailyfile.file                     = /tmp/daily_%s.log
	
	; Skypebot useing rabbitmq
	log4php.appender.skypebot                           = LoggerAppenderRabbitMQ
	log4php.appender.skypebot.layout                    = LoggerLayoutPattern
	log4php.appender.skypebot.layout.ConversionPattern  = "%d{ISO8601} [%p] %c: %m (at %F line %L)%n"
	log4php.appender.skypebot.host                      = localhost
	log4php.appender.skypebot.port                      = 5672
	log4php.appender.skypebot.user                      = guest
	log4php.appender.skypebot.password                  = guest
	log4php.appender.skypebot.virtualHost               = /
	log4php.appender.skypebot.exchange                  = x.fetch.debugging
	log4php.appender.skypebot.queue 		            = q.fetch.debugging
	log4php.appender.skypebot.routingKey                = r.fetch.debugging

## Step4. Install and Setting the rabbitmq server

About installation and configuration of the rabbitmq server, you can see following links on rabbitmq official site.

* [RabbitMQ Server Installation] (http://www.rabbitmq.com/install.html, "RabbitMQ Server Installation")
* [RabbitMQ Server Configuration] (http://www.rabbitmq.com/configure.html, "RabbitMQ Server Configuration")

## Setp5. Run the  feichio.py deamon and the client send.py 

When the fetchio.py is running, it will connecting to rabbitmq server by configuration of settings.py in src directory.

So please make sure your rabbitmq server is configured correctly before start it.Such as exchange name,queue name,and routing bindings.

Tips:

* About log4php configuration you can see [Apache Log4php Configuration](http://logging.apache.org/log4php/docs/configuration.html, "Apache Log4php Configuration")
* About log4php Layout pattern,you can see [Class LoggerLayoutPattern](http://logging.apache.org/log4php/apidocs/log4php/layouts/LoggerLayoutPattern.html, "Class LoggerLayoutPattern"), if you familier log4j, it's easy.

That's all ! 

__EOF__

