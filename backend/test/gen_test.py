'''
用于生成测试的库
'''
from hashlib import md5
from string import digits, ascii_letters
from random import randint, choice

mail = ['@qq.com','@163.com','@gmail.com', '@hotmail.com']
source = ['jd', 'qq', '163', 'cms']
xtime = ['2016.2', '2016.3', '2017.1']

def make_rnd_str(minLen=3, maxLen=10):
    '''
    生成随机字符串
    '''
    letters = digits + ascii_letters
    return ''.join([choice(letters) for _ in range(randint(minLen, maxLen))])

class gen_test:

    def gen_test_csv(gen_add, gen_time):
        '''
        gen_add: 生成地址
        gen_time: 生成数据次数
        '''
        with open(gen_add, 'w') as f:
            f.write('user,password,passwordHash,email,source,xtime\n')
            while gen_time:
                gen_time -= 1
                data = []
                data.append(make_rnd_str(3,6))
                pwd = make_rnd_str(8,15)
                pwdHash = md5(pwd.encode('utf-8')).hexdigest()
                data.append(pwd)
                data.append(pwdHash)
                data.append(str(randint(1000000,100000000)) + choice(mail))
                data.append(choice(source))
                data.append(choice(xtime))
                print(data)
                f.write(','.join(d for d in data) + '\n')

if __name__ == '__main__':
    gen_test.gen_test_csv('./test.csv', 100)
                   
            