# -*- coding:utf-8 -*-
import pymysql

class SunckSql():
    def __init__(self,host,user,password,database,port):
        self.host=host
        self.user=user
        self.passwd=password
        self.dbName=database
        self.port=port

    def connect(self):
        self.db = pymysql.connect(self.host,self.user,self.passwd,self.dbName,self.port)
        self.cursor=self.db.cursor()

    def close(self):
        pass
        # self.cursor.close()
        # self.db.close()

    def get_one(self,sql):
        res=None
        try:
            self.connect()
            self.cursor.execute(sql)
            res=self.cursor.fetchone()
        except Exception as e:
            print(e)
            print("查询失败")
        finally:
            self.close()
        return res

    def get_all(self,sql):
        res=()
        try:
            self.connect()
            self.cursor.execute(sql)
            res=self.cursor.fetchall()
        except Exception as e:
            print(e)
            print("查询失败")
        finally:
            self.close()
        return res

    def get_all_obj(self,sql,tableName,*args):
        resList = []
        fieldsList = []
        if(len(args) > 0):
            for item in args:
                fieldsList.append(item)
        else:
            fieldsSql="select COLUMN_NAME from information_schema.COLUMNS where table_name = '%s' and table_schema = '%s'" % (tableName,self.dbName)            
            fields = self.get_all(fieldsSql)
            for item in fields:
                fieldsList.append(item[0])

        res = self.get_all(sql)

        for item in res:
            obj = {}
            count = 0
            for x in item:
                obj[fieldsList[count]] = x
                count +=1
            resList.append(obj)
            
        return resList


    def insert(self,sql):
        count=0
        try:
            self.connect()
            count=self.cursor.execute(sql)
            print("插入数据成功")
            self.db.commit()
        except Exception as e:
            print(e)
            print("插入数据失败")
            self.db.rollback()
        finally:
            self.close()
        return count

    def update(self,sql):
        count = 0
        try:
            self.connect()
            count = self.cursor.execute(sql)
            print("数据更新成功")
            self.db.commit()
        except Exception as e:
            print(e)
            print("数据更新失败")
            self.db.rollback()
        finally:
            self.close()
        return count

    def delete(self,sql):
        count = 0
        try:
            self.connect()
            count = self.cursor.execute(sql)
            print("删除数据成功")
            self.db.commit()
        except Exception as e:
            print(e)
            print("数据删除失败")
            self.db.rollback()
        finally:
            self.close()
        return count

if __name__ == '__main__':
    s = SunckSql(host="127.0.0.1", user='root', password='ooxx748@@', database='my', port=3306)
    # print(s.get_all("select * from bank"))
    # res = s.get_all("select * from ce")
    # for row in res:
    #     print("%d----%s" % (row[0], row[1]))
    # s.delete("delete from ceshi where id=10")
    # s.insert("insert into bk values (3,'bk')")
    # t=s.get_one("select * from bk where id=15")
    # print(t)
    # s.update("update bk set name='hg1' where id=3")
    # s.delete("delete from bk where id=3")