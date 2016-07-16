#! /usr/bin/env python
#coding=utf-8

import os
import sys
import re
import time
import datetime

reload(sys)
sys.setdefaultencoding('utf8')

idlist = []

f = open(u'uid.txt', 'r').readlines()

for item in f:

	idlist.append(item.strip())

dicc = {}

result = open('result.txt', 'a')

file1 = open(u'uid_list_gaoji-全量微博.txt', 'r').readlines()
file2 = open(u'uid_list_hushuli-全量微博.txt', 'r').readlines()
file3 = open(u'uid_list_jiangshi-全量微博.txt', 'r').readlines()

filelist = file1 + file2 + file3

print len(filelist)

for i,line in enumerate(filelist):

	message = re.findall(r'新浪	(\d*)	.+?	.+?	.+?	.+?	.+?	.+?	.+?	.+?	.+?	(\d*)	(\d*)', line)

	if message:

		message_tuple = message[0]

		uid = message_tuple[0]

		fans = message_tuple[1]

		follows = message_tuple[2]

		try:

			if uid not in filelist[i + 1]:

				dicc[uid] = [fans, follows]

		except IndexError:

			pass

for item in idlist:

	try:

		fansandfollow = dicc[item]

		try:

			fansfollow = float(fansandfollow[0])/float(fansandfollow[1])

			result.write(item + ',' + fansandfollow[0] + ',' + fansandfollow[1] + ',' + str(fansfollow) + '\n')

		except ZeroDivisionError:

			result.write(item + ',' + fansandfollow[0] + ',' + fansandfollow[1] + ',' + str(10000) + '\n')

	except KeyError:

		result.write(item + ',' + '0' + ',' + '0' + ',' + str(10000) + '\n')