#!/usr/bin/env python

import sys

def enable():
    '''
        1. To copy the apt.conf
        
    '''
    print "enable"


def disable():
    print "disable"


if __name__ == '__main__':
	args = sys.argv
	if args[1] == "enable":
		enable()
	else:
		disable()
