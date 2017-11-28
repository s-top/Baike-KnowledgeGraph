#-*- coding: UTF-8 -*-
import pymysql
import jieba
import sys
import jieba.posseg as pseg
reload(sys)
sys.setdefaultencoding('utf-8')

# 创建停用词list
def stopwordslist(filepath):
   stopwords = {}
   fstop = open(filepath, 'r')
   for eachWord in fstop:
      stopwords[eachWord.strip().decode('utf-8', 'ignore')] = eachWord.strip().decode('utf-8', 'ignore')
   return stopwords
stopwords = stopwordslist('stopwords.txt')
#学校名称
def name(inpath, outpath):
   fr = open(inpath, 'r')
   fw = open(outpath, 'w')
   for line in fr.readlines():
      tmp = line.strip('\n')
      for key, value in eval(tmp).items():
         if key == '中文名':
            fw.write("{'中文名': '" + value +"'}\n")
   fw.close()
   fr.close()
# name('all.txt', 'name.txt')

#简称
def short(inpath, outpath):
   fr = open(inpath, 'r')
   fw = open(outpath, 'w')
   for line in fr.readlines():
      tmp = line.strip('\n')
      for key, value in eval(tmp).items():
         if key == '简称':
            text = ""
            seg_list = pseg.cut(value)  # 默认是精确模式
            for word in seg_list:
               if word.word.strip() != "":
                  if word.word.strip('\n') not in stopwords:
                     if word.word == '大':
                        text = text[:-1] + word.word + ' '
                     else:
                        text = text + word.word + ' '
            fw.write("{'简称': '" + text + "'}\n")
   fw.close()
   fr.close()
# short('all.txt', 'short.txt')

#主要院系
def dept(inpath, outpath):
   fr = open(inpath, 'r')
   fw = open(outpath, 'w')
   for line in fr.readlines():
      tmp = line.strip('\n')
      for key, value in eval(tmp).items():
         if key == '主要院系':
            text = ""
            seg_list = pseg.cut(value)  # 默认是精确模式
            for word in seg_list:
               if word.word.strip() != "":
                  if word.word.strip('\n') in ['、','，']:
                     word.word = '!'
                  if word.word.strip('\n') not in stopwords:
                     if word.word != '!':
                        text = text + word.word
                     else:
                        word.word = ' '
                        text = text + word.word
            fw.write("{'主要院系': '" + text + "'}\n")
   fw.close()
   fr.close()
# dept('all.txt', 'dept.txt')

#创办时间
def getTime(inpath, outpath):
   fr = open(inpath, 'r')
   fw = open(outpath, 'w')
   for line in fr.readlines():
      tmp = line.strip('\n')
      for key, value in eval(tmp).items():
         if key == '创办时间':
            fw.write("{'创办时间': '" + value[0:4] +"年'}\n")
   fw.close()
   fr.close()
# getTime('all.txt', 'time.txt')

#英文名
def getEnglish(inpath, outpath):
   fr = open(inpath, 'r')
   fw = open(outpath, 'w')
   for line in fr.readlines():
      tmp = line.strip('\n')
      for key, value in eval(tmp).items():
         if key == '英文名':
            fw.write("{'英文名': '" + value +"'}\n")
   fw.close()
   fr.close()
# getEnglish('all.txt', 'En-name.txt')

#知名校友
def friend(inpath, outpath):
   fr = open(inpath, 'r')
   fw = open(outpath, 'w')
   for line in fr.readlines():
      tmp = line.strip('\n')
      for key, value in eval(tmp).items():
         if key == '知名校友':
            text = ""
            seg_list = pseg.cut(value)  # 默认是精确模式
            for word in seg_list:
               if word.word.strip() != "":
                  if word.word.strip('\n') in ['、','，']:
                     word.word = '!'
                  if word.word.strip('\n') not in stopwords:
                     if word.word != '!':
                        text = text + word.word
                     else:
                        word.word = ' '
                        text = text + word.word
            fw.write("{'知名校友': '" + text +"'}\n")
   fw.close()
   fr.close()
# friend('all.txt', 'friend.txt')