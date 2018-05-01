# Social Engineering Database backend
## Introduction
Just a backend exposing the API interface, shabby a little bit but it can run:>

## RESTful API
- `/api/find`
- `/api/find/user/[arg]?limit=[int]&skip=[int]`
- `/api/find/email/[arg]?limit=[int]&skip=[int]`
- `/api/find/password/[arg]?limit=[int]&skip=[int]`
- `/api/find/passwordHash/[arg]?limit=[int]&skip=[int]`
- `/api/analysis/[source, xtime, suffix_email]`

## Install environment
``` bash
# Use virtualenv is advised
pip install -r ./requirements.txt

# Run api_main.py
# Before you doing this, you should modify conf/config.py
python ./api_main.py
```

## MongoDB setttings
### Database structure
Fields | Instructions
-- | --
_id |  MongoDB ID
email | Email Address like `85378639@gmail.com`
password | Password in cleartext
passwordHash | Password in hash
source | Data leakage source
suffix_email | Suffix of email like `@gmail.com`
user | Username or login name
xtime | Data leakage time

### Install Mongodb
Find and Download the package you need in http://www.mongodb.org/downloads

#### Linux
``` bash
tar -zxvf [package]
mv mongodb-linux-x86_64-****/ /usr/local/mongodb
# export to ENV PATH
export PATH=/usr/local/mongodb/bin:$PATH

# make a data dir
mkdir -p /data/db
cd /usr/local/mongodb/bin/

# Run mongodb
./mongod
# ./mongo
```

#### On windows
- Find and Download packages in http://www.mongodb.org/downloads
- Then install *.msi, simply enough.

### Run MongoDB
```bash
./mongo
# Create database in MongoDB shell
# > use [DATABASE]
> use socialdb
# If you want to import some test data, use test/gen_test.py to generate some test data.
python ./test/gen_test.py

# base_import.py using like below
# Python base_import.py -format [*.json] -f [*.csv]
python base_import.py -format ./test/test.json -f ./test/test.csv
```

