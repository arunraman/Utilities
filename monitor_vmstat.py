#!/usr/bin/python
__author__ = 'arunraman'

import sys

def read_vmstat(column_num,repeat,threshold):
    for linenum,line in enumerate(sys.stdin):
        if linenum == 2:
            l = line.split()
            if repeat != 0:
                if l[column_num - 1] > threshold :
                    repeat -= 1
                    print "Threshold reached!!"
                    break

def Main():
    column_number = int(sys.argv[1])
    repeat = int(sys.argv[2])
    threshold = int(sys.argv[3])
    read_vmstat(column_number,repeat,threshold)

if __name__ == '__main__':
    Main()
