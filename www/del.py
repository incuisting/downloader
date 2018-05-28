#! /usr/bin/env python3
import os
import sys
import shutil
def getPath():
    print('scranPath:')
    dirPath=input()
    return dirPath

def loopDir(dirPath):
    fileNameList=[]
    for idx, filename in enumerate(os.listdir(dirPath)):
        print('('+str(idx+1)+')'+filename)
        fileNameList.append(filename)
    return fileNameList

def getDelteIndex():
    print('全部清除请输入cc,退出输入q')
    delIndex=input()
    if(delIndex=='q'):
        exit()
    if(delIndex !='cc'):
        return int(delIndex)-1
    else:
        return delIndex

def deleteFile(index,dirPath,fileNameList):
    if(index=='cc'):
        for fileName in fileNameList:
           os.remove(dirPath+'/'+fileName) 
    else: 
        path = dirPath+'/'+fileNameList[delIndex]
        if os.path.isdir(path):
            shutil.rmtree(path,ignore_errors=True)
        elif os.path.isfile(path):
            os.remove(path)

def exit():
    sys.exit()

if __name__ =='__main__':
    dirPath = getPath()
    os.system('df -k /')
    dirFileList = loopDir(dirPath)
    while len(dirFileList)>0:
        delIndex = getDelteIndex()
        deleteFile(delIndex,dirPath,dirFileList)
        dirFileList=loopDir(dirPath)

