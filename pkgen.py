#!/usr/bin/env python

import os
import ecdsa
import hashlib
import base58
import requests
import time
from smtplib import SMTP_SSL as SMTP
import logging


wif = ""

def ping_address(publicAddress):
	global pk
	global wif
	global publicKey

def wif_conversion(pk):
	global wif
	padding = '80' + pk
	# print padding

	hashedVal = hashlib.sha256(padding.decode('hex')).hexdigest()
	checksum = hashlib.sha256(hashedVal.decode('hex')).hexdigest()[:8]
	# print hashedVal
	# print padding+checksum

	payload = padding + checksum
	wif = base58.b58encode(payload.decode('hex'))
	print wif


while True:

	pk = os.urandom(32).encode("hex")
	wif_conversion(pk)

	sk = ecdsa.SigningKey.from_string(pk.decode("hex"), curve = ecdsa.SECP256k1)
	vk = sk.verifying_key
	publicKey = ("\04" + vk.to_string())
	ripemd160 = hashlib.new('ripemd160')
	ripemd160.update(hashlib.sha256(publicKey).digest())
	networkAppend = '\00' + ripemd160.digest()
	checksum = hashlib.sha256(hashlib.sha256(networkAppend).digest()).digest()[:4]
	binary_address = networkAppend + checksum
	publicAddress = base58.b58encode(binary_address)
	print publicAddress
	#Store the ulr and the public address
	url = 'https://blockchain.info/q/addressbalance/'+publicAddress
	#Check the public address on blockchain.com to see the balance
	req = requests.get(url)
	#In case blockchain.com throws an error for to many requests
	try:
		#Convert the balance returned as an integer
		convert = int(req.content)
		file = open('collection.txt', 'a')
		file.write(wif + '\n' + publicAddress + '\n')
		file.close()
	except ValueError:
		print 'Timeout, lets have a break'
		time.sleep(5)
	#Print the address balance
	print convert
	#If the address balance is more than 0 it creates a file and store public address and balance
	if convert > 0:
	    print 'We found something!'
	    file = open('results.txt', 'a')
	    file.write(wif + '\n' + publicAddress + '\n' + str(convert) + '\n')
	    file.close()
	else:
	    print 'Empty'
