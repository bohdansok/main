""" Dic to tab-delimited Dic"""
##Python version 3.85+
##
import os
import os.path
from datetime import datetime

i = 0
#print('XML-файл з ЄДР ФОП має бути у тому ж каталозі, що й файл програми!')
infilename = 'newdict.txt'
inFile = open(infilename, 'r', encoding='cp1251')
infilesize = int(os.path.getsize(infilename))
print('Роботу розпочато', datetime.now())
print('Розмір вхідного файлу', infilesize, " байт. Обробка може забрати.....")
outfilename =  'pydict.txt'
outFile = open(outfilename, 'w', encoding='cp1251')
#print(titlestr, end='\n', file=outFile, flush=False)
mydict = {}
for line in inFile:
	line = line.replace('\n', '')
	mydict[str(line.partition('\t')[0])] = str(line.partition('\t')[2])
	#
print(mydict.items(), file=outFile, end='')
print(type(mydict))
print('Роботу завершено', datetime.now())
print('Done!')
outFile.flush()
outFile.close()
inFile.close()
