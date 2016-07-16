#! /usr/bin/env python
#coding=utf-8

import os
import sys
import re
from collections import OrderedDict

reload(sys)
sys.setdefaultencoding('utf8')

result = open('result_hushuli.txt', 'a')

filename = open(u'uid_list_hushuli-全量微博.txt', 'r').readlines()

id_list = open(u'uid_list_hushuli.txt','r').readlines()

#用户字典
uid_dic = OrderedDict({})
for line in id_list:

	uid_dic[line.strip('\n')] = []

for line in filename:

	shangwangfangshi = re.findall(r'新浪	(\d*)	.+?	.+?	.+?	.+?	.+?	.+?	.+?	.+?	(.+?)	.+?	.+?', line)

	if shangwangfangshi and '转发微博' in line:

		message = shangwangfangshi[0]

		#print message[1]

		uid_dic[message[0]].append(message[1])

for uid,item in uid_dic.items() :
	#print len(item)

	quchonglist = len(set(item))

	result.write(uid + ',' + str(quchonglist) + '\n')