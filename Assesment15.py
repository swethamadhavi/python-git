#1.Write a function tho check Whether the given number is prime or not
# n=int(input("Enter a number:"))
# def prime(n):
#     if(n>1):
#         for i in range(2,n):
#             if (n%i==0):
#                 print("{} is not prime number".format(n))
#                 return n
#             else:
#                 print("{} is prime number".format(n))
#                 break
# prime(n)

#2.x=[121,24,55,7,9] to fetch palindrome number
# x=[121,24,55,7,9]
# out=[]
# def palindrome(x):
#     for i in x:
#         s=0
#         temp=i
#         while(i>0):
#             r=i%10
#             s=s*10+r
#             i=i//10
#         if(temp==s):
#             out.append(temp)
# palindrome(x)
# print(out)
# out.sort()
# print(out[2],out[3])

#3.x={'A':100,'B':200}
# x={'A':100,'B':200}
# def add():
#     keys=list(x.keys())
#     print(keys)
#     values=list(x.values())
#     print(values)
#     z=dict(zip(values,keys))
#     print(z)
# add()


#4.x=[1,2,3,5] add 10 to each element in list using lambda function
# x=[1,2,3,5]
# z=[]
# def add(x):
#   y=lambda i:i+10
#   for i in x:
#     z.append(y(i))
# add(x)
# print(z)

#5.x=[[1,2,3],[4,5,6],[1,2,3]] unique elements from list
# x=[[1,2,3],[4,5,6],[1,2,3]]
# out=[]
# def unique(x):
#     for i in x:
#         if i not in out:
#             out.append(i)
# unique(x)
# print(out)

#6.Type of functions with example
#without args with return val
# def add():
#     print("good")
#     print("Hello")
# add()

#Without args with return val
# def sub():
#     a=10
#     b=20
#     return a-b
# c=sub()
# print(c)

#with args with return val
# def add(x,y):
#     return x+y
# c=add(10,20)
# print(c)

#with args without return val
# def mul(x,y):
#     print(x*y)
# mul(10,20)

#Formal Arguments,Actual arguments
# def add(a,b,c,d):
#     a=a+10
#     b=b+10
#     c=c+10
#     d=d+10
#     return a,b,c,d
# k,l,m,n=add(10,20,30,40)
# print("k val",k)
# print("l val",l)
# print("m val",m)
# print("n val",n)

#Positional arguments
# def add(x,y):
#     print("x val",x)
#     print("y val",y)
# add(20,30)

#Keyword Arguments
# def mul(a,b):
#     print("a val",a)
#     print("b val",b)
# mul(a=20,b=50)

# #Default arguments
# def sub(a=10,b=20,c="java"):
#     print("a val", a)
#     print("b val",b)
#     print("c val", c)
# sub(30,40,60)

#variable length arguments
# def add(*a):
#     return a
# x=add(2,4,8)
# print(x)

#keyword variable arguments
# def java(**a):
#     return a
# x=java(a=10,b=8,c=30,d=78)
# print(x)

#Lambda function
# def mul(x,y):
#     return x+y
# c=lambda x,y:x if(x>y) else y
# print(c(20,30))

#7.Filter,map,reduce with syntax and example
#Filter:It will take 2 arguments one is function and another one list it will filter particular element
#syntax:var_name=list(filter(fun,iterable_obj))
# x=list(range(1,5))
# print(x)
# a=list(filter(lambda i:i%2!=0,x))
# print(a)

#Map:Map will apply on each and every element on list will modify all the element and generate new element
#syntax:var_name=map(fun,sequence)
# x=list(range(1,11))
# a=list(map(lambda i:i-10,x))
# print(a)

#Reduce:Reduce the sequence of elements into single element by applying specific function
#syntax:reduce(fun name,sequence)
#If we want to reduce we used import module called functools
# from functools import reduce
# x=list(range(1,11))
# print(x)
# x=[2,5,6,7]
# z=reduce(lambda a,b:a*b,x)
# print("sum",z)