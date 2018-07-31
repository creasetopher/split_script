# -*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import re
import datetime
import csv

month = datetime.datetime.now().month
today = datetime.datetime.now().day


driver = webdriver.Chrome()
driver.get('https://linkleadingtointernaltool.com')


f = raw_input('''
     \nA new browser window will open, enter your FB credentials (probably twice). \nPress any key once tool home page has loaded\n
 ''')
raw_data = driver.page_source


res={}


p_data = BeautifulSoup(raw_data, 'html.parser')
tag = p_data.body.div


queues = {
'211210282641172':'q0',
'611377409033562':'q1',
'1737094019886832':'q2',
'1720265718224160':'q3',
'324308627954917':'q4',
'1262648457187303':'q5',
'140458053063402':'q6',
'1675860282737057':'q7',

'948937798567419':'q8',
'163825337380608':'q9',

'266075127121766':'q10',
'1854471258119486':'q11',
'321765094860806':'q12',

'287327145026401':'q13',
'1779966785364563':'q14',

'950091088393640':'q15',
'271371510020735':'q16',
'1763128587236607':'q17',

'368832540266270':'q18',
'1418528984905260':'q19',


'1978633062418488':'q20',
'1949183378703247':'q21',
'1963082020603161':'q22',
'856295201186971':'q23',
'492087294501417':'q24',
'168114917085315':'q25',



'524891794563009':'q26',
'1382008185176931':'q27',
'248425082235073':'q28',


'230749937329182':'q29',


'227978010948732':'q30',
'1629330860714180':'q31',
'234276890323762':'q32',
'1279932455379744':'q33',
'325997517771465':'q34',
'1220761734699384':'q35'
}

main_block = str(tag.find_all('div', limit = 1)[0])
q_pattern = 'q_id=\d+'
cand_pattern = r'''qid=\d+.*"'''  #possible 1 candidate
vol_pattern = ' - </span>.*dsort=' #metric for possible q pattern

cands = re.findall(cand_pattern, main_block)
for a in cands:
    if bool(re.search(q_pattern, a)): #find possible candidate in html div block
        qid = re.search(q_pattern, a).group()
        qid = qid[qid.find('=')+1:]
        if qid in queues: #ensure that qid is one that we want
            if bool(re.search(vol_pattern, a)): #ensure that block contains q metric
                vol_str = re.search(vol_pattern, a)
            if bool(vol_str):
                vol_str = re.findall('\d+', vol_str.group())
                if len(vol_str) < 1:
                    vol_str = ['0']
                res[queues[qid]] = vol_str[-1]


a = [
    '948937798567419',
    '163825337380608',
    '211210282641172',
    '266075127121766',
    '1854471258119486',
    '321765094860806',
    '287327145026401',
    '1779966785364563'
    ]


b = [
    '611377409033562',
    '1737094019886832',
    '1720265718224160',
    '324308627954917',
    '1262648457187303',
    '140458053063402',
    '1675860282737057',
    '1779966785364563'
    ]


c = [
    '950091088393640',
    '271371510020735',
    #'1763128587236607'
    ]


d = [
    '1978633062418488',
    '1949183378703247',
    '1963082020603161',
    '856295201186971',
    '492087294501417',
    '168114917085315'
    ]

e = [
    '1382008185176931',
    #'248425082235073',
    '140458053063402',
    '1675860282737057',
    '1720265718224160',
    ]
with open ('split_csv.csv', 'wb') as split_csv:
    split_writer = csv.writer(split_csv, delimiter=',')

    print 'A ↓ \n'
    for q in a:
        print queues[q] + ': ' + res[queues[q]]
        split_writer.writerow([queues[q], res[queues[q]]])
        print '\n' + '\n'


    print 'B ↓ \n'
    for q in b:
        print queues[q] + ': ' + res[queues[q]]
        split_writer.writerow([queues[q], res[queues[q]]])
        print '\n' + '\n'

    print 'C ↓ \n'
    for q in c:
        if q in res[queues[q]] and q in queues:
            print queues[q] + ': ' + res[queues[q]]
            split_writer.writerow([queues[q], res[queues[q]]])
            print '\n' + '\n'

    print 'D ↓ \n'
    for q in d:
        print queues[q] + ': ' + res[queues[q]]
        split_writer.writerow([queues[q], res[queues[q]]])
        print '\n' + '\n'

    print 'E ↓ \n'
    for q in e:
        print queues[q] + ': ' + res[queues[q]]
        split_writer.writerow([queues[q], res[queues[q]]])
        print '\n' + '\n'
