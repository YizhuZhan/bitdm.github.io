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

result = open('result_jiangshi.txt', 'a')

filename = open(u'uid_list_jiangshi-全量微博.txt', 'r').readlines()

id_list = open(u'uid_list_jiangshi.txt','r').readlines()

user_dic = OrderedDict({})

for line in id_list:

	user_dic[line.strip('\n')] = []

for line in filename:

	shangwangfangshi = re.findall(r'新浪	(\d*)	.+?	.+?	.+?	(.+?)	.+?	.+?	.+?	.+?	.+?	.+?	.+?', line)

	if shangwangfangshi and '转发微博' in line:

		message = shangwangfangshi[0]

		#print message[1]

		user_dic[message[0]].append(message[1])

for uid,item in user_dic.items() :

	try:

		distance = len(item)

		start_time = datetime.datetime.strptime(item[0],"%Y-%m-%d %H:%M:%S")

		end_time = datetime.datetime.strptime(item[-1],"%Y-%m-%d %H:%M:%S")

		fren = float(distance)/(time.mktime(end_time.timetuple()) - time.mktime(start_time.timetuple()) + 1.0)
		#print distance,fren

		result.write(uid + ',' + str(fren*3600) + '\n')

	except IndexError or ZeroDivisionError,e:

		result.write(uid + ',' +'0' + '\n')