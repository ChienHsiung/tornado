import tornado.web
import tornado.ioloop
import config
from application import Application

if __name__ == "__main__":
	print(tornado.version)
	print("list = ",config.options["list"])

	app = Application()
	app.listen(config.options["port"])
	tornado.ioloop.IOLoop.current().start()