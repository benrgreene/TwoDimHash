#!/usr/bin/env python

# Author: Ben Greene
# Copyright October 2015

# Object: A two dimensional hash table


import random, os.path
import types
import math
import os
import sys

class TDHash:
	def __init__(self, filename, size = None):
		if size is None:
			size = 499
		self.hash_map = [[[] for x in range(size)] for y in range(size)]
		self.key_list = []
	
	# Given an object, add the object to hash table.
	def add(self, object):
		hash_vals = get_hash(object.key_x, object.key_y)
		self.hash_map[hash_vals[0]][hash_vals[1]].append(object)
		self.key_list.append([object.key_x, object.key_y])
		
	# Given an object, delete the object if it is in the table.
	# Return if the object was in the hash table or not. 
	def delete(self, object):
		hash_vals = get_hash(object.key_x, object.key_y)
		try:
			self.hash_map[hash_vals[0]][hash_vals[1]].remove(object)
			return True
		except ValueError:
			return False
	
	# Given two keys, return the object associated with them.
	# If no object is found, return None
	def get(self, key_x, key_y):
		hash_vals = get_hash(key_x, key_y)
		# Check for collusions 
		for x in range(0, len(self.hash_map[hash_vals[0]][hash_vals[1]])):
			object = self.hash_map[hash_vals[0]][hash_vals[1]][x]
			if object.key_x == key_x and object.key_y == key_y:
				return object
		return None
		
	def get_keys(self):
		return self.key_list
	
# Returns two hash values based on two given strings
def get_hash(key_x, key_y):
	to_return = [0,0]
	prime_mod = 7
	prime_big = 23	
	for c in key_x:
		to_return[0] = (to_return[0] * prime_mod + ord(c)) % prime_big
	for c in key_y:
		to_return[1] = (to_return[1] * prime_mod + ord(c)) % prime_big
	return to_return