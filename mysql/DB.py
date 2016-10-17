#/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb
import yaml
import os
import datetime
import random

class DB:

    conf    = None
    cursor  = None

    # 初始化DB配制
    def __init__(self, name='db'):
        # 加载配制
        conf = self.loadConfig().get(name)
        if ( conf is None ):
            raise RuntimeError('Invalid mysql connection "%s"' % name)

        self.timezone   = conf.get('timezone')
        self.autocommit = conf.get('autocommit', True)
        if ( conf.has_key('timezone') ):
            del conf['timezone']

        if conf.has_key('autocommit'):
            del conf['autocommit']
        self.conf = conf

    # 连接MySql
    def connect(self):
        if (self.cursor is not None):
            return self.cursor

        try:
            conn=MySQLdb.connect( **self.conf )
        except Exception, e:
            self.log("Connect Exception:%s" % e)
            raise RuntimeError('Mysql Connect Exception "%s"' % e)

        conn.autocommit( self.autocommit )
        if ( self.timezone is not None ):
            conn.cursor().execute("set time_zone='%s'" % self.timezone)

        self.cursor = conn.cursor()
        return self.cursor

    # 查询所有结果
    def fetch_all(self, sql, param=None):
        self.execute(sql, param)
        fields = map(lambda x: x[0], self.connect().description)
        return [dict(zip(fields, row)) for row in self.connect().fetchall()]

    # 查询一条结果
    def fetch_one(self, sql, param=None):
        self.execute(sql, param)

        fields = map(lambda x: x[0], self.connect().description)
        result = dict( zip( fields, self.connect().fetchone() ) )
        return result


    def insert(self, table, data_set):
        fields = ', '.join(map(self.quote_field, data_set.keys()))
        values = ', '.join(map(self.quote_value, data_set.values()))

        sql = 'INSERT INTO %s (%s) VALUES (%s)' % \
        (self.quote_field(table), fields, values)

        result = self.execute(sql)
        self.log(sql + "\nresult:%s" % result)
        return result

    def execute(self, sql, param=None):
        res = self.connect().execute(sql, param)
        self.log("execute res:%s sql:\n %s" % (res, sql) )
        return res

    #消除数据中的非法字符
    def quote_value(self,value):
        if isinstance(value, bool):
            value = int(value)
        elif value is None:
            value = ''
        elif isinstance(value, str) and value.upper() == 'NULL':
            value = ''
        return "'%s'" % MySQLdb.escape_string(str(value))

    # 为字段添加表名定界符
    def quote_field(self, table):
        return '.'.join(map(lambda x: "`%s`" % x, table.split('.')))

    # 写入日志记录
    def log(self, msg):
        msg = '['+ datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+ ']\n'\
            + msg \
            + '\n'
        log_dir = os.getcwd() + '/log/' + datetime.datetime.now().strftime("%Y%m")
        if ( os.path.exists(log_dir) == False ):
            os.mkdir(log_dir)
        log_file = log_dir + '/log_' + datetime.datetime.now().strftime("%Y%m%d") + '.log'
        fp = open(log_file,'ab')
        fp.write(msg)

    def loadConfig(self):
        f           = open('./conf/db.yaml')
        return yaml.load(f)


# DB().connect()
# table = 'test_1'
# data_set = {
#     'name':datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
# }
# DB().insert(table ,data_set)

# sql = 'SELECt * FROM test_1 WHERE id<10'
# print DB().fetch_one(sql)
#
# sql = 'SELECt * FROM test_1 LIMIT 3'
# print DB().fetch_all(sql)
#
id = random.randint(1,10)
print id
sql = 'SELECt * FROM test_1 where id=%d' % (id)
print DB().fetch_all(sql)
sql = "update test_1 set name=%s where id=%d" % (datetime.datetime.now().strftime("%Y%m%d%H%M%S"), id)
DB().execute( sql )

sql = 'SELECt * FROM test_1 where id=%d' % (id)
print DB().fetch_one(sql)