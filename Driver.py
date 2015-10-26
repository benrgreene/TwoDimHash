#!/usr/bin/env python

import random, os.path
import math
import os
from TDHash import TDHash
from datetime import datetime
from my_object import my_object


def main():
	my_hash_obj = TDHash(None)
	test_file = open("data.txt", 'r')
	tstart = datetime.now()
	
	for line in test_file:
		line = line.replace('\n', '')
		parts = line.split(' ')
		my_hash_obj.add(my_object(int(parts[2].strip()), parts[0].strip(), parts[1].strip(), parts[3]))
		
	keys = my_hash_obj.get_keys()
	number = 1.0
	for key in keys:
		temp = my_hash_obj.get(key[0].strip(), key[1].strip())
		number = eval(str(number) + " " + temp.sign + " " + str(temp.modifier))
		# print key[0] + "-" + key[1] + "-"
		
	print str(number)
	
	tend = datetime.now()
	print tend - tstart

if __name__ == '__main__':
	main()