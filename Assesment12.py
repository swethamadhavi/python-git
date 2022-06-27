#To find unique elements in the string
# x="Hellooooworld"
# y=list(x)
# print(y)
# y=set(x)
# print(y)
# m=list(y)
# print(m)
# z="".join(y)
# print(z)

# x="HELLLOworld"
# unique_elements=" "
# for element in x:
#     if(element not in unique_elements):
#         unique_elements+=element.casefold()
# print("The unique_elements are:{}".format(unique_elements))
# print()

#using the title case
# x="helloworld program"
# y=x.split()
# print(y)
# y=x.title()
# print(y)

#Reversing a string
# x="Swetha madhavi"
# print(x[::-1])

# x="Swetha madhavi"
# x=list(x)
# x.reverse()
# x=''.join(x)
# print(x)

#print a string in n times
# x="swetha"
# print(x*5)

#swap values between two variables
# x="swetha"
# y="madhavi"
# print(x,y)
# x,y=y,x
# print("x value is",x)
# print("y value is",y)

#combining a list of strings into a single string
# x=['a','b','c','d','e','f']
# y=''.join(x)
# print(y)

#split a string into list of substrings
# x="HelloWorld"
# x=list(x)
# print(x)

#list comprehension
# x=[1,2,3,4,5]
# x=[i*i for i in x]
# print(x)

#check string is palindrome or not
# x="abcdcba"
# if(x==x[::-1]):
#     print("{} is a palindrome".format(x))
# else:
#     print("{} is not palindrome".format(x))

# x="abcdcba"
# x=list(x)
# x.reverse()
# y=''.join(x)
# print(y)
# if(y==x):
#     print("{} is a palindrome".format(y))
# else:
#     print("{} is a palindrome".format(y))

#frequency of elements in a list
# import collections
# x=[10,40,4,5,4,5,6,8,10]
# y=collections.Counter(x)
# print("The frequency of list elements are:",y)

#To find whether two strings are anagrams
# x="ABCD"
# y="DCBA"
# if((x)==y):
#         print("Both are Anagrams")
# else:
#         print("Both are not Anagrams")

#Merging 2 dictionaries
# x={'a':10,'b':20}
# y={'m':20,'n':30}
# print(x|y)