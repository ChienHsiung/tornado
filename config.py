import os

BASE_DIRS = os.path.dirname(__file__)

options={
	"port":8080,
	"list":["good","nice","ok"]
}

settings={
	"debug":True,
	"static_path":os.path.join(BASE_DIRS,"static"),
	"template_path":os.path.join(BASE_DIRS,"templates")
}