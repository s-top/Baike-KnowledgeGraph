#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import json
reload(sys)
sys.setdefaultencoding('utf8')
#将学校名称转为序列
def schoolName2str(filename):
    data = []
    fr = open(filename, 'r')
    lines = fr.readlines()
    for line in lines:
        data.append(line.strip('\n'))
    fr.close()
    fw = open('school.txt', 'w')
    for i in data:
        fw.write("'" + i + "',")
    fw.close()
    print filename + " 完成"
#获取城市
def getCity(filename):
    result = {'所属地区': '无信息', '中文名': '无信息'}
    fr = open(filename, 'r')
    fw = open('city-name.txt', 'w')
    for line in fr.readlines():
        tmp = line.strip('\n')
        for key, value in eval(tmp).items():
            if key == '所属地区':
                result['所属地区'] = value
                # print result['所属地区']
            if key == '中文名':
                result['中文名'] = value
        fw.write("{'所属地区': '" + result['所属地区'] + "', '中文名': '" + result['中文名'] + "'}\n")
    fr.close()
    fw.close()
    print "写入完毕"
# schoolName2str('../loadingData/stopwords.txt')
getCity('../loadingData/all.txt')
