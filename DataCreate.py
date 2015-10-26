#!/usr/bin/env python

import random, os.path
import types
import math
import os
import string
import sys


def main():
	my_file = open("data.txt", "w")
	for x in range(0, 300):
		key_x = ''.join(random.choice(string.ascii_uppercase) for q in range(5))
		key_y = ''.join(random.choice(string.ascii_uppercase) for q in range(5))
		my_mod = random.randint(1,10)
		sign_n = random.randint(1,4)
		if sign_n == 1:
			sign = "+"
		elif sign_n == 2:
			sign = "-"
		elif sign_n == 3:
			sign = "*"
		elif sign_n == 4:
			sign = "/"
		my_file.write(key_x + " " + key_y + " " + str(my_mod) + " " + sign + "\n")
		
if __name__ == "__main__":
	main()