#!/usr/bin/env python 
#encoding=utf-8
import os
import sys
import pickle
def TraversalFile(rootdir,feature):
	FileList=[]
	for root,SubFloders,files in os.walk(rootdir):
		for f in files:
			if f.find(feature)!=-1:
				FileList.append(os.path.join(root,f))
	return FileList
#feature
#[43, 0.746, 2, [9.3, -12.6, -0.41739130434782545, 59.197958412098295, 23]]
#长短，能量，音节数字
rootdir='../SingleDataAndLabel/'
FileListData=TraversalFile(rootdir,'D.pkl')
FileListLable=TraversalFile(rootdir,'L.pkl')
LableDict={}
#print len(FileListData)
print len(FileListLable)
for fileL in FileListLable:
	pkl_file=open(fileL,'rb')
	Lable=pickle.load(pkl_file)
	#print fileL
#	print Lable
	LableDict[fileL[22:41]]=Lable
print len(LableDict)
#for key in LableDict:
#	print key
count=0
def LR(LRpara,item):
	out=0
	item1=[1]
	for iter in range(len(item)):
		if iter==0:
	
			item1.append(item[iter]/48)
		if iter ==1:
			item1.append(item[iter]/0.4)
	for iter in range(len(LRpara)):
		out=out+LRpara[iter]*item1[iter]
	return out
countRight=0
for fileD in FileListData :
	pkl_file=open(fileD,'rb')
	Data=pickle.load(pkl_file)
	max_i = 0
	max_LR = -100 
	if fileD[22:41] in LableDict:
		count+=1
		for iter in range(len(Data)):
		#	print Data[iter][0:2]
			if LR([-1.7899,-1.3599,2.0514],Data[iter][0:2])>max_LR:
				max_i=iter
				max_LR=LR([-1.7899,-1.3599,2.0514],Data[iter][0:2])
	#for item in LableDict[fileD[22:41]]:
	#	print item
		#if item[max_i]==1:
		#	countRight+=1
	if LableDict[fileD[22:41]][max_i]==1:
		countRight+=1
#	print len(Data)
#	print Data
#print count
print countRight
"""	
pkl_file=open('./Data.pkl','rb')
Data=pickle.load(pkl_file)
pkl_file=open('./Label.pkl','rb')
Label=pickle.load(pkl_file)
feature=[]
for iter in range(len(Data)):
	feature.append([Label[iter],Data[iter][0],Data[iter][1],Data[iter][2]])#,Data[iter][3][4],Data[iter][3][0],Data[iter][3][1],Data[iter][3][2],Data[iter][3][3]])
	if iter ==100:
		print Data[iter]
		print Label[iter]
		for iter1 in range(len(Data[iter])):
			print Data[iter][iter1],iter1
#print feature
file1=open('./trainData','w')
for iter in range(len(feature)):
	file1.write(str(feature[iter][0])+'\t')
	file1.write('1:'+str(feature[iter][1])+'\t')
	file1.write('2:'+str(feature[iter][2])+'\t\n')	
#	file1.write('3:'+str(feature[iter][3])+'\t\n')
	#file1.write('4:'+str(feature[iter][4])+'\t')
	#file1.write('5:'+str(feature[iter][4])+'\t')
	#file1.write('6:'+str(feature[iter][6])+'\n')
file1.close()
"""
