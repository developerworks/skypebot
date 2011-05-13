h1. Getting the real-time debugging info by Skype4Py,Log4php,RabbitMQ

When our web application have error ocurred,i must be logged in server,and tail -f /var/log/daily-$date.log |grep 'somthing'
to find if there is error information about it.

And a new method to getting the debugging message from skype, or from other instant message client ?

Right, we are using Skype now, because our team use it to commulicate with each other. You can use others like xmpp clients,and so on.

h2. Required python modules

* pika (or py-amqp)
* logging
* Skype4Py

You can install those modules by setuptools,about setuptools details you can see the article "Charming Python: Hatch Python eggs with setuptools":http://www.ibm.com/developerworks/linux/library/l-cppeak3/index.html

bc. 

easy_install pika
easy_install logging
easy_install Skype4Py

