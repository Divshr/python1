##1)arithmetic operations

a=10
b=40
sum=a+b
print("sum: ",sum )

sub=a-b
print("sub: ",sub)

mul=a*b
print("mul: ",mul)

div=b/a
print("div: ",div)

##Assignment operators

a=10
b=a
print(b)

a=2
a+=3
print(a)


##logical operators
a=8
print(a>2 and a<10)

a=8
print(a>2 or a<10)

a=8
print(not(a>2 and a<10))

##2) program to check odd or even number

num=15
if(num % 2) == 0:
    print("number is even")
else:
    print("number is odd")

##3) Program to check leap year

year=2021

if(year%4)==0:
    print(year,"is leap year")
if(year%400)==0:
    print(year,"is leap year")
if (year % 100) == 0:
    print(year, "is leap year")
else:
    print(year, "is not a leap year")


##4) list functions
list=[1,2,3,4,5,6,7,8]
print(list)

print(list[0:5])

list[1]=0
print(list)

list.remove(8)
print(list)

list1=[]
list1.append(list)
print(list1)

print(len(list))

##5)

i = 1
for i in range(1,10):
    print(i)

i=1
while i<11:
    print(i)
    i=i+1

