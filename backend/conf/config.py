class MongoDBConfig:
    g_server_ip = '127.0.0.1'	# mongodb数据库地址
    g_server_port = 27017		# 数据库端口
    g_db_name = 'socialdb'  		# 数据库名
    ALLOWED_EXTENSIONS = ['txt', 'csv'] # 允许上传的类型
    error_line_file = 'E:\Socialdb\backend\test.log' # 错误日志路径
