import tornado.web
from views import index
from views import function
import config

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
            (r'/mobirise',function.mobirise)
        ]
        super().__init__(handlers,**config.settings)