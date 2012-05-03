#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
class Property():
	'''
	This class is to handle property file
	'''
	REPLACE_MODE=1
	APPEND_MODE=2
	NOMAL_MODE=0
	
	def __init__(self,filePath):
		self.re={}
		self.file=filePath
		pf = open(filePath)   # open file
		for line in pf:   # go through the line
			print line
			tmp = line.split("=",1)   #split using ��=��
			self.re[tmp[0]] = tmp[1]  
			del line
		pf.close()
		
	def add_pro(self,key,value,mode):
		if mode==Property.NOMAL_MODE or mode==None:
			if key in self.re.keys():
				print key+" is already existing. Exit."
				sys.exit()
			else:
				pro = open(self.file,"a")
				pro.write(key+"="+value+ "\n")
				pro.close()
				
		if mode==Property.APPEND_MODE:
			pro = open(self.file,"a")
			pro.write(key+"="+value+ "\n")
			pro.close()

		#TODO add part about REPLACE mode
		
		
	def remove_pro(self,key, value):
		pass
	
	
class BashFile(Property):
	"""docstring for BashFile
	This class is to operate the BashFile
	The file location is ~/.bashrc
	"""
	def __init__(self, *arg):
		super().__init__()
		self.arg = arg

	def add_alias(self,name,value):
		pass


	def add_path(self,path):
		pass


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
	import os
	print os.linesep
	pro = Property("c:\\test.txt")
	pro.add_pro("test", "value")
#	main()
