__author__ = 'jszheng'

import sys

if len(sys.argv)<3 :
    print("Usage: grepworld word infile1 [infile2 [... [infileN]]]")
    sys.exit()

word = sys.argv[1]
for filename in sys.argv[2:]:
    for line_number, line in enumerate(open(filename), start=1):
        if word in line:
            print("{0}:{1}:{2:.40}".format(filename, line_number, line.rstrip()))