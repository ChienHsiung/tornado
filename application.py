import tornado.web
import config
from views import main

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', main.Index),
            (r'/form', main.Form),
            (r'/query',main.Query),
        ]
        super(Application,self).__init__(handlers,**config.settings)
        # super().__init__(handlers)