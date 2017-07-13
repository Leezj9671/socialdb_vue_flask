# Social Database backend
## Introduction
Just a backend, shabby a little bit but it can run:>

## Database structure
- _id: MongoDB ID
- email: Email Address like 85378639@gmail.com
- password: password
- passwordHash: Hash(password）
- source: data source
- suffix_email: the suffix of email like "@gmail.com"
- user: username or login name
- xtime: data leakage time

## Install Mongodb
- Find and Download packages in http://www.mongodb.org/downloads
- On Linux
``` bash
tar -zxvf [package]
mv mongodb-linux-x86_64-****/ /usr/local/mongodb
# export to ENV PATH
export PATH=/usr/local/mongodb/bin:$PATH

# make a data dir
mkdir -p /data/db
cd /usr/local/mongodb/bin/

# run mongodb
./mongod
# ./mongo
```
- On windows
- - Find and Download packages in http://www.mongodb.org/downloads
- - Then install *.msi, simply enough.

## Mongodb things
```bash
./mongo
# create database
# > use [DATABASE]
> use socialdb
# if you want to import some test data, use ./test/gen_test.py to generate some test data.
python ./test/gen_test.py
# python base_import.py -format [*.json] -f [*.csv]
python base_import.py -format ./test/test.json -f ./test/test.csv
```
## Install env
``` bash
# use virtualenv
pip install -r .\requirements.txt

# run api_main.py
# before do this, you should modify the ./conf/config.py
python .\api_main.py
```