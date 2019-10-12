#!/usr/bin/env python3
import sys
import re
import csv

if (len(sys.argv)==1) or (sys.argv[1] == "-h") :
    print("""\
    Usage: textcount.py [OPTIONS]
         -h                      Display this usage message
         -t textfile             input text file
         -n numberfile           input number file
    """)
    sys.exit()

print ("running...")

startpos = 0

#print (*sequence)

#read in text file
tcontents = ""
if sys.argv[1] == "-t":
    filename = sys.argv[2]
    f = open(sys.argv[2], "r")
    if f.mode =='r':
        tcontents=f.read()
        print (tcontents)

        # remove whitespace
        tcontents = tcontents.replace(" ", "")
        tcontents = tcontents.replace("\n", "")

        if startpos != 0:
            tcontents = tcontents[startpos:]

        # remove puncutation
        tcontents = re.sub('[.,\']', '', tcontents)
        tcontents = re.sub('[:;-]', '', tcontents)

        print ("\n\n" + tcontents)

# read in number file
sequence = []
if sys.argv[3] == "-n":
    with open(sys.argv[4], newline='') as csvfile:
        arrays = list(csv.reader(csvfile))
        print (arrays)

        #combine all rows into one array
        for x in arrays:
         for y in x:
           sequence.append(y)

        print (sequence)

        # compute result
        result = ""
        for c in sequence:
          ci = int(c)
          print ("\n", ci, len(tcontents))
          if (ci < len(tcontents)):
            result += tcontents[ci-1]
          else:
            result += "^"
        print ("\n\n" + result)
