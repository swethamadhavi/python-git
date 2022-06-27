#Write a program to reverse the string
# str="my name is Swetha"
# y=str.split()
# print(y)
# y=list(reversed(y))
# print(" ".join(y))

#write a program to find highest frequency character in a string
# x="Helloworld"
# char='l'
# count=0
# for i in range(len(x)):
#     if(x[i]==char):
#         count=count+1
# print("The Highest Frequency Character in a string",count)
# print()


#
# #Print the words ending with letter A
# x="Hello Rama NagA is Good RA"
# y=x.split()
# out=[]
# print(y)
# for i in y:
#     if(i.endswith('A')):
#         out.append(i)
# print(out)
# a=' '.join(out)
# print(a)


#To print string into int
# x='1234'
# print(int(x))
#
# #'Amma is MadaM' to fetch palindrome string
# x="Amma is MadaM"
# y=x.split()
# out=[]
# print(y)
# for i in range(len(y)):
#     temp=y[i]
#     temp=temp[::-1]
#     if(temp==y[i]):
#         out.append(temp)
# print(out)

#To print in given string count small and upper letters,special characters,numbers
# x="Hello Kasi Your Salary is $10000"
# upper,lower,special,digits=0,0,0,0
# for i in range(len(x)):
#     if(x[i].isupper()):
#         upper+=1
#     elif(x[i].islower()):
#         lower+=1
#     elif(x[i].isdigit()):
#         digits+=1
#     else:
#         special+=1
# print("Upper case letters:",upper)
# print("lower case letters:",lower)
# print("Digits:",digits)
# print("Special Characters:",special)

#find the sum of ascii value of given string
# x='ABCDE'
# y=sum(ord(ch) for ch in x)
# print("The y value of charcter",y)

# #To find the substring in agiven string and count of 'A'
# x="AAAAABBBCCC"
# y=list(x)
# print(y)
# z=y.count('A')
# print(z)

#To print "Hello World" into "hellO worlD"
# x='Hello World'
# x=x.replace('H','h').replace('o','O',1).replace('W','w').replace('d','D')
# print(x)
#
