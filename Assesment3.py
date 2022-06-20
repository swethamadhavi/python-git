#Convert integer into all types
x=10
print(float(x))
print(bool(x))
print(str(x))
print(complex(x))


#Question list index
x=[1,2,3,4,4,5]
print(len(x))
x[0],x[3]=100,100
print(x)


#Find length of the String
str="HELLLO WORDLD"
print(str)
print(len(str))

#We can change tuples values
x=(1,2.6,"Swetha",4.00,1,True,1,1,'A1R3@s')
print(len(x))
x=list(x)
x[1]=4
print(x)
x=tuple(x)
print(x)


#Range of bytearray
0-255
x=[1,2,3,4,5,6,7]
a=bytearray(x)
a[0]=234
a[4]=47
for i in a:
    print(i,end="  ")


#convert a number into float
y="10.30"
print(float(y))
print(y)



#generate 1-10 numbers using rane and print numbers
x=range(1,10)
for i in x:
    print(i,end=" ")


#Output in dynamic way
x="HELLO PYTHON"
print(len(x))
print(x[2:7])
print(x[2:len(x)-5])

