import tornado.web
import pymysql

class Index(tornado.web.RequestHandler):
	def get(self,*args,**kwargs):
		# self.write("Hello world ")
		self.render("index.html")

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
		conn = pymysql.connect(host='127.0.0.1',user='root',password='ooxx',database='my',charset='utf8')
		cur = conn.cursor()
		cur.execute(sql)
		conn.commit()
	except pymysql.Error as e:
		print("数据库连接失败："+str(e))

def QueryMysql(sql):
	try:
		conn = pymysql.connect(host='127.0.0.1',user='root',password='ooxx',database='my',charset='utf8')
		cur = conn.cursor()
		cur.execute(sql)
		res = cur.fetchall()
		return res
	except pymysql.Error as e:
		print("数据库连接失败："+str(e))		

