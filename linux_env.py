#!/usr/bin/env python
# -*- coding:utf-8 -*-
from models import *

class Software(object):
	"""docstring for Software"""
	def __init__(self, *arg):
		self.arg = arg

	def install(self):
		print "start to install software..."
			

def main():
	software = Software()
	software.install()

	bashfile = BashFile()


if __name__ == '__main__':
	bash = MyBashFile()

