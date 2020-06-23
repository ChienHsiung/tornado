import tornado.web
from views import index
from views import function
import config
from conn import ConnMysql
from conn.ConnMysql import SunckSql

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/',index.IndexHandler),
            (r'/form',index.FormHandler),
            (r'/requestinfo',index.RequestInfoHandler),
            (r'/upfile',index.UpfileHandler),
            (r'/template',index.TemplateHandler),
            (r'/templatesub',index.TemplateHandlersub),    
            (r'/transvalue',index.TransValueHandler),
            (r'/function',function.函數),
            (r'/mobirise',function.mobirise),
            (r'/mobiriseform',function.mobiriseform)

        ]
        super().__init__(handlers,**config.settings)

        self.db = SunckSql(
            config.conn["host"],
            config.conn["user"],
            config.conn["password"],
            config.conn["db"],
            config.conn["port"]
            )