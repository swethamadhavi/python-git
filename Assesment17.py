#1.Method overloading is poosible in python.If possible write an example
#In Python method overloaing is not possible
#If we are trying to declare multiple methods with same name and different no.of arguments then python will always consider only last method
# class Python:
#     def java(self):
#         print("no_arg method")
#     def java(self,a):
#         print("one-arg method")
#     def java(self,a,b):
#         print("two-arg method")
# obj=Python()
# #obj.java()
# #obj.java(10)
# obj.java(20,30)

#2.Constructor overloading using variable length arguments
#constructor overloading is not possible in python
#If we are trying to declare multiple methods with same name and different no.of arguments then python will always consider only last method
# class Python:
#     def __init__(self,*a):
#         print("no.of arguments")
# obj=Python()
# #obj1=Python(10)
# #obj2=Python(10,20)
# #obj3=Python(10,20,30)


#3.Create a abstract class and write method in side that
# from abc import *
# class Test():
#     @abstractmethod
#     def m1(self):
#         print("Good Morning")
# t=Test()
# t.m1()

#4.What is multiple inheritance and write an example
#Inheriting properities from multiple parent classes to single child class
# class A:
#     def add(self):
#         print("add teo numbers",)
# class B:
#     def sub(self):
#         print("subtract two numbers")
# class C(A,B):
#     def mul(self):
#         print("multiply two numbers")
# obj=C()
# obj.add()
# obj.sub()
# obj.mul()

#5.Create a class and create object dynamically use global() method
# from abc import *
# class DBInterface(ABC):
#     @abstractmethod
#     def connect(self):
#         pass
#     @abstractmethod
#     def disconnect(self):
#         pass
# class Oracle(DBInterface):
#     def connect(self):
#         print("Connecting to Oracle Database")
#     def Swetha(self):
#         print("Swetha is good")
#     def disconnect(self):
#         print("Disconnecting to Oracle Database")
# class Sybase(DBInterface):
#     def connect(self):
#         print("Connecting to Sybase Database")
#     def Madhavi(self):
#         print("Madhavi is good")
#     def disconnect(self):
#         print("Disconnecting to Sybase  Database")
# dbname=input('Enter Database Name:')
# classname=globals()[dbname]
# x=classname()
# x.connect()
# x.disconnect()