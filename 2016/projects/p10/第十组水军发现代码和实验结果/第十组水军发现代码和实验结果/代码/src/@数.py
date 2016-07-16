#! /usr/bin/env python
#coding=utf-8

import os
import sys
import re
import time
import datetime
from collections import OrderedDict

reload(sys)
sys.setdefaultencoding('utf8')

result = open('result_hushuli.txt', 'a')

filename = open(u'uid_list_hushuli-全量微博.txt', 'r').readlines()

id_list = open(u'uid_list_hushuli.txt','r').readlines()

user_dic = OrderedDict({})

for line in id_list:

	user_dic[line.strip('\n')] = []

for line in filename:

	uid = re.findall(r'新浪	(\d*)	', line)

	if uid and '转发微博' in line:

		user_dic[uid[0]].append(line.count('@'))

def add(x,y):

	return x+ y
for uid,item in user_dic.items():

	try:

		aaa = sum(item)

		result.write(uid + ',' + str(float(aaa)/float(len(item))) + '\n')

	except ZeroDivisionError:

		result.write(uid + ',' + str('0') + '\n')