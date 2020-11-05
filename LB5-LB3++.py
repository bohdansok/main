import os
import sys
import csv
import linecache
import time

filename = 'Students01.txt'
sortedfile = 'Student_sorted.txt'
fd = open(filename, 'r+', encoding='UTF-8')
reader = csv.reader(fd, delimiter =";")
sort = sorted(reader, key=lambda reader: reader[1], reverse=True)
print(sort)
sd = open(sortedfile, 'w', encoding='UTF-8')
a = 0
while a < len(sort):
    line = str(sort[a][0]) + ';' + str(sort[a][1])
    print(line, end="\n", file=sd, flush=True)
    print(line)
    a+=1
sd.flush()
sd.close()
fd.close()

time.sleep(1.00)

cline = linecache.getline(filename, 2)
print('\n',cline)
for filename in os.listdir("..\\"):
   print(filename)
        

    
