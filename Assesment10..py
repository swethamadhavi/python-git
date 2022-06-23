#Print 1 to 10 numbers in that pattern
# count=1
# for i in range(1,5):
#    for j in range(1,i+1):
#       print(count,end=' ')
#       count=count+1
#    print()

#Write a compare to compare two strings
# x="Hello world"
# y="java"
# if(len(x)==len(y)):
#    if(x==y):
#       print("Both are equal")
#    else:
#       print("Both are unequal")
# else:
#    print("Both are unequal")

#Write a program to print fibonacii series
# n=int(input("Enter n values:"))
# a=0
# b=1
# count=0
# if(n==1):
#    print(a)
# else:
#    print("Fibonacii Series:")
#    while(count<n):
#       print(a)
#       c=a+b
#       a=b
#       b=c
#       count+=1

#write a program to finf palindrome in list and find biggest largest number in list
# x=[11,43,67,99,22,223]
# y=[]
# for i in x:
#    temp=i
#    s=0
#    while(i>0):
#       r=i%10
#       s=s*10+r
#       i=i//10
#    if(s==temp):
#       y.append(s)
# print(y)
# print(max(y))

#write a program to given number is prime or not
# num=int(input("Enter a number:"))
# if(num>1):
#    for i in range(2,num):
#       if(num%i==0):
#          print("%d is Not prime number" %num)
#          break
#    else:
#       print("%d is a prime number" %num)

#write a program to print name in this pattern
# x="SWETHA"
# for i in range(len(x)):
#    for j in range(i+1):
#       print(x[j],end=' ')
#    print()

#Write a program to find second largest number in x
# x=[11,43,67,999,22,223]
# x.sort()
# print("The Second largest number is",x[-2])