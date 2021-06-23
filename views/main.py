import tornado.web
import pymysql

class Index(tornado.web.RequestHandler):
	def get(self,*args,**kwargs):
		# self.write("Hello world ")
		self.render("index.html")

class Check(tornado.web.RequestHandler):
	# 依据header收集用户信息
    def get(self):
    	# self.write("-------method:\n")
        self.write(self.request.method)
        # self.write("\n-------uri:\n")
        self.write(self.request.uri)
        # self.write("\n-------path:\n")
        self.write(self.request.path)
        # self.write("\n-------query:\n")
        self.write(self.request.query)
        # self.write("\n-------version:\n")
        self.write(self.request.version)
        # self.write("\n-------headers:\n")
        # self.write(self.request.headers)
        # self.write("\n-------body:\n")
        self.write(self.request.body)
        # self.write("\n-------remote_ip:\n")
        self.write(self.request.remote_ip)
        # self.write("\n-------protocol:\n")
        self.write(self.request.protocol)
        # self.write("\n-------host:\n")
        self.write(self.request.host)
        # self.write("\n-------arguments:\n")
        self.write(self.request.arguments)
        # self.write("\n-------query_arguments:\n")
        self.write(self.request.query_arguments)
        # self.write("\n-------body_arguments:\n")
        self.write(self.request.body_arguments)
        # self.write("\n-------files:\n")
        self.write(self.request.files)
        # self.write("\n-------cookies:\n")
        self.write(self.request.cookies)
        # self.write("\n")

class Form(tornado.web.RequestHandler):
	def get(self,*args,**kwargs):
		# 可以取得網址列裡面的參數(只有用在get時)
		# ex:http://127.0.01:8080/form?myarg1="test"&myarg2=111
		# myarg1 = self.get_query_argument("myarg1")
		# myarg2 = self.get_query_argument("myarg2")
		# print(myarg1,myarg2)
		self.render("form.html")

	def post(self,*args,**kwargs):
		# self.set_header("Access-Control-Allow-Origin", "*")
		username = self.get_argument("username")
		userpassword = self.get_argument("userpassword")
		location = self.get_argument("YourLocation")
		sex = self.get_arguments("sex")
		hobby = self.get_arguments("hobby")

		sql = "insert into mytable(name,pwd,location) values('%s','%s','%s')" % (username,userpassword,location)
		print(sql)
		runMysql(sql)
		self.render("result.html")

class Query(tornado.web.RequestHandler):
	def get(self,*args,**kwargs):
		self.render("query.html")

	def post(self,*args,**kwargs):
		location = self.get_argument("YourLocation")

		sql = "select * from mytable where location = '%s'" % (location)
		res = QueryMysql(sql)
		self.render("show.html" , data = res)

def runMysql(sql):
	try:
		conn = pymysql.connect(host='127.0.0.1',user='root',password='ooxx748',database='my',charset='utf8')
		cur = conn.cursor()
		cur.execute(sql)
		conn.commit()
	except pymysql.Error as e:
		print("数据库连接失败："+str(e))

def QueryMysql(sql):
	try:
		conn = pymysql.connect(host='127.0.0.1',user='root',password='ooxx748',database='my',charset='utf8')
		cur = conn.cursor()
		cur.execute(sql)
		res = cur.fetchall()
		return res
	except pymysql.Error as e:
		print("数据库连接失败："+str(e))		

