__author__ = 'bincker'
#-*- coding: gbk -*-

import os
import re

# 枚举dirPath目录下的所有文件
def ListFiles(dirPath):

	fileList = []
	for root, dirs, files in os.walk(dirPath):
	#begin
		for fileObj in files:
		#begin
			fileList.append(os.path.join(root, fileObj))
		#end
	#end
	return fileList
#end

def FindString(filePath, regex):
#begin
	fileObj = open(filePath, 'r')
	for eachLine in fileObj:
	#begin
		if re.search(regex, eachLine, re.I):
		#begin
			print(fileObj)		#打印文件对象
			break

	#end
#end


def main():
#begin
	fileDir = "/home/kotz/Desktop/" + os.sep + "aaatest"		# 查找该目录下
	regex = raw_input("please input here")              #'android.webkit.WebView'
	fileList = ListFiles(fileDir)
	print(fileList)
	for fileObj in fileList:
	#begin
		FindString(fileObj, regex)




	#end
	os.system('exit')
#end

if __name__ == '__main__':
#begin
	main()
