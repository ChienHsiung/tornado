import tornado.web
from tornado.web import RequestHandler
import os
import config

class IndexHandler(RequestHandler):
	def set_default_headers(self):
		pass
	def initialize(self):
		#self.send_error(500)
		pass
	def prepare(self):
		pass
	def write_error(self,status_code,**kwargs):
		#self.write("伺服器發生錯誤")
		pass
	def on_finish(self):
		pass
	def get(self,*args,**kwargs):
		# self.write("Hello world ")
		self.render("menu.html")

class FormHandler(RequestHandler):
	def get(self,*args,**kwargs):
		# 可以取得網址列裡面的參數(只有用在get時) ex:http://127.0.01:8080/form?myarg1="test"&myarg2=111
		# myarg1 = self.get_query_argument("myarg1")
		# myarg2 = self.get_query_argument("myarg2")
		# print(myarg1,myarg2)
		self.render("form.html")

	def post(self,*args,**kwargs):
		username = self.get_argument("username")
		userpassword = self.get_argument("userpassword")
		sex = self.get_arguments("sex")
		hobby = self.get_arguments("hobby")
		print(username,userpassword,sex,hobby)
		self.write("Success Sended !!")

class RequestInfoHandler(RequestHandler):
	def get(self,*args,**kwargs):
		print(self.request.method)
		print(self.request.host)
		print(self.request.uri)		
		print(self.request.path)
		print(self.request.query)
		print(self.request.version)	
		print(self.request.headers)
		print(self.request.body)
		print(self.request.remote_ip)
		print(self.request.files)
		self.write("<h1 style='color:red'> show info already !! </h1>")			

class UpfileHandler(RequestHandler):
	def get(self,*args,**kwargs):
		self.render("upfile.html")
	def post(self,*args,**kwargs):
		filesContent=self.request.files
		# print(files)
		for filesName in filesContent:
			fileArray = filesContent[filesName]
			for fileObj in fileArray:
				filePath=os.path.join(config.BASE_DIRS,"upfile/" + fileObj.filename)
				with open(filePath,"wb") as f:
					f.write(fileObj.body)
		self.write("files upload already !!")			

class TemplateHandler(RequestHandler):
	def get(self,*args,**kwargs):
		self.render("template.html")

class TemplateHandlersub(RequestHandler):
	def get(self,*args,**kwargs):
		self.render("templatesub.html")

#參數的傳遞 to web UI
class TransValueHandler(RequestHandler):
	def get(self,*args,**kwargs):
		mytmp = 100
		mycolor = 0
		mydata={
			"name":"chien hsiung",
			"age":50
		}
		mytable=[
			{"name":"Chien Hsiung","age":50},
			{"name":"君君","age":18},
			{"name":"小三","age":16}
		]
		# 用兩種方法傳遞 mudata; mydata1=mydata & **mydata
		self.render("transValue.html",num = mytmp,mydata1 = mydata,**mydata,color = mycolor,table=mytable)