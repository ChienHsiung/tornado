import tornado.web
from tornado.web import RequestHandler
import os
import config

class FunctionHandler(RequestHandler):
    def get(self,*args,**kwargs):
        def mysum(a,b):
            return a+b
        self.render("function.html" ,mysum = mysum)