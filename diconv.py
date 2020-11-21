""" Dic to tab-delimited Dic"""
##Python version 3.85+
##
import os
import os.path
from datetime import datetime

i = 0
#print('XML-файл з ЄДР ФОП має бути у тому ж каталозі, що й файл програми!')
infilename = 'olddict.txt'
inFile = open(infilename, 'r', encoding='cp1251')
infilesize = int(os.path.getsize(infilename))
print('Роботу розпочато', datetime.now())
print('Розмір вхідного файлу', infilesize, " байт. Обробка може забрати.....")
outfilename =  'newdict.txt'
outFile = open(outfilename, 'w', encoding='cp1251')
#print(titlestr, end='\n', file=outFile, flush=False)
fl_firstcyr = False
cyrcnt = 0
while i < infilesize:
    curstr = str(inFile.read(1))
   # if cyrcnt == 0:
       # print(curstr, end='', file=outFile, flush=False)
    if (curstr in list('1йцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ')) and (cyrcnt == 0):
        cyrcnt += 1
        print('\t' + curstr, end='', file=outFile, flush=False)
        continue
    if (cyrcnt > 0) or (cyrcnt == 0):
        print(curstr, end='', file=outFile, flush=False)
    if curstr == '\n': 
        cyrcnt = 0
i += 1
print('Роботу завершено', datetime.now())
print('Done!')
outFile.flush()
outFile.close()
inFile.close()
