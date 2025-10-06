# program that reads a file and takes
# Author: Daniel Finnerty

FILENAME= "numbers.txt"
DATADIR= "../week01/"
FULLPATH= DATADIR + FILENAME

print (FULLPATH)

with open (FULLPATH, "rt") as fp:
    total = 0
    for line in fp:
        #print (f" {line} has length {len(line)}")
        total += int(line)
    print (total)