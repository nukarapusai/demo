
# class Employ:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def show(self):
#         print(self.name,self.age)
#
# c=Employ("A",9)
# # print(c.name,c.age)
# import mysql.connector
# db=mysql.connector.connect(host='localhost',
#                            user='root',
#                            passwd='root',
#                            database='saidb'
#
# )
# a=db.cursor()
# a.execute('show database')
# # class Father:
#     def __init__(self):
#         print('father')
#     def show(self):
#         print('a')
# class Son(Father):
#     def __init__(self):
#         #super().__init__()
#
#         print('child')
#     def disp(self):
#         print('B')
#
# s=Son()

# class Employe():
#     def name(self):
#         print('A')
# class Salary():
#     def salary(self):
#         print(20)
# class age(Employe,Salary):
#     def age(self):
#         print(30)
#
# call=age()
#
# call.name()
# call.salary()
# call.age()
# def world(str):
#     count=dict()
#     words=str.split()
#
#     for word in words:
#         if word in count:
#             count[word]+=1
#         else:
#             count[word]=1
#     return count
# print(world("my father lkes red color but i like red color and blue color"))
#
# a="my father lkes red color but i like red color and blue color"
#
# #
# def small(fun):
#     def big():
#         res=fun()
#         modifer=res.upper()
#         return modifer
#     return big
#
# @small
# def Cappitel():
#     return 'how are you?'
# c=Cappitel()
# print(c)

def small(un):
    def big():
        res=un()
        mod=res.upper()
        return mod
    return big
@small
def cap():
    return 'hieie'
c=cap()
print(c)
#
# def small(fun):
#     def wrapper():
#         res=fun()
#         modify=res.title()
#         return modify
#     return wrapper()
# @small
# def cappitel():
#     return 'heLOlo'
# c=cappitel
# print(c)
#
#
#

#
# def string(str):
#     count=dict()
#     words=str.split()
#
#     for i in words:
#         if i in count:
#             count[i]+=1
#
#         else:
#              count[i]=1
#     return count
# print(string("hi, how are yoy, hi sai, how ar you tony"))


# def string(str):
#     count=dict()
#     words=str.split()
#
#     for i in words:
#         if i in count:
#             count[i]+=1
#         else:
#             count[i]=1
#
#     return count
# print(string("hi, how are you sai, sai is good"))

#
# def string(str):
#     count=dict()
#     words=str.split()
#
#     for i in words:
#         if i in count:
#             count[i]+=1
#
#         else:
#             count[i]=1
#
#     return count
# print(string("hello, heoll, hi, hi"))
#
#
#




#
# def small(fun):
#     def wrapper():
#         res=fun()
#         a=res.upper()
#         return a
#     return wrapper
# @small
# def Cappitel():
#     return 'how r u?'
# c=Cappitel()
# print(c)
#
#
#
# a='hi how are you'
# b=0
#
#
#
# def string(str):
#     count=dict()
#     Words=str.split()
#     for i in Words:
#         if i in count:
#             count[i]+=1
#         else:
#             count[i]=1
#     return count
# print(string('Hi, how are you wello come'))
#
#
#
#
#
#
#












#
# def small(a,b):
#     print(a,b)
# def wrapper(fun):
#     def inner(a,b):
#         if a>b:
#             a,b=b,a
#         return fun(a,b)
#     return inner
# a=wrapper(small)
# a(2,4)
#
# def small(fun):
#     def wrapper():
#         a=fun()
#         b=a.upper()
#         return b
#     return wrapper()
# @small
# def Cap():
#     return 'Hello, hoW, Hula'
# c=Cap
# print(c)