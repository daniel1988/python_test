#!/usr/bin/python
# -*- coding:utf-8 -*-


# class Staff:
#     '类注释'

#     staffCount = 0

#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         Staff.staffCount += 1

#     def displayCount(self):
#         print 'staffCount:', Staff.staffCount

#     def displayAll(self):
#         print "Staff.name:%s, Staff.salary:%d" % (self.name, self.salary)

# staff_1 = Staff("ear", 200)
# staff_2 = Staff("eye", 300)

# staff_1.displayCount()
# staff_2.displayAll()

# print "Staff.__doc__:", Staff.__doc__
# print "Staff.__name__:", Staff.__name__
# print "Staff.__module__:", Staff.__module__
# print "Staff.__bases__", Staff.__bases__
# print "Staff.__dict__", Staff.__dict__

class Student(object):
    pass

s = Student()
s.name = 'Daniel'

print s.name
