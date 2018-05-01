'''
操作方式 .py -j test.json -f test.csv
'''
import os
import sys
import re
import getopt
import json
import time
import datetime
import hashlib

from pymongo import MongoClient
from conf.config import MongoDBConfig

def usage():
    print('import.py USAGE:')
    print('-h, --help:\tprint help message.')
    print('-f, --format:\tformat json file')
    print('-d, --data:\timport a data file')
    print('-p, --path:\timport path files')
    print('Examples:\nimport.py -f ./test.json -d ./test.csv')

def check_opts(argv):
    '''
    负责检查参数完整性
    '''
    try:
        opts, args = getopt.getopt(argv[1:], 'f:d:p:', ['format=', 'data=', 'path='])
        if opts == []:
            usage()
            sys.exit(0)
    except getopt.GetoptError as err:
        print("[!] ", err)
        usage()
        sys.exit(2)

    format_file = ''
    data_file = ''
    data_path = ''
    for o, a in opts:
        if o in ('-h', '--help'):
            usage()
            sys.exit(1)
        elif o in ('-f', '--format'):
            format_file = a
        elif o in ('-d', '--data'):
            data_file = a
        elif o in ('-p', '--path'):
            data_path = a
        else:
            print('[!] Unhandeled options.')
            usage()
            sys.exit(3)
    if format_file == '':
        # FormatFile是必需的
        print('[!] Format File is NEEDED')
        usage()
        sys.exit(1)
    if not (data_file == '') ^ (data_path == ''):
        print('[!] Data file and path file is NEEDED one of them.')
        usage()
        sys.exit(1)
    return format_file, data_file, data_path

def file_into_database(filename, split_sign, csv_sign, regex, cus, ids):

    client = MongoClient(MongoDBConfig.g_server_ip, MongoDBConfig.g_server_port)
    db = client[MongoDBConfig.g_db_name]
    collection = db.person
    starttime = datetime.datetime.now()

    try:
        with open(filename) as file:
            ef = open(MongoDBConfig.error_line_file, 'a')
            cnt = 0
            for line in file:
                try:
                    linedata = {}
                    if csv_sign:
                        csv_sign = False
                        continue
                    # print("cus", cus)
                    linedata = dict(linedata, **cus)
                    line = line.strip('\n')
                    group = line.split(split_sign)
                    for i, val in enumerate(ids):
                        linedata[val] = group[i]
                    if 'email' in ids:
                        linedata['suffix_email'] = linedata['email'].split('@')[1].lower()
                        linedata['user'] = linedata['email'].split('@')[0]
                    if 'password' in ids and 'passwordHash' not in ids:
                        linedata['passwordHash'] = hashlib.md5(linedata['password'].encode('utf-8')).hexdigest()
                    for re_id, val in regex.items():
                        pattern = val["re"]
                        target = linedata[val["target"]]
                        redata = re.findall(pattern, target)[0]
                        if type(redata) is tuple:
                            redata = redata[0]
                        linedata[re_id] = redata
                    linedata['create_time'] = time.strftime('%Y/%m/%d %H:%M:%S',time.localtime(time.time()))
                    collection.save(linedata)
                except:
                    cnt += 1
                    ef.write(str(linedata) + '\n')

            ef.close()

    except IOError:
        print('[!] Data file or log file opened ERROR! ', filename, MongoDBConfig.error_line_file)
        sys.exit(1)

    endtime = datetime.datetime.now()
    print('导入成功，时间为{}s. 出错数量为{}个'.format(endtime - starttime, cnt))

def main(argv):
    format_file, data_file, data_path = check_opts(argv)

    # 社工库本地地址
    sgk_path = 'F:\\shegongku'

    columns = []
    try:
        with open(format_file,'r') as f:
            json_file = json.load(f)
            # 从json文件中的split确定分隔符
            split_sign = json_file["split"]
            csv_sign = json_file["strip_csv_tilte"]
            regex_pattern = json_file["regex"]
            custom_field = json_file["custom_field"]
            ids = json_file["id"]
            sorted_ids = [k for k in sorted(ids.keys())]
            ids = [ids[i] for i in sorted_ids]
    except IOError:
        print('[!] Format file opened ERROR!')
        sys.exit(1)

    if data_file != '':
        file_into_database(data_file, split_sign, csv_sign, regex_pattern, custom_field, ids)
    elif data_path != '':
        for fpathe,dirs,fs in os.walk(sgk_path):
            for f in fs:
                file_into_database(os.path.join(fpathe,f), split_sign, csv_sign, regex_pattern, custom_field, ids)

if __name__ == '__main__':
    main(sys.argv)

