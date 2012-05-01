#!/usr/bin/env python



class BashFile(object):
	"""docstring for BashFile
	This class is to operate the BashFile
	The file location is ~/.bashrc
	"""
	def __init__(self, *arg):
		super(BashFile, self).__init__()
		self.arg = arg


	def add_property(self,key,value):
		pass


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
	main()
