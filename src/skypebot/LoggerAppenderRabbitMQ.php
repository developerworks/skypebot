<?php
/**
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
 * @package log4php
 */
/**
 * Appender for writing to RabbitMQ
 *
 * @author Zhiqiang,He <developerworks@163.com>
 * @version $$
 * @subpackage appenders
 * @since 2.1
 */
class LoggerAppenderRabbitMQ extends LoggerAppender {

	private $host;
	private $port;
	private $virtual_host;
	private $user;
	private $password;
	private $exchange;
	private $queue;
	private $routing_key;
	private $routing_type;
	private $durable;
	private $auto_delete;
	private $prefetch_count;
	
	private $append;

	/**
	 * @var AMQPConnection
	 */
	private $connection;
	
	/**
	 * @var AMQPChannel
	 */
	private $channel;

	public function __construct($name = '') {
		parent::__construct($name);
	}
	public function __destruct() {
		$this->close();
	}

	/**
	 * Build a rabbitmq connection.
	 * 
	 * @return boolean true if all ok.
	 * @throws an Exception if the attempt to connect to the requested rabbitmq server fails.
	 */
	public function activateOptions() {
		try{
			$this->connection = new AMQPConnection($this->host, $this->port, $this->user, $this->password);
			$this->channel = $this->connection->channel();
			
//			$this->channel->exchange_declare($this->exchange, $this->routing_type, false, false, false);
//			$this->channel->queue_declare($this->queue, false, false, false, false);
//			$this->channel->queue_bind($this->queue, $this->exchange, $this->routing_key);
		}
		catch(AMQPConnectionException $ce){
			$this->append = false;
		}
		catch(AMQPChannelException $che){
			$this->append = false;
		}
		$this->append = true;
		return true;
	}
	
	/**
	 * Appends a new event to rabbitmq message queue
	 * @throws LoggerException If the publish message fails.
	 */
	public function append(LoggerLoggingEvent $event) {
        if($this->connection && $this->layout !== null && $this->append == true) {
        	try{
        		$this->channel->access_request($this->virtual_host, false, false, true, true);
	        	$message = $this->getLayout()->format($event);
	        	$msgObject = new AMQPMessage(json_encode($message),array(
	        	      'content_type' => 'text/plain'
	        	));
	        	$this->channel->basic_publish($msgObject, $this->exchange, $this->routing_key);
        	}
        	catch(LoggerException $e){}
        }
	}
	
	public function close() {
		if($this->closed != true) {
            if($this->channel != null){
            	$this->channel->close();
            	$this->channel = null;
            }
            if($this->connection != null){
                $this->connection->close();
                $this->connection = null;	
            }
            $this->closed = true;
		}		
	}
	
	public function getHost() {
		return $this->host;
	}
	
	public function setHost($host) {
		$this->host = $host;
	}
	
	public function getPort() {
		return $this->port;
	}
	
	public function setPort($port) {
		$this->port = $port;
	}
	
	public function getVirtualHost() {
		return $this->virtual_host;
	}
	public function setVirtualHost($virtual_host) {
		$this->virtual_host = $virtual_host;
	}
	
	public function getUser() {
		return $this->user;
	}
	
	public function setUser($user) {
		$this->user = $user;
	}
	
	public function getPassword() {
		return $this->password;
	}
	
	public function setPassword($password) {
		$this->password = $password;
	}
	
	public function getExchange() {
		return $this->exchange;
	}
	
	public function setExchange($exchange) {
		$this->exchange = $exchange;
	}
	
	public function getQueue() {
		return $this->queue;
	}
	
	public function setQueue($queue) {
		$this->queue = $queue;
	}
	
	public function getRoutingKey() {
		return $this->routing_key;
	}
	
	public function setRoutingKey($routing_key) {
		$this->routing_key = $routing_key;
	}
	
	public function getRoutingType(){
		return $this->routing_type;
	}
	
	public function setRoutingType($routing_type){
		$this->routing_type = $routing_type;
	}
	
	public function getDurable() {
		return $this->durable;
	}
	
	public function setDurable($durable) {
		$this->durable = $durable;
	}
	
	public function getAutoDelete() {
		return $this->auto_delete;
	}
	
	public function setAutoDelete($auto_delete) {
		$this->auto_delete = $auto_delete;
	}
	
	public function getPrefechCount() {
		return $this->prefetch_count;
	}
	
	public function setPrefetchCount($prefetch_count) {
		$this->prefetch_count = $prefetch_count;
	}
	
	public function getAppend(){
		return $this->append;
	}
	
	public function setAppend($append){
		$this->append = $append;
	}
	
	public function getConnection(){
		return $this->connection;
	}
	
	public function getChannel(){
		return $this->channel;
	}
}
?>