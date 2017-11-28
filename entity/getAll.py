#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')
result = {'中文名': '无信息', '英文名': '无信息', '简称': '无信息', '所属地区': '无信息','创办时间': '无信息', '知名校友': '无信息', '主要院系': '无信息'}
name = []
fr = open('name.txt', 'r')
for line in fr.readlines():
    tmp = line.strip('\n')
    for key, value in eval(tmp).items():
        if key == '中文名':
            name.append(value)
fr.close()
city = []
fr = open('city.txt', 'r')
for line in fr.readlines():
    tmp = line.strip('\n')
    for key, value in eval(tmp).items():
        if key == '所属地区':
            city.append(value)
fr.close()
dept = []
fr = open('dept.txt', 'r')
for line in fr.readlines():
    tmp = line.strip('\n')
    for key, value in eval(tmp).items():
        if key == '主要院系':
            dept.append(value)
fr.close()
friend = []
fr = open('friend.txt', 'r')
for line in fr.readlines():
    tmp = line.strip('\n')
    for key, value in eval(tmp).items():
        if key == '知名校友':
            friend.append(value)
fr.close()
Enname = []
fr = open('En-name.txt', 'r')
for line in fr.readlines():
    tmp = line.strip('\n')
    for key, value in eval(tmp).items():
        if key == '英文名':
            Enname.append(value)
fr.close()
time = []
fr = open('time.txt', 'r')
for line in fr.readlines():
    tmp = line.strip('\n')
    for key, value in eval(tmp).items():
        if key == '创办时间':
            time.append(value)
fr.close()
short = []
fr = open('short.txt', 'r')
for line in fr.readlines():
    tmp = line.strip('\n')
    for key, value in eval(tmp).items():
        if key == '简称':
            short.append(value)
fr.close()
fw = open('all.txt', 'w')
for i in range(len(name)):
    fw.write("'"+name[i]+"' : {'中文名': '" + name[i] + "', '英文名': '" + Enname[i] + "', '简称':'" + short[i]+"', '所属地区': '" + city[i] + "', '创办时间': '" + time[i] + "','知名校友': '" + friend[i] + "', '主要院系': '" + dept[i] + "'},")
fw.close()
