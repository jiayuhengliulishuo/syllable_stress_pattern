#encoding=utf-8
import os
import sys
import pickle
import re
def findSpecial(stringF):
	outPosition=[0]
	for iterS in range(len(stringF)):
		if stringF[iterS]=='.':
			outPosition.append(0)
		if stringF[iterS]==':':
			outPosition.append(1)
	out=[0 for i in range(len(outPosition))]
	#print out
	if len(outPosition)==1:
		out=[]
	elif 1 in outPosition:
		for iteroP in range(len(outPosition)):
			if outPosition[iteroP]==1:
				out[iteroP]=1			
	else:
		out[0]=1
	return out
		
pkl_file=open('./WordList.pkl','rb')
WordList=pickle.load(pkl_file)
#for key in WordList:
#	print (WordList[key])
dict_file='./SmallDict'
dictionary = {}
multWordList={}
for line in open(dict_file).readlines():#按行打开字典文件
	#下面一句是正则表达式，需要查询r是什么意思，\s又是什么意思，
	m = re.match(r'^(\S+)\s+(.*)$', line.strip())#line.strip和文件读入，忽略特殊字符有关系
	#dictionary[m.group(1)] = m.group(2)#又是为什么group可以分开两者，要研究清楚
#	print m.group(1)
#	print m.group(2)
	#print findSpecial(m.group(2))
	if len(findSpecial(m.group(2)))>0:#提取多音节的单词
		multWordList[m.group(1)]=findSpecial(m.group(2))
	#print type(m.group(2))
	#print len(m.group(2))
print len(multWordList)#875个多音节单词
pkl_file=open('./mulWordList.pkl','wb')
pickle.dump(multWordList,pkl_file)
pkl_file.close()
print multWordList
