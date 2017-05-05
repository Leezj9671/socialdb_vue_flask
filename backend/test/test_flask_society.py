import requests

url = "http://127.0.0.1:5000/api"

#测试Person
print("Person:\n{}".format(requests.get(url+"/find/user/123").text))


#测试analysis
print("Analyze email:\n{}".format(requests.get(url+"/analysis/email", data={"email":"@qq.com"}).text))
