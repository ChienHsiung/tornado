import tornado.web
from tornado.web import RequestHandler
import os
import config

class 函數(RequestHandler):
    def get(self,*args,**kwargs):
        # a,b的值是從網頁上設定的
        def mysum(a,b):
            return a+b
        mysum1 = {"sum":0}
        self.render("函數.html" ,mysum = mysum,mysum1=mysum1)

    def post(self,*args,**kwargs):
        n1 = int(self.get_argument("num1"))
        n2 = int(self.get_argument("num2"))

        def mysum(n1,n2):
            print(n1,n2)
            return n1+n2
        mysum1 = {"sum":n1+n2}
        self.render("函數.html",mysum=mysum,mysum1=mysum1)

class mobirise(RequestHandler):
    def get(self):
        self.render("mobirise.html")

class mobiriseform(RequestHandler):
    def get(self):
        data = self.application.db.get_all_obj("select * from bank order by date desc limit 100","bank")
        self.render("mobiriseform.html",data=data)