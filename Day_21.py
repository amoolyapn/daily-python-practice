#Tuples practice
tuple = ()

t=(1) # here the single element acts as a list not tuple
t0=(1,) # for single element we need to add , and it becomes tuple
t1 = (1,2,3)
t2=(1,"Hello",3.14)
print(type(1))
print(type(t0))
print(t1)
print(t2)


#Accessing elements from tuple
a=(10,20,30,40,50)
print(a[1])
print(a[3])
print(a[0:])
print(a[0:2])


#Tuple Operations

t1 = (1, 2, 3)
t2 = (4, 5)

t3 = t1 + t2     # Concatenation

t4 = t1 * 2      # Repetition

print(2 in t1)   # Membership test

print(len(t1)) 


# Iteration
for item in t1:
    print(item)



#Tuple Methods

t = (1, 2, 2, 3)

print(t.count(2))  #returns 2
print(t.index(3))  #index is 3


#unpacking Tuple
t = (10, 20, 30)
a, b, c = t
print(a)  # 10
print(b)  # 20
print(c)  # 30



#Using functions in tuples - returns value
#1
def min_max(nums):
    return min(nums), max(nums)

result = min_max([3, 5, 1, 9])
print(result)          # (1, 9)
min_val, max_val = result
print(min_val, max_val)  # 1 9


#2
def operations(a,b):
  sum=a+b
  sub=a-b
  div=a/b
  prod=a*b
  return sum,sub,div,prod

results=operations(10,5)
print(results)
print(results[0])


#Nested tuples
tuple=((1,2,3,4),(5,6,7,8))
print(tuple[0])
print(tuple[1])
print(tuple[0][1])


#conversion and adding element
family=("ammu","Paru","Aishu","Laki")     #tuple
temp=list(family)     #tuple converted to list
temp.append("Gowthu")
temp.append("Chithra")
temp[0]="Ammu"
family=tuple(temp)  #list again converted back to tuple
print(family)


#indexing
tuple=(11,22,33,44,55,66,66)
res=tuple.index(66,0,6)
print(res)

t=(11,22,33,33,55,66,77)
res=t.index(33,0,4)
print("Index of 33:",res)


