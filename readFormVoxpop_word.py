#encoding=utf-8
import sys
import os
import re
import pickle
#定义遍历文件夹的函数，第一个输入是文件夹的路径，第二个输入是要查找的文件
def TraversalFile(rootdir,featurename):
	FileList=[]
	for root,SubFloders,files in os.walk(rootdir):
		for f in files:
			if f.find(featurename)!=-1:
				FileList.append(os.path.join(root,f))
	#			print('found')
	#		else:
	#			print('not found')
	return FileList
WordList=[]#存放和单词文件名
filename='voxpop_word_test.transcript'
for line in open(filename).readlines():#按行从单词文件中提取单词
	tokens = re.split(r'\s+', line.strip())#需要查询一下re.split是什么意思
	#print len(tokens)#tokens 的长度为4
	#print tokens#其中的内容大概是['<s>', 'COLUMN', '</s>', '(5903_engzo_6450_android)']
	WordList.append([tokens[1],tokens[3]])
	#print tokens[1],tokens[3]#第一个是单词，第二个是音频文件名
#print len(WordList)#总共20722个文件
"""
for iter in range(len(WordList)):
	print WordList[iter][1],len(WordList[iter][1])#andrew机器文件名大概是25，ios机器文件名大概是21
"""
FileList=[]
#遍历wav文件，制作成dict
Worddict={}
for WLitem in WordList:
	
	#无后缀版本
	if Worddict.has_key(WLitem[0]):	
		Worddict[WLitem[0]].append(WLitem[1])
	else:
		Worddict[WLitem[0]]=[WLitem[1]]
	"""
	#print TraversalFile('./WavData',WLitem[1][1:len(WLitem[1])-1])	
	if Worddict.has_key(WLitem[0]):	
		Worddict[WLitem[0]].append(TraversalFile('./WavData',WLitem[1][1:len(WLitem[1])-1]))
	else:
		Worddict[WLitem[0]]=[TraversalFile('./WavData',WLitem[1][1:len(WLitem[1])-1])]
	"""
print Worddict
pkl_file=open('./WordList.pkl','wb')
pickle.dump(Worddict,pkl_file)
pkl_file.close()
