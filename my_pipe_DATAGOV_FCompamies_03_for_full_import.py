""" Перетворення  XML-файлу даних про юросіб з ЄДР на структорований текстовий файл, без сміття"""
##Python version 3.85
##
import os
import os.path
from datetime import datetime


## Strigs to find - Start
enddataline = '</SUBJECT>'
frmname_st = '"><NAME>'
frmname_nd = '</NAME><SHORT_NAME'
statut_st = '<AUTHORIZED_CAPITAL>'
statut_nd = '</AUTHORIZED_CAPITAL>'
edrpo_st = '<EDRPOU>'
edrpo_nd = '</EDRPOU>'
actkinds_st = '<ACTIVITY_KINDS>'
actkinds_nd = '</ACTIVITY_KINDS>'
kerivn_st = '<SIGNERS>'
kerivn_nd = '</SIGNERS>'
zasnov_st = '<FOUNDERS>'
zasnov_nd = '</FOUNDERS>'
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
##titlestr = "ЄДРПО" + '\t' + "Назва" + '\t' + "Дата_засн" + '\t' + "Дата_лікв" + '\t' + "Стан"  + '\t' + "Адреса" + '\t' + "Стат_фонд" + '\t' + "КВЕД" + '\t' + "Керівник" + '\t' + "Засновники" + '\t' +  'Дані ЄДР від '
titlestr = "ЄДРПОУ" + '\t' + "Назва" + '\t' + "ОПФ" + '\t' + "Дата_засн" + '\t' + "Дата_лікв" + '\t'
titlestr = titlestr + "Стан"  + '\t' + "Адреса" + '\t'
titlestr = titlestr + "Стат_фонд" + '\t' + "КВЕД" + '\t' + "Керівник" + '\t'
titlestr = titlestr + "Засновник" + '\t' + "Контакт1" + '\t' + "Контакт2"  + '\t' + "Контакт3" + '\t' + "Коментар_дата_ЄДР"
curstr = ''
curstrout = ''
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
    datastr = datastr.replace('\t', '').replace('\n', '')
    datastr = datastr.replace('&quot;', '"').replace('&apos;', "'")
    tempstr = str(datastr.partition(edrpo_st)[2])
    edrpo = str(tempstr.partition(edrpo_nd)[0])
    tempstr = str(datastr.partition(actkinds_st)[2])
    actkinds = str(tempstr.partition(actkinds_nd)[0]).replace('<ACTIVITY_KIND><CODE>', 'КВЕД ')
    actkinds = actkinds.replace('</NAME><PRIMARY>так</PRIMARY>', ' (основний); ')
    actkinds = actkinds.replace('</CODE><NAME>', ' ')
    actkinds = actkinds.replace('</ACTIVITY_KIND>', '')
    actkinds = actkinds.replace('</NAME><PRIMARY>ні</PRIMARY>', ' (додатковий); ')
    tempstr = str(datastr.partition(kerivn_st)[2])
    kerivn = 'Керівництво:' + str(tempstr.partition(kerivn_nd)[0]).replace('<SIGNER>', ' ')
    kerivn = kerivn.replace('</SIGNER>', ';')
    tempstr = str(datastr.partition(zasnov_st)[2])
    zasnov = 'Засновники:' + str(tempstr.partition(zasnov_nd)[0]).replace('<FOUNDER>', ' ')
    zasnov = zasnov.replace('</FOUNDER>', '')
    tempstr = str(datastr.partition(frmname_st)[2])
    name = str(tempstr.partition(frmname_nd)[0])
    tempstr = str(datastr.partition(stdate_st)[2])
    stdate = str(tempstr.partition(stdate_nd)[0])
    tempstr = str(datastr.partition(statut_st)[2])
    statfnd = str(tempstr.partition(statut_nd)[0])
######
    tempstr = str(datastr.partition(opf_st)[2])
    opf = str(tempstr.partition(opf_nd)[0])
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
    outstr = edrpo + '\t' + name + '\t' + opf + '\t' + stdate + '\t' + termdate + '\t'
    outstr = outstr + stan  + '\t' + adresa + '\t'
    outstr = outstr + statfnd + '\t' + actkinds + '\t' + kerivn + '\t'
    outstr = outstr + zasnov + '\t' + cont1 + '\t' + cont2  + '\t' + cont3 + '\t' + 'Дані ЄДР від ' + datasetdate
    outstr = outstr.replace('\n', '')
    return outstr


print('XML-файл з ЄДР ЮО має бути у тому ж каталозі, що й файл програми!')
infilename = input('Введыть повну назву XML-файлу з ЄДР ЮО:')
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
        print(curstrout, end='\n', file=outFile, flush=False)
        curstr = ''
        Linedone = False
    i += 1
print('Роботу завершено', datetime.now())
print('Done!')
outFile.flush()
outFile.close()
inFile.close()
