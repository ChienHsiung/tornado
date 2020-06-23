import os

BASE_DIRS = os.path.dirname(__file__)

options={
	"port":8080,
	"list":["good","nice","ok"]
}

conn={
	"host":"127.0.0.1",
	"user":"root",
	"password":"ooxx748@@",
	"db":"my",
	"port":3306
}

settings={
	"debug":True,
	"static_path":os.path.join(BASE_DIRS,"static"),
	"template_path":os.path.join(BASE_DIRS,"templates")
}