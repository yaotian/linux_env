#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import os
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
	
	
class MyBashFile(Property):
	"""docstring for BashFile
	This class is to operate the BashFile
	The file location is ~/.bashrc
	"""
	def __init__(self, fileName=None):
		homedir = os.path.expanduser('~')
		if fileName==None:
			fileName=homedir+os.sep+".bashrc"
		super(fileName)


	def add_alias(self,name,value):
		self.add_pro(name,value)


	def add_path(self,path):
		pass


class ClassName(object):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg
		