#!/usr/bin/python2.7
import sys
#if(len(sys.argv)==2)
print("string is  {:^50} ".format(sys.argv[1]));
print("string is  %55s"%(sys.argv[1]));
#else:
#    sys.stderr.write("ERROR [0]\n",format(sys.argv[0]));
