'''
api
'''

from pymongo import MongoClient
from flask import Flask, request, jsonify, Response
from flask_restful import Api, Resource
from werkzeug.datastructures import Headers
from conf.config import MongoDBConfig

app = Flask(__name__)
client = MongoClient(MongoDBConfig.g_server_ip ,MongoDBConfig.g_server_port)
db = client[MongoDBConfig.g_db_name]

# class AResponse(Response):
#     '''为解决跨域请求的相应类'''
#     def __init__(self, response=None, **kwargs):
#         kwargs['headers'] = ''
#         headers = kwargs.get('headers')
#         # 跨域控制 
#         origin = ('Access-Control-Allow-Origin', '*')
#         methods = ('Access-Control-Allow-Methods', 'HEAD, OPTIONS, GET, POST, DELETE, PUT')
#         if headers:
#             headers.add(*origin)
#             headers.add(*methods)
#         else:
#             headers = Headers([origin, methods])
#         kwargs['headers'] = headers
#         return super().__init__(response, **kwargs)

def response_cors(data=None, status=None):
    '''为返回的json格式进行跨域请求'''
    if data:
        resp = jsonify({"status": status, "data": data})

    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

class Person(Resource):
    '''人员类'''
    def get(self, user=None, email=None, password=None, passwordHash=None, source=None, xtime=None):
        #data用于存储获取到的信息

        data = []

        #待改进
        if user:
            persons_info = db.person.find({"user": user}, {"_id": 0})
            
        elif email:
            persons_info = db.person.find({"email": email}, {"_id": 0})

        elif password:
            persons_info = db.person.find({"password": password}, {"_id": 0})
        
        elif passwordHash:
            persons_info = db.person.find({"passwordHash": passwordHash}, {"_id": 0})
        
        elif source:
            persons_info = db.person.find({"source": source}, {"_id": 0})

        elif xtime:            
            persons_info = db.person.find({"xtime": xtime}, {"_id": 0})            
            
        else:
            #限制只能查询10个
            persons_info = db.person.find({}, {"_id": 0, "update_time": 0}).limit(10)
 
        for person in persons_info:
            data.append(person)

        #判断有无数据返回 
        if data:
            return response_cors(data, "ok")
        else:
            return response_cors(data, "not found")
            
    def post(self):
        '''
        以json格式进行提交文档
        '''
        data = request.get_json()
        if not data:
            return {"response": "ERROR DATA"}
        else:
            user = data.get('user')
            email = email.get('email')

            if user and email:
                if db.person.find_one({"user": user, "email": email}, {"_id": 0}):
                    return {"response": "{{} {} already exists.".format(user, email)}
                else:
                    db.person.insert(data)
            else:
                return redirect(url_for("person"))
    
    def put(self, user, email):
        '''
        根据user和email进行定位更新数据
        '''
        data = request.get_json()
        db.person.update({'user': user, 'email': email},{'$set': data})
        return redirect(url_for("person"))

    def delete(self, email):
        '''
        email作为唯一值, 对其进行删除
        '''
        db.person.remove({'email': email})
        return redirect(url_for("person"))


class Analysis(Resource):
    '''
    分析功能
    '''
    def get(self, type_analyze):
        '''
        type为分析类型，包括邮箱后缀、泄漏来源、泄漏时间
        type: [suffix_email, source, xtime]
        '''
        if type_analyze in ["source", "xtime", "suffix_email"]:
            pipeline = [{"$group" : {"_id" : '$'+type_analyze, "sum" : {"$sum" : 1}}}]
            return response_cors(list(db.person.aggregate(pipeline)), "ok")
            #return jsonify({"status": "ok", "sum": db.person.find().count(), "data": })

        else:
            return response_cors("use /api/analysis/[source, xtime, suffix_email] to get analysis data.", "error")
            #return jsonify({"status":"error", "response":"use /api/analysis/[source, xtime, suffix_email] to get analysis data."})
        
#添加api资源
api = Api(app)
api.add_resource(Person, "/api/find")
#do better
api.add_resource(Person, "/api/find/user/<string:user>", endpoint="user")
api.add_resource(Person, "/api/find/email/<string:email>", endpoint="email")
api.add_resource(Person, "/api/find/pwd/<string:password>", endpoint="password")
api.add_resource(Person, "/api/find/pwdHash/<string:passwordHash>", endpoint="passwordHash")
api.add_resource(Person, "/api/find/source/<string:source>", endpoint="source")
api.add_resource(Person, "/api/find/time/<string:xtime>", endpoint="xtime")
###
api.add_resource(Analysis, "/api/analysis/<string:type_analyze>", endpoint="type_analyze")

if __name__ == '__main__':
    app.run(debug=True)
    #app.response_class = AResponse