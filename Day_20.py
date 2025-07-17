#list and tuples practcie revision
stu=["ammu",12,"Delhi"] #list

print(stu[0:]) #slicing so here it prints elements from 0 index to len(stu) i.e, entire list
stu[1]=15 #Mutable property

stu.append("cse") #Adds element at the end
print(stu)

print(stu[0:2]) 

stu[0]=12 #mutable property
stu[3]=1
stu[2]=7
print(stu)

stu.sort()  #sorting (Default ascending)
print(stu)

stu.sort(reverse=True) #sorting (Reveerse the default i.e, descending)
print(stu)

stu.pop(2) #pop -  remove the element by providig index
print(stu)



#type casting
a=2
b=float("2.4")
sum=a+b
print(sum)


a=2
b="4"
c=int(b)
sum=a+c
print(sum)
print(type(a))
print(type(b))
print(type(c))