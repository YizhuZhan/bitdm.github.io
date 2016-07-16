#! /usr/bin/env python
#coding=utf-8

import os
import sys
import re
from collections import OrderedDict

reload(sys)
sys.setdefaultencoding('utf8')

result = open('result_jiangshi.txt', 'a')

filename = open(u'uid_list_jiangshi-全量微博.txt', 'r').readlines()

id_list = open(u'uid_list_jiangshi.txt','r').readlines()

yuanchuang_dic = OrderedDict({})

all_dic = OrderedDict({})

for line in id_list:

	yuanchuang_dic[line.strip('\n')] = 0

	all_dic[line.strip('\n')] = 0
for line in filename:

	#print line

	message = re.findall(r'新浪	(\d*)	', line)

	if message and u'新发布微博' in line :

		yuanchuang_dic[message[0]] += 1

	if message:

		all_dic[message[0]] += 1

for item in id_list:

	try:

		per = float(yuanchuang_dic[item.strip('\n')])/float(all_dic[item.strip('\n')])

		result.write(item.strip('\n') + ',' +str(per) + '\n')

	except ZeroDivisionError,e:

		per = 10000.0

		result.write(item.strip('\n') + ',' +str(per) + '\n')