<?php

phpinfo();

/**
 * A User class 
 */
class User(){
	public $username;
	public $address;
	public $email;
	
	/**
	 * Constructor
	 */ 
	public function __construct($username, $address, $email){
		$this->‌username = $username;
		$this->address = $address;
		$this->email = $email;
	}
}



?>