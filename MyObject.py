#!/usr/bin/env python

# Author: Ben Greene
# Copyright October 2015

import random, os.path
import types
import math
import os
import sys

class MyObject:
	def __init__(self, modifier, key_x, key_y, sign):
		self.modifier = modifier
		self.key_x = key_x
		self.key_y = key_y
		self.sign = sign