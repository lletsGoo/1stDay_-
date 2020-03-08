# -*- coding:utf-8 -*-


source_dir = r'C:\Users\yangyi\Desktop\网络攻防\password_new_chaifen\new\out_8.txt'
target_dir = r'C:\Users\yangyi\Desktop\网络攻防\password_new_chaifen\new\neww\\'

flag = 0

name = 1

dataList = []

with open(source_dir,'r') as f_source:
    for line in f_source:
        flag+=1
        dataList.append(line)
        if flag == "每个字典的密码数":
            with open(target_dir+"out_8"+str(name)+".txt",'w+') as f_target:
                 for data in dataList:
                      f_target.write(data)
            name+=1
            flag = 0
            dataList = []


