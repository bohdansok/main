""" Перетворення  XML-файлу даних про юросіб з ЄДР на структорований текстовий файл, без сміття"""
##Python version 3.85+
##
import os
import os.path
from datetime import datetime


## Strigs to find - Start
enddataline = '</SUBJECT>'
frmname_st = '"><NAME>'
frmname_nd = '</NAME><ADDRESS>'
actkinds_st = '<ACTIVITY_KINDS>'
actkinds_nd = '</ACTIVITY_KINDS>'
stdate_st = '<START_DATE>'
stdate_nd = '</START_DATE>'
opf_st = '<OPF>'
opf_nd = '</OPF>'
adr_st = '<ADDRESS>'
adr_nd = '</ADDRESS>'
stan_st = '<STAN>'
stan_nd = '</STAN>'
term_st = '<TERMINATED_INFO>'
term_nd = '</TERMINATED_INFO>'
cont_st = '<CONTACTS>'
cont_nd = '</CONTACTS>'
## Strigs to find - End
##
## Global vars
datasetdate = '13.11.2020' #  !! Change according to actual date of the dataset
titlestr = "ПІБ" + '\t' + "Дата_засн" + '\t' + "Дата_лікв" + '\t'
titlestr = titlestr + "Стан"  + '\t' + "Адреса" + '\t'
titlestr = titlestr + "КВЕД" + '\t' + "Контакт1" + '\t' + "Контакт2"  + '\t'
titlestr = titlestr + "Контакт3" + '\t' + "Коментар_дата_ЄДР"
curstr = ''
curstrout = ''
##reccnt = 0
i = 0
Linedone = False
## End of Global vars


def tfind(where, what):  # returns True if contains, False - if doesn't
    if where.find(what) == -1:
        result = False
    else:
        result = True
    return result


def procline(datastr):
    cont1 = ''
    cont2 = ''
    cont3 = ''
    ##
    datastr = datastr.replace('\n', '').replace('&apos;', "'")
    datastr = datastr.replace('&quot;', '"').replace('\t', '')
    tempstr = str(datastr.partition(actkinds_st)[2])
    actkinds = str(tempstr.partition(actkinds_nd)[0]).replace('<ACTIVITY_KIND><CODE>', 'КВЕД ')
    actkinds = actkinds.replace('</NAME><PRIMARY>так</PRIMARY>', ' (основний); ')
    actkinds = actkinds.replace('</CODE><NAME>', ' ')
    actkinds = actkinds.replace('</ACTIVITY_KIND>', '')
    actkinds = actkinds.replace('</NAME><PRIMARY>ні</PRIMARY>', ' (додатковий); ')
    tempstr = str(datastr.partition(frmname_st)[2])
    name = str(tempstr.partition(frmname_nd)[0])
    tempstr = str(datastr.partition(stdate_st)[2])
    stdate = str(tempstr.partition(stdate_nd)[0])
    tempstr = str(datastr.partition(adr_st)[2])
    adresa = str(tempstr.partition(adr_nd)[0])
    tempstr = str(datastr.partition(stan_st)[2])
    stan = str(tempstr.partition(stan_nd)[0])
    tempstr = str(datastr.partition(term_st)[2])
    termdate = str(tempstr.partition(term_nd)[0])
    termdate = str(termdate.partition(';')[0])
    tempstr = str(datastr.partition(cont_st)[2])
    contacts = str(tempstr.partition(cont_nd)[0])
    contacts = contacts.replace(' ', '').replace('-', '').replace('(', '')
    contacts = contacts.replace(')', '').replace('+', '')
    if contacts.find(';') != -1:
        cont1 = str(contacts.partition(';')[0])
        cont1 = cont1.replace(',', '')
        cont2 = str(str(contacts.partition(';')[2]).partition(';')[0])
        cont2 = cont2.replace(',', '')
        cont3 = str(str(str(contacts.partition(';')[2]).partition(';')[2]).partition(';')[0])
        cont3 = cont3.replace(',', '')
    if contacts.find(',') != -1:
        cont1 = str(contacts.partition(',')[0])
        cont1 = cont1.replace(',', '')
        cont2 = str(str(contacts.partition(',')[2]).partition(',')[0])
        cont2 = cont2.replace(',', '')
        cont3 = str(str(str(contacts.partition(',')[2]).partition(',')[2]).partition(',')[0])
        cont3 = cont3.replace(',', '')
#
#
    outstr = name + '\t' + stdate + '\t' + termdate + '\t'
    outstr = outstr + stan  + '\t' + adresa + '\t'
    outstr = outstr + actkinds + '\t' + cont1 + '\t' + cont2  + '\t' + cont3 + '\t' + 'Дані ЄДР від ' + datasetdate
    return outstr

print('XML-файл з ЄДР ФОП має бути у тому ж каталозі, що й файл програми!')
infilename = input('Введыть повну назву XML-файлу з ЄДР ФОП:')
inFile = open(infilename, 'r', encoding='cp1251')
infilesize = int(os.path.getsize(infilename))
print('Роботу розпочато', datetime.now())
print('Розмір вхідного файлу', infilesize, " байт. Обробка може забрати кілька годин...")
outfilename = infilename + '.' + datasetdate + '.txt'
outFile = open(outfilename, 'w', encoding='cp1251')
print(titlestr, end='\n', file=outFile, flush=False)
while i < infilesize:
    curstr = curstr + str(inFile.read(1))
    if tfind(curstr, enddataline):
        curstr = curstr.replace(enddataline, '\n')
        Linedone = True
    if Linedone:
        curstrout = procline(curstr)
##        reccnt += 1
##        print(str(reccnt) + '\r' , end='\r' , flush=True)
        print(curstrout, end='\n', file=outFile, flush=False)
        curstr = ''
        Linedone = False
    i += 1
print('Роботу завершено', datetime.now())
print('Done!')
outFile.flush()
outFile.close()
inFile.close()
