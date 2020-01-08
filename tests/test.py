# This is an automated test file to check the validity of a buch of known
# addresses contained in test.txt
# Some of those addresses contain balances.
# The test is used to verify the validity of the response from blockchain.com

#!/usr/bin/env python

import os
import requests
import time
import logging

file = open('test.txt')
lines = file.readlines()

for line in lines:
    print line
    #Store the ulr and the public address
    url = 'https://blockchain.info/q/addressbalance/'+line
	#Check the public address on blockchain.com to see the balance
    req = requests.get(url)
	#In case blockchain.com throws an error for to many requests
    try:
		#Convert the balance returned as an integer
        convert = int(req.content)
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
