#! /usr/bin/env python
# -*- coding: utf-8 -*-
#爬取百科信息
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import urllib2
import json
from bs4 import BeautifulSoup

#打开网页，获取网页内容
def url_open(url):
    headers = ("user-agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0")
    opener = urllib2.build_opener()
    opener.addheaders = [headers]
    urllib2.install_opener(opener)
    data = urllib2.urlopen(url).read().decode("utf-8","ignore")
    return data
#学校列表
def listSchool(filename):
    data = []
    fr = open(filename, 'r')
    lines = fr.readlines()
    for line in lines:
        data.append(line.strip('\n'))
    fr.close()
    return data
if __name__== '__main__':
    school = listSchool('stopwords.txt')
    result_data = []
    for index in school:
        keywd = index
        keywords = urllib2.quote(keywd)
        url = "https://baike.baidu.com/item/" + keywd
        data = url_open(url)
        soup = BeautifulSoup(data, 'html.parser')
        name_data = []
        value_data = []
        name_node = soup.find_all('dt', class_="basicInfo-item name")
        for i in range(len(name_node)):
            name_data.append(name_node[i].get_text().replace('    ', ''))
        value_node = soup.find_all('dd', class_="basicInfo-item value")
        for i in range(len(value_node)):
            value_data.append(value_node[i].get_text().replace('\n', ''))
        result = {'中文名': '无信息', '英文名': '无信息', '简称': '无信息', '所属地区': '无信息','创办时间': '无信息', '知名校友': '无信息', '主要院系': '无信息'}
        for i in range(len(name_data)):
            if name_data[i] == '中文名':
                result['中文名'] = value_data[i]
            if name_data[i] in ['英文名','外文名']:
                result['英文名'] = value_data[i]
            if name_data[i] == '简称':
                result['简称'] = value_data[i]
            if name_data[i] == '所属地区':
                result['所属地区'] = value_data[i]
            if name_data[i] == '创办时间':
                result['创办时间'] = value_data[i]
            if name_data[i] == '知名校友':
                result['知名校友'] = value_data[i]
            if name_data[i] == '主要院系':
                result['主要院系'] = value_data[i]
        result_data.append({'中文名': result['中文名'], '英文名': result['英文名'], '简称': result['简称'], '所属地区': result['所属地区'],'创办时间': result['创办时间'], '知名校友': result['知名校友'], '主要院系': result['主要院系']})
        print "正在读取"
    fw = open('all.json', 'w')
    fw.write(json.dumps(result_data, encoding='UTF-8', ensure_ascii=False))
    fw.close()
    print("任务完成")