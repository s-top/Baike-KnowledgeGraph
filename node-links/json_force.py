#!/usr/bin/env python
# coding:utf8

import sys
reload(sys)
sys.setdefaultencoding('utf8')
import json

nodes = []
links = []
cityList = []
deptList = []
timeList = []
shortList = []
EnnameList = []
friendList = []
#中心节点
nodes.append({'id': '中国', 'class': 'courtry', 'group': 0, 'size': 22})
#城市节点
fr = open('../entity/city.txt', 'r')
for line in fr.readlines():
    tmp = line.strip('\n')
    for key, value in eval(tmp).items():
        str = value.split(' ')[0]
        if str not in cityList:
            cityList.append(str)
            # 城市节点
            nodes.append({'id': str, 'class': 'city', 'group': 1, 'size': 18})
            links.append({'source': '中国', 'target': str, 'value': 3})
            links.append({'source': str, 'target': '中国', 'value': 3})
fr.close()
#创办时间节点
fr = open('../entity/time.txt', 'r')
for line in fr.readlines():
    tmp = line.strip('\n')
    for key, value in eval(tmp).items():
        if value not in timeList:
            timeList.append(value)
            # 创办时间节点
            nodes.append({'id': value, 'class': 'date', 'group': 3, 'size': 13})
fr.close()
#英文名节点
fr = open('../entity/En-name.txt', 'r')
for line in fr.readlines():
    tmp = line.strip('\n')
    for key, value in eval(tmp).items():
        if value not in EnnameList:
            timeList.append(value)
            # 英文名节点
            nodes.append({'id': value, 'class': 'enName', 'group': 4, 'size': 13})
fr.close()
# 知名校友、院系节点
fr = open('../entity/name.txt', 'r')
for line in fr.readlines():
    tmp = line.strip('\n')
    for key, value in eval(tmp).items():
        nodes.append({'id': value + '知名校友', 'class': 'friends', 'group': 5, 'size': 15})
        nodes.append({'id': value + '主要院系', 'class': 'depts', 'group': 6, 'size': 15})
fr.close()
#校友集合
fr = open('../entity/friend.txt', 'r')
for line in fr.readlines():
    tmp = line.strip('\n')
    for key, value in eval(tmp).items():
        name = value.split(' ')
        for friend in name:
            if friend not in friendList:
                friendList.append(friend)
                # 校友节点
                nodes.append({'id': friend, 'class': 'person', 'group': 8, 'size': 11})
fr.close()

#院系集合
fr = open('../entity/dept.txt', 'r')
for line in fr.readlines():
    tmp = line.strip('\n')
    i = 0
    for key, value in eval(tmp).items():
        name = value.split(' ')
        for dept in name:
            if dept not in deptList:
                deptList.append(dept)
                # 院系节点
                nodes.append({'id': dept, 'class': 'person', 'group': 9, 'size': 11})
fr.close()

#简称节点
fr = open('../entity/short.txt', 'r')
for line in fr.readlines():
    tmp = line.strip('\n')
    for key, value in eval(tmp).items():
        if value not in shortList:
            shortList.append(value)
            # 英文名节点
            nodes.append({'id': value, 'class': 'short', 'group': 7, 'size': 13})
fr.close()

fc = open('../entity/all.txt', 'r')
for line in fc.readlines():
    tmp = eval(line.strip('\n'))
    # 学校节点
    nodes.append({'id': tmp['中文名'], 'class': 'school', 'group': 2, 'size': 20})
    links.append({'source': tmp['所属地区'].split(' ')[0], 'target': tmp['中文名'], 'value': 3})
    links.append({'source': tmp['中文名'], 'target': tmp['所属地区'].split(' ')[0], 'value': 3})
    # 时间
    links.append({'source': tmp['中文名'], 'target': tmp['创办时间'], 'value': 3})
    links.append({'source': tmp['创办时间'], 'target': tmp['中文名'], 'value': 3})
    # 英文名
    links.append({'source': tmp['中文名'], 'target': tmp['英文名'], 'value': 3})
    links.append({'source': tmp['英文名'], 'target': tmp['中文名'], 'value': 3})
    # 知名校友节点
    links.append({'source': tmp['中文名'], 'target': tmp['中文名']+'知名校友', 'value': 3})
    links.append({'source': tmp['中文名']+'知名校友', 'target': tmp['中文名'], 'value': 3})
    person = tmp['知名校友'].split(' ')
    for index in person:
        links.append({'source': tmp['中文名']+'知名校友', 'target': index, 'value': 3})
        links.append({'source': index, 'target': tmp['中文名']+'知名校友', 'value': 3})
    # 主要院系节点
    links.append({'source': tmp['中文名'], 'target': tmp['中文名']+'主要院系', 'value': 3})
    links.append({'source': tmp['中文名']+'主要院系', 'target': tmp['中文名'], 'value': 3})
    academy = []
    academy = tmp['主要院系'].split(' ')
    for index in academy:
        links.append({'source': tmp['中文名']+'主要院系', 'target': index, 'value': 3})
        links.append({'source': index, 'target': tmp['中文名']+'主要院系', 'value': 3})
    # 简称节点
    links.append({'source': tmp['中文名'], 'target': tmp['简称'], 'value': 3})
    links.append({'source': tmp['简称'], 'target': tmp['中文名'], 'value': 3})
fc.close()

fw = open('../html/nodes.json', 'w')
fw.write(json.dumps({'nodes': nodes, 'links': links}, encoding='UTF-8', ensure_ascii=False))
fw.close()


