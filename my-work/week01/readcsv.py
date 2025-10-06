# program that reads a file and takes
# Author: Daniel Finnerty
import csv

FILENAME= "students.csv"
DATADIR= "../week01/" #each ".." goes up 1 level
FULLPATH= DATADIR + FILENAME

'''
with open (FULLPATH, "rt") as fp:
    for line in fp:
        print(line, end="")
'''

'''
with open (FULLPATH, "rt") as fp:
    reader = csv.reader(fp, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)  #You can change the text after QUOTE
    total = 0
    linenumber = 0
    for line in reader:
        if linenumber: # is not the header (line 0)
            #print (line)
            total += int(line[1]) # the ages have quotes so are read in as strings
        else: # is the header
            print (line)
        linenumber += 1
    print (total)
'''

import pandas
df = pandas.read_csv(DATADIR + FILENAME)
print(df)
