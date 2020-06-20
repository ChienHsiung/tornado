import tornado.web
from tornado.web import RequestHandler
import os
import config

class 函數(RequestHandler):
    def get(self,*args,**kwargs):
        def mysum(a,b):
            return a+b
        self.render("函數.html" ,mysum = mysum)