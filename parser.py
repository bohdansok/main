import os.path


def tfind(where, what):
            if where.find(what)  != -1:
                     result = True
            else:
            	result = False
            return result
    
infn = "redhoodgirl.txt"
ss = "бабушка"
i = 0
infile = open(infn, "rt")
curstr = ""
while i < os.path.getsize(infn):
   curstr = curstr + infile.read(1)
   if tfind(curstr, ss):
   	print(i)
   	curstr = ""
   i += 1
infile.close()