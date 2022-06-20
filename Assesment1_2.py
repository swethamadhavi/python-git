#print all reserved keywors in python
import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))



#initalise all student information and print values and types
name="Swetha"
rollno="11x2478"
address="vijayawada"
phoneno=9912567899
fathername="RangaRao"
age=21
branch="CSE"
percentage=80
print(name)
print(rollno)
print(address)
print(phoneno)
print(fathername)
print(age)
print(branch)
print(percentage)
print(type(name))
print(type(rollno))
print(type(address))
print(type(phoneno))
print(type(fathername))
print(type(age))
print(type(branch))
print(type(percentage))

#program to get substring from string
str="Hello World"
print(len(str))
print(str[0])
print(str[1])
print(str[2])
print(str[3])
print(str[4])
print(str[5])
print(str[6])
print(str[7])
print(str[8])
print(str[9])
print(str[10])
print(str[:1])
print(str[:2])
print(str[:3])
print(str[:4])
print(str[:5])
print(str[:6])
print(str[:7])
print(str[:8])
print(str[:9])
print(str[:10])
print(str[:11])
print(str[:5])
print(str[:11])
print(str[len(str)-1])
print(str[::-5])
print(str[-6:-4])
print(str[::4])

#print first and last value of any given string input=Lemcode
str="Lemcode"
print(len(str))
print(str[1:6])
print(str[1:7])
print(str[::-6])
print(str[::6])
print(str[len(str)-2])



#print letters Hlool in x,print first 3 letters in x,print last 3 letters in x,remove last 3 letters from x,get onlylast ele from x,get only ll from x
x="Helloworld"
print(len(x))
print(x[::2])
print(x[:3])
print(x[7:10])
print(x[:-3])
print(x[len(x)-1])
print(x[2:4])


#list concatenation,multiplication
x=[10,33.5,'swetha',33]
print(x)
y=[4,577.8,"madhavi"]
print(y)
x=x+y
print(x)
print(x[2])
print(y[-3])
print(y[len(y)-1])
x=x*2
print(x)




#print bytes example
a=[1,3,5,7]
x=bytes(a)
print(x[3])
print(x[-1])



#print bytesarray example
a=[1,2,3,4]
x=bytearray(a)
x[1]=44
for i in x:
    print(i,end=" ")