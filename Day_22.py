X=int(input("Enter the number:"))
match X:
    case 0:
        print("Value is 0");
    case 1:
        print("value is 1");
    case _:
        print("Default case!!");


name= "Ammu"
for i in name:
    print(i)


#multiplication table
#Break
n = int(input("Enter the value: "))
for k in range(12):
    if(k==10):
        break
    print(n,"x",k+1,"=",n*(k+1))


#multiplication table
#Continue
n = int(input("Enter the value: "))
for k in range(12):
    if(k==10):
        print("Skip")
        continue
    print(n,"x",k+1,"=",n*(k+1))


#Function
a = int(input("Enter a value:"))
b = int(input("Enter b value:"))
def sum(a,b):
    sum = a+b
    print(sum)
    if (a>b):
        print("A is greater")
    elif (a<b):
        print("B is greater")
    else:
        print("Equal")
sum(a,b)


#Return statement
#1
def average(*numbers):
    sum=0
    for i in numbers:
        sum = sum+i
    return sum/len(numbers)
c = average(5,6,7,8)
print(c)


#2
def avg(nums):
    sum = 0
    for i in nums:
        sum = sum+i
    return sum/len(nums)
c = avg([1,2,3])
print(c)


#List [] - mutable
list = [i*i  for i in range(5)]
list.append(7)
print(list)

list = [i*i for i in range(10) if i%2==0]
print(list)

lst = [1,5,33,66,7,5,2,66]
lst.sort()
lst.reverse()
lst.index()
lst.count()
list = lst
list[5]=5
print(list)
#or 
list = lst.copy()
print(list)


#Tuples () - immutalbe
alphabets= ("a","B","c","d","e","f")
temp=list(alphabets)
temp.append("g")
alphabets=tuple(temp)
print(alphabets)


#f-strings
name="Ammu"
city="Tumkur"
print(f"My name is {name} and im from {city}")

#doc-strings
def sum(a,b):
    ''' Sum of a and b'''
    sum = a+b
    print(sum)
sum(2,6)
print(sum.__doc__)


#Recurssion
#Factorial
n=int(input("Enter n value: "))
def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
print(factorial(n))


#Fibanocci series
n=int(input("Enter n value:"))
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print(fib(n))



#Enumerate - used to get index and value at a same time
fruits=['apple','kiwi','mango','grapes']
for index,fruit in enumerate(fruits):
    print(index,fruit)