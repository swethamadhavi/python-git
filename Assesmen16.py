#1.What is class and object write an example
#Class:Class is a collection of objects and methods and variables
#syntax:class keyword "Classname":
#Object:It is an instance of class.Object is a blueprint of class.
#Syntax:obj=A()
# class A:
#     def add(self,x,y):
#         print("Hello World")
#         print("Good morning")
#         print(x)
#         print(y)
#     def sub(self,a,b):
#         print("Hello")
#         print("java")
#         print(a)
#         print(b)
# obj=A()
# obj.add(10,20)
# obj.sub(30,50)

#2.What is constructor and use with example
#Constructor:It is a special method
#The name constructor should be __init__(self) method
#Syntax:def __init__(self):
#Constructor will be executed only once
#Constructor is an optional anf if we are not providing any constructor the python wil provide default constructor
# class B:
#     def __init__(self,x,y):
#         self.a=x
#         self.b=y
#         print(self.a)
#         print(self.b)
#     def java(self,a,b):
#         print(self.a)
#         print(self.b)
#     def python(self,a,b):
#         print(self.a)
#         print(self.b)
# obj=B(40,50)
# obj.java(10,20)
# obj.python(20,30)

#3.What is the difference between instane method,static method,class method
#Instance Method:The method which conains self as a default parameter is called instance method
#The instance can be access here usig self
#Instance variable we can't access inside the class method and static method
#Class method:The method which we are accessing only class or static variable is called class method
#We can declare class method here @classmethod
#We can accces var using class.varname
#static method:Inside static method we can use any static var and class var
#we can't provide any self or cls as a parameter
#There is no parameters for static method
# class A:
#     x=10
#     def __init__(self):
#         A.y=200
#     def python(self):
#         A.z=500
#         print("instance method",A.z)
#         print("instance method",A.y)
#         print("instance method",A.x)
#         print("instance method self",self.x)
#     @classmethod
#     def add(cls):
#         A.s=300
#         cls.c=400
#         print("class method",cls.c)
#         print("class method",A.s)
#         print("x val:",A.x)
#         print("y val:",cls.x)
#     @staticmethod
#     def print():
#         A.d=600
#         print("static method",A.d)
#         print("x val",A.x)
# obj=A()
# obj.python()
# A.add()
# A.print()

#4.How to access one class data into another class
# class B:
#     def __init__(self,name,address,rno,sal):
#         self.name=name
#         self.address=address
#         self.rno=rno
#         self.sal=sal
#     def python(self):
#         print("dislaying emp data:")
#         print("Name:",self.name)
#         print("address:",self.address)
#         print("rno:",self.rno)
#         print("sal:",self.sal)
# class A:
#     def modify(self,obj_B):
#         print(obj_B.name)
#         print(obj_B.address)
#         print(obj_B.rno)
#         print(obj_B.sal)
# obj=B("Swetha","vijayawada",107,20000)
# obj.python()
# obj_A=A()
# obj_A.modify(obj)

#5.What is inner class and how to access inner class data write two methods
#Inner class:Class inside the class is called inner class

# class A:
#     # def __init__(self):
#     #     self.ob1=self.B()
#     #     self.ob1.java()
#     #     self.ob1.python()
#     def CPP(self):
#         print("Class A CPP functon")
#     def C(self):
#         print("Class A C language")
#     class B:
#         # def __init__(self):
#         #     print("inner class B object created")
#         def java(self):
#             print("inner class B java function")
#         def python(self):
#             print("inner class B python")
# obj=A()
# obj.CPP()
# obj.C()
# obj.B().python()
# obj.B().java()

# class A:
#     def __init__(self):
#         self.ob1=self.B()
#         self.ob1.java()
#         self.ob1.python()
#     def CPP(self):
#         print("Class A CPP functon")
#     def C(self):
#         print("Class A C language")
#     class B:
#         # def __init__(self):
#         #     print("inner class B object created")
#         def java(self):
#             print("inner class B java function")
#         def python(self):
#             print("inner class B python")
# obj=A()
# # obj.CPP()
# # obj.C()
# # obj.B().python()
# # obj.B().java()

#6.What is reference variable how to access data using that
#Self automatically access object
# class A:
#     def python(self):
#         self.x=100
#         a=2000
#         print(self.x)
#         print(a)
#     def python1(self):
#         print(self.x)
# obj=A()
# obj.python()
# obj.python1()



