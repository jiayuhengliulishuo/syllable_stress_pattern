#encoding=utf-8
import os
import json
import sys
import os
import pickle
import numpy 
def list2mean(list1):
	N=len(list1)
	#listn=float(list1)
	listn=list1
	narray=numpy.array(listn)
	sum1=narray.sum()
	mean=float(sum1)/float(N)
	return mean
def list2var(list1):
	N=len(list1)
	#listn=float(list1)
	listn=list1
	narray=numpy.array(listn)
        sum1=narray.sum()
	mean=float(sum1/N)
	narray2=narray*narray
	sum2=narray2.sum()
	var=float(sum2/N-mean**2)
	return var
def pitch2feature(pitchVals):
	pitchmax=max(pitchVals)
	pitchmin=min(pitchVals)
	pitchmean=list2mean(pitchVals)
	pitchstd=list2var(pitchVals)
	pitchlen=len(pitchVals)
	out=[pitchmax,pitchmin,pitchmean,pitchstd,pitchlen]
	return out
def getPitch(startP,endP,pitch,startF,endF):
#	print startP,endP,startF,endF
	if startF<startP and endF<startP:#都小于起点	
		out=pitch
#		print out
	if startF<startP and endF<=endP and endF>=startP:#小于到中间
		out=pitch[:endF-startP+1]
	if startF>=startP and endF<=endP:#中间到中间
		out=pitch[startF-startP:endF-startP+1]
	if startF>=startP and endF> endP and startF<=endP:#中间到最后
		out=pitch[startF-startP:]
	if startF>=endP:#大于到大于
		out=pitch
	if startF<startP and endF>endP:
		out=pitch
	return out
#定义遍历文件夹的函数，第一个输入是文件夹的路径，第二个输入是要查找的文件

def TraversalFileLabel(rootdir,featurename):
	FileList=[]
	for root,SubFloders,files in os.walk(rootdir):
		for f in files:
			if f.find(featurename)!=-1:
				FileList.append(os.path.join(root,f))
	#			print('found')
	#		else:
	#			print('not found')
	return FileList
def Isjson(jsonFileName):#json 中存储了数据的featture
	json_data=open(jsonFileName)
	data=json.load(json_data)
	if len(data)==13:#这一句查看是否是
		return True
	else :
		return False
#def meanFeature(meanS):
#	if 
#	out=[]
#	sortmean=meanS.sort()
#	meanmax=max(meanS)
#	meanmin=min(meanS)
#	for iter in meanS:
#		for item in sortmean:
#			if item==
		
#	return out
def featureExtraction(jsonFileName):
	outfeature=[]
	outfeature1=[]
	json_data=open(jsonFileName)
	data=json.load(json_data)
	pitchvals=data['intonation_curve']['vals']
	startP=data['intonation_curve']['start']
	endP=data['intonation_curve']['end']
	if len(pitchvals)>0:
	#print pitch2feature(getPitch(startP,endP,pitchvals,startF,endF))
		for item in data['words'][0]["syllables"]:
			lenOfSyllables=len(data['words'][0]["syllables"])
			startF=item['stats']['start']
			endF=item['stats']['end']
		#during  time ,energy,len,max ,min ,mean ,std ,len 8#features
			outfeature.append([item['stats']['end']-item['stats']['start'],item['stats']['energy'],lenOfSyllables,pitch2feature(getPitch(startP,endP,pitchvals,startF,endF))])
#		meanS=[]
#		for item in outfeature:
#			meanS.append(item[3][2])
#		meanfeature=meanFeature(meanS)
#		for iter in range(len(outfeature)):
#			item=outfeature[iter]
#			outfeature.append([item[0],item[1],item[2],meanfeature[iter]])
		return outfeature
	else :
		return []
		#outfeature.append(data['words'][0]["syllables"][item]['stats']['start'],data['words'][0]["syllables"][item]['stats']['end'],data['words'][0]["sylliables"][item]['stats']['energy'])
#	#print data['intonation_curve']
#	#print type(data['intonation_curve'])#dict
#	#print len(data['intonation_curve'])#3,start,end,vals
#	print data['intonation_curve']['vals']
#	#print type(data['intonation_curve']['vals'])#list
#	print data['intonation_curve']['start']
#	print data['intonation_curve']['end']
#	print data['intonation_curve']['end']-data['intonation_curve']['start']
#	print len(data['intonation_curve']['vals'])
#	pitch=data['intonation_curve']['vals']
#	startP=data['intonation_curve']['start']
#	endP=data['intonation_curve']['end']
#	startF=data['words'][0]["syllables"][2]['stats']['start']
#	endF=data['words'][0]["syllables"][2]['stats']['end']
#	print startF,endF
#	print getPitch(startP,endP,pitch,startF,endF)
#	print pitch2feature(getPitch(startP,endP,pitch,startF,endF))
#以下信息调试word中每个音节的信息，以上调试pitch信息
#	#print data
#	print type(data)#dict
#	print len(data)#13个关键字，我们需要的是words这个关键字
#	#for keyJson in data:
#	#	print keyJson
#	print data['words']
#	print type(data['words'])#list
#	print len(data['words'])#1
#	print type(data['words'][0])#dict
#	print len(data['words'][0])#4,stats,syllables,word,scores
#	#for key in data['words'][0]:
#	#	print key#stats,syllables,word,scores
#	print type(data['words'][0]["syllables"])#list
#	print len(data['words'][0]["syllables"])#3,和音节数有关
#	#for iter in range(len(data['words'][0]["syllables"])):
#		#print item
#	print type(data['words'][0]["syllables"][0])#dict
#	print (data['words'][0]["syllables"][0])#dict
#	for key in data['words'][0]["syllables"][1]:
#		print key#phones,stats,scores
#	print type(data['words'][0]["syllables"][1]['stats'])#dict
#	print len(data['words'][0]["syllables"][1]['stats'])#6
#	for key in data['words'][0]["syllables"][1]['stats']:
#		print key#end,energy,pitch_pattern,start,pitch_level,stress_pattern
#	print data['words'][0]["syllables"][1]['stats']['start']
#	print data['words'][0]["syllables"][1]['stats']['end']
#	#print data['words'][0]["syllables"][1]['stats']['pitch_pattern']
#	print data['words'][0]["syllables"][1]['stats']['energy']
#	print data['words'][0]["syllables"][0]['stats']['start']
#	print data['words'][0]["syllables"][0]['stats']['end']
#	#print data['words'][0]["syllables"][0]['stats']['pitch_pattern']
#	print data['words'][0]["syllables"][0]['stats']['energy']
#	print data['words'][0]["syllables"][2]['stats']['start']
#	print data['words'][0]["syllables"][2]['stats']['end']
#	#print data['words'][0]["syllables"][2]['stats']['pitch_pattern']
#	print data['words'][0]["syllables"][2]['stats']['energy']
pkl_file=open('./mulWordList.pkl','rb')
multWordList=pickle.load(pkl_file)
#print multWordList
def has_pitch(jsonFileName):
	json_data=open(jsonFileName)
	data=json.load(json_data)
	pitchvals=data['intonation_curve']
#	startP=data['intonation_curve']['start']
#	endP=data['intonation_curve']['end']
	if len(pitchvals)>=1:
		return True
	else:
		return False
pkl_file=open('./WordList.pkl')
WordList=pickle.load(pkl_file)
#print WordList
key1=0#多音节单词数
roots='./json/'
def file2dict(rootdir,filefeature):
	FileList={}
	for root,SubFloders,files in os.walk(rootdir):
		for f in files:
			if f.find(filefeature)!=-1:
				FileList[f]=''
	return FileList
jsonFileList=file2dict(roots,'json')
count=0
WordData=[]
WordLabel=[]
S2=0
S3=0
S4=0
S=0
for keymWL in multWordList:
	if WordList.has_key(keymWL.upper()):
		key1+=1
#		print keymWL.upper()
#		print keymWL
		for item in WordList[keymWL.upper()]:
			#print item#单词地址
			#print item[1:len(item)-1]
			#print TraversalFileLabel(roots,item[1:len(item)-1])#此处是文件遍历查找，若直接获取则时间会加快，否则待查文件夹下文件做成dict也可以很快
#			print item[1:len(item)-1]+'.json'
			if jsonFileList.has_key(item[1:len(item)-1]+'.json'):
			#	count+=1
				if Isjson('./json/'+item[1:len(item)-1]+'.json') and has_pitch('./json/'+item[1:len(item)-1]+'.json'):
					DataSingleWord=[]
					DataSingleWordLable=[]
					
					filenameSingleD= './SingleDataAndLabel/'+item[1:len(item)-1]+'D.pkl'
					filenameSingleL= './SingleDataAndLabel/'+item[1:len(item)-1]+'L.pkl'
#					print './json/'+item[1:len(item)-1]+'.json'
					count+=1
				#	print count	
					temp=featureExtraction('./json/'+item[1:len(item)-1]+'.json')
					if len(temp)==2:
						S2+=1
					if len(temp)==3:
						S3+=1
					if len(temp)==4:
						S4+=1
					if len(temp)>=5:
						S+=1
					for itemF in temp:
						WordData.append(itemF)
						DataSingleWord.append(itemF)
			#			print itemF,len(temp)
					for itemL in multWordList[keymWL]:
						WordLabel.append(itemL)
						DataSingleWordLable.append(itemL)
					if count==100:
						print featureExtraction('./json/'+item[1:len(item)-1]+'.json')
					pkl_file=open(filenameSingleD,'wb')
					pickle.dump(DataSingleWord,pkl_file)
					pkl_file.close()
					pkl_file=open(filenameSingleL,'wb')
					pickle.dump(DataSingleWordLable,pkl_file)
					pkl_file.close()
		#		print count
			#	WordData.append(featureExtraction('./json/'+item[1:len(item)-1]+'.json'))
		#		WordLabel.append(multWordList[keymWL])
			#	if  count== 2:# or count==111:#count ==10 的情况下没有intonation_curve
			#		print item[1:len(item)-1]
	#				print len(multWordList[keymWL])
			#		featureExtraction('./json/'+item[1:len(item)-1]+'.json')
			#		print featureExtraction('./json/'+item[1:len(item)-1]+'.json')
		#	for #文件在json中找到:
				#提取特征，标注类标，可以存储两种形式，一种是数组形式，一种是文件夹形式形式，这样就可以分别处理每个文件来
#print key1  #875
#print WordData
print "样本数：",count
#print len(WordData)
#print len(WordLabel)
#print WordLabel
pkl_file=open('./DataAndLabel/Data.pkl','wb')
pickle.dump(WordData,pkl_file)
pkl_file.close()
pkl_file=open('./DataAndLabel/Label.pkl','wb')
pickle.dump(WordLabel,pkl_file)
pkl_file.close()
print "两音节，三音节，四音节，多音节书"
print S2,S3,S4,S
