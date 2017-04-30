'''
操作方式 .py -format test.json -f test.csv
'''
#coding:utf-8
import sys
import re
import json
from itertools import islice
from pymongo import MongoClient
from conf.config import MongoDBConfig

client = MongoClient(MongoDBConfig.g_server_ip, MongoDBConfig.g_server_port)
db = client[MongoDBConfig.g_db_name]

def command_import(argv):
    point=0
    while point < 4:
        point+=1
        if argv[point]=='-format':
            try:
                with open(argv[point+1],'r') as f:
                    json_file=json.load(f)
                point+=1
            except IOError:
                print('格式文件打开失败')
                return '格式文件打开失败'
        if argv[point]=='-f':
            try:
                fname=argv[point+1]
                data_file=open(fname,'r')
                point+=1
            except IOError:
                print('数据文件打开失败')
                return '数据文件打开失败'
    columns=[]
    
    for column in json_file:
        columns.append(json_file[column])

    #从json文件中的split确定分隔符
    fenge = json_file["split"]
    column = data_file.readline().strip('\n').split(fenge)

    #判定json格式中所需要的数据项
    num=[]
    t = 0
    for i in column:
        if i in columns:
            num.append(t)
        t += 1
    
    for line in islice(data_file, 0, None):
        if line=='\n':
            continue
        linedata={}
        line=line.strip('\n')
        group=line.split(fenge)
        
        for i in num:
            linedata[column[i]]=group[i]
        
        #warning: may cause errors.
        if 'email' in column:
            linedata['suffix_email'] = linedata['email'].split('@')[1]

        db.person.save(linedata)

    print('导入成功')
    data_file.close()

if __name__=='__main__':
    command_import(sys.argv)
