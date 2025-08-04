#Loops -day 3 revision
for i in range(3):
  print(i)


i=0
while i<=5:
  print("Hello")
  i+=1


def greet(name):
  return "Hello"+name
print(greet("Amoolya"))


#lambda function
square= lambda x: x*x
print(square(5))

#pattern
n=5
for i in range(1,n+1)
print("*"*i)

#Factorial
def factorial(n):
  if (n==0 or n==1):
    return 1
  else:
    return n*factorial(n-1)
print(factorial(5))


#Prime numbers
def is_prime(n):
  if n<2:
    return False
  for i in range(2,int(n**0.5)+1):
    if n%i==0:
      return False
  return True
print(is_prime(11))


#sum of digits
def sum_digits(n):
  total=0
  while n>0:
    total+=n%10
    n//=10
  return total
print(sum_digits(123))
