# coding=utf-8
__author__ = 'HD'

import sys
import re
import time
import datetime

reload(sys)
sys.setdefaultencoding('utf8')

# 微博文件
WEIBOFILE = open('weibo.txt', 'r').readlines()

# 生成用户列表

UIDLIST = open('uid.txt', 'r').readlines()


# 大于100话题用户列表
def over100_uid(weibofile):
    over100_list = []

    result_weiboid = []

    result_uid = []

    for line in weibofile:
        weibo_id = re.findall(r'新浪	.+?	+?	.+?	(\d*)	', line)

        if weibo_id:

            over100_list.append(weibo_id[0])

    over100_set = list(set(over100_list))

    for item1 in over100_set:

        if over100_list.count(item1) >= 100:

            result_weiboid.append(item1)

    for line in weibofile:

        cont = re.findall(r'新浪	(\d*)	+?	.+?	(\d*)	', line)

        if cont:

            a = cont[0]

            uid = a[0]

            boid = a[1]

            if boid in result_weiboid:

                result_uid.append(uid)

    return list(set(result_uid))


if __name__ == '__main__':

    over100 = over100_uid(WEIBOFILE)

    result = open('result.txt', 'a')

    for item in UIDLIST:

        if item in over100:

            result.write(item + ',' + 'yes\n')

        else:

            result.write(item + ',' + 'no\n')
