#Remove the duplicates elements from list without using set
# x=[1,2,3,4,1,2,5,6]
# out=[]
# for i in x:
#     if i not in out:
#         out.append(i)
# print(out)

#Using set
# x=[1,2,3,4,1,2,5,6]
# x=set(x)
# x=list(x)
# print(x)

#Count the each element how many times it is exists
# x=[1,2,3,4,1,2,5,6]
# for i in x:
#     if i in x:
#         print(i,x.count(i))
# print()

# x=[1,2,3,4,1,2,5,6]
# y={}
# for i in x:
#     if i in y:
#         y[i]+=1
#     else:
#         y[i]=1
# print("count no of elements in list:",y)


#Sorting the elements in list without sort
# x=[10,2,4,3,5]
# for i in range(len(x)):
#     for j in range(i+1,len(x)):
#         if(x[i]>x[j]):
#             x[i],x[j]=x[j],x[i]
# print(x)

#using sort()
# x=[10,2,4,3,5]
# x.sort()
# print(x)

#print only even numbers using list comprehension
# x=[1,3,2,4,5,7,6,8]
# x=[x[i] for i in range(len(x)) if x[i]%2==0]
# print(x)


#Write a program to print even and its position in another list
# x=[1,3,2,4,5,7,6,8]
# y=[]
# for i in range(len(x)):
#     if(x[i]%2==0):
#        y.append(x[i])
#        y.append(i)
# print(y)

