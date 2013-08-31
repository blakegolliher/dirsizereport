#!/usr/bin/env python
## 
#
# Based on Rosetta Code recursive dir walk example 
# http://rosettacode.org/wiki/Walk_a_directory/Recursively#Python
#
# Blake Golliher - blakegolliher@gmail.com
#
##

import fnmatch
import sys,os
from math import log

rootPath = sys.argv[1]
pattern = '*'
fullSize = 0

for root, dirs, files in os.walk(rootPath):
    for filename in fnmatch.filter(files, pattern):
        fullpathname = os.path.join(root, filename)
        size = os.path.getsize(fullpathname)
        ## print "SIZE = %s  -> %s" % (size,fullpathname)
        fullSize = fullSize + size

## Thanks internet!
## http://stackoverflow.com/questions/1094841/reusable-library-to-get-human-readable-version-of-file-size
unit_list = zip(['bytes', 'kB', 'MB', 'GB', 'TB'], [0, 0, 1, 2, 2])
def sizeof_fmt(num):
    """Human friendly file size"""
    if num > 1:
        exponent = min(int(log(num, 1024)), len(unit_list) - 1)
        quotient = float(num) / 1024**exponent
        unit, num_decimals = unit_list[exponent]
        format_string = '{:.%sf} {}' % (num_decimals)
        return format_string.format(quotient, unit)
    if num == 0:
        return '0 bytes'
    if num == 1:
        return '1 byte'

print "Whole size of path %s is %s." % (rootPath,sizeof_fmt(fullSize))
