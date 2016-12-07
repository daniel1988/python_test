#!/usr/bin/env python
# -*- coding:utf-8 -*-

import redis
import demjson

redis_srv = redis.Redis(host='127.0.0.1', port=6379)

hashname = 'hashname';
data_dict = {
    'sdf':'123',
    'dd':'3333',
    'eeeee':'ffff'
}
print redis_srv.hmset(hashname, data_dict)

print redis_srv.hgetall(hashname)

field_list = ['dd', 'eeeee']

field_dict = {'a':'eeeee'}
print redis_srv.hmget(hashname, field_dict)

# redis_srv.expire(hashname, 10)


# data_dict = {}
# key = 'foo_1'
# json = redis_srv.get(key)
# print json
# if ( json ):
#     data_dict = demjson.decode(json)

# dic = {'ccc':'11', 'eee':222}
# for k,v in dic.items():
#     data_dict[k] = v



# json = demjson.encode(data_dict)
# redis_srv.set(key, json)