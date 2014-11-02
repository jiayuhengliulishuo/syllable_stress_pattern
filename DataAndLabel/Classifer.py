#encoding=utf-8
import os
import sys
import pickle
#feature
#[43, 0.746, 2, [9.3, -12.6, -0.41739130434782545, 59.197958412098295, 23]]
#长短，能量，音节数字
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
