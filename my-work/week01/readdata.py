# program that reads a file and takes
# Author: Daniel Finnerty

import csv

FILENAME = "data.csv"
DATADIR = "../week01/"
FULLPATH = DATADIR + FILENAME

'''
# calculate average by converting the string into an integer
with open (FULLPATH, "rt") as fp:
    reader = csv.reader (fp, delimiter=",")
    linecount = 0
    total = 0
    for line in reader:
        if not linecount: # this is the first row (header row)
            # print(f"{line}\n----------")
            pass
        else: # all susequent rows
            total += int(line[1])
        linecount += 1
    print (f"Average is {total/(linecount-1)}")
'''

'''
# using quote parameter to read in the numbers as floats
with open (FULLPATH, "rt") as fp:
    reader = csv.reader (fp, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
    linecount = 0
    total = 0
    for line in reader:
        if not linecount: # this is the first row (header row)
            # print(f"{line}\n----------")
            pass
        else: # all susequent rows
            total += line[1]
        linecount += 1
    print (f"Average is {total/(linecount-1)}")
'''

with open (DATADIR + FILENAME, "rt") as fp: 
    reader = csv.DictReader(fp, delimiter="," , quoting=csv.QUOTE_NONNUMERIC) 
    total = 0 
    count = 0 
    for line in reader: 
        total += line['age'] 
        # print (line) 
        count +=1
    print (f"average is {total/(count)}") # why is there no -1 this time?