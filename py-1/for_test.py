#!/usr/bin/python

# for num in range(1,20):
#     print num
#     if ( num == 20 ) :
#         break;

# else :
#     print num



# for letter in 'Python':
#     if letter == 'h':
#         pass
#         print "pass--------"
#     print "current letter:" , letter


# list = ['php', 'Python', 'c++']
# print list
# print list[2]

# tup = ('english', 'chinese', 'math')
# print tup
# print tup[1:2]
#
import demjson
data = {}

dic = {'aaa':'11', 'bb':222}
print dic
for k,v in dic.items():
    data[k] = v
    print k,v

print data

json = demjson.encode(data)

print 'json:', json

dict_2 =  demjson.decode(json)
print dict_2


print dict(zip(dict_2.values(), dict_2.keys()))
