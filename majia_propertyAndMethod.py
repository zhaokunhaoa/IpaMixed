# -*- coding: utf-8 -*-

import random
import os
import sys

os.chdir(sys.path[0])  

file_absPath = os.getcwd()
classArray = ['NSString','NSDictionary','NSData','NSArray']# 类型从这个数组里随机选
hRule = ["e;","n;","m;","q;","r;","y;"]
mRule = ["c];","n];","m];","l];","p];","q];","w];"]
randomStrArray = []


def hRuleStr(nameStr,className):
    str = ''
    str += '\n\n/*********dagenijiaxiangyousibaijinyama**********/\n@property(nonatomic,strong)'+className +' * '+nameStr+';\n/*********dagenijiaxiangyousibaijinyama**********/\n\n'
    str += '\n\n/*********dagenijiaxiangyousibaijinyama**********/\n-('+ className +' *)mz'+nameStr+';\n/*********dagenijiaxiangyousibaijinyama**********/\n\n'
    return str

def mRuleStr(nameStr,className):
    str = ''
    str += '\n\n/*********dagenijiaxiangyousibaijinyama**********/\n'+className +' * '+nameStr+' = '+'[['+className+' alloc]init];'+'\n/*********dagenijiaxiangyousibaijinyama**********/\n\n'
    return str


def main():
    randomStrArray = getUselessArray()
    file_name(file_absPath)

def getUselessArray():
    
    first = "abcdefghijklmnopqrstuvwxyz"
    second = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    third = "1234567890"
    number = "345"
    index = 0
    randomArray = []
    for i in range(500):
        final = (random.choice(first))
        index = random.randint(3, 5)
        
        for i in range(index):
            final += (random.choice(first))
            final += (random.choice(second))
        
        for i in range(index):
            final += (random.choice(third))
        
        randomStrArray.append(final)

    return list(set(randomStrArray))



#.h文件添加废代码
def HFileUselessCode(file_path,strs):
    
    file_data = ""
    Ropen=open(file_path,'r')
    isStart=0
    isEnd=0

    for line in Ropen:
        if '@interface' in line:
            isStart=1
        
        if '@end' in line:
            isEnd=1

        nameStr = random.choice(randomStrArray)
        className = random.choice(classArray)
        flag = 0
        for str in strs:
            if str in line:
                flag = 1
                file_data += line
                if isEnd == 1:
                    break
                if isStart == 1:
                    file_data += hRuleStr(nameStr, className)
                    randomStrArray.remove(nameStr)#防止创建的元素名重复(创建一个从数组中删除一个)
                break
                
        if flag == 0:
            file_data += line
    Ropen.close()
    Wopen=open(file_path,'w')
    Wopen.write(file_data)
    Wopen.close()
    print(file_data)


#.m文件添加废代码
def MFileUselessCode(file_path,strs):

    file_data = ""
    Ropen=open(file_path,'r')#读取文件
    
    for line in Ropen:
        if line.strip().startswith('//'):
            continue
        nameStr = random.choice(randomStrArray)
        className = random.choice(classArray)
        flag = 0
        for str in strs:
            if str in line:
                file_data += line
                file_data += mRuleStr(nameStr, className)
                randomStrArray.remove(nameStr)#防止创建的元素名重复(创建一个从数组中删除一个)
                flag = 1
                break
                
        if flag == 0:
            file_data += line
        

    Ropen.close()
    Wopen=open(file_path,'w')
    Wopen.write(file_data)
    Wopen.close()
    print(file_data)


def file_name(file_dir):
    for file in os.listdir(file_dir):
        #递归遍历文件夹下的.h和.m文件并添加废代码
        if 'Pod' in file:
            continue
        file_path = os.path.join(file_dir, file)
        if os.path.isdir(file_path):
            file_name(file_path)
            continue
        else:
            if '.h' in file:
                HFileUselessCode(file_path, hRule)#往凡是以hRule这些中的某一个结尾的oc语句后添加费代码
            if '.m' in file:
                MFileUselessCode(file_path, mRule)#往凡是以mRule这些中的某一个结尾的oc语句后添加费代码           

main()
