##1) Arithmetic operation
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

print("Enter the operator (+,-,/,*): ")
ch = input()

if ch=='+':
    print("sum: ", add(2,5))
elif ch=='-':
    print("substraction: ", sub(2,5))
elif ch=='*':
    print("multiplication: ", mul(2,5))
elif ch=='/':
    print("division: ", div(10,5))
else:
    print("Invalid operator")


##2) Binary sort
def binary_sort(a,val,first,last):
    if first==last:
        if a[first]>val:
            return first
        else:
            return first+1
    if first>last:
        return first
    mid = (first+last)//2
    if a[mid]< val:
        return binary_sort(a,val,mid+1,last)
    elif a[mid]> val:
        return binary_sort(a,val,first,mid-1)
    else:
        return mid

def sort(a):
    for i in range(1, len(a)):
        val = a[i]
        j = binary_sort(a, val, 0, i-1)
        a = a[:j] + [val] + a[j:i] + a[i + 1:]
    return a

print("Binary sorted array: ")
print(sort([10, 34, 2, 4, 6, 8, 32, 67]))


#3)
def table(n):
    return lambda a:a*n
n=2
b=table(n)
for i in range (1,11):
    print(n,"*" ,i, "=" ,b(i))

#4)
num = int(input("enter the number: "))
factors=[]
for i in range(1, num+1):
    if num % i ==0:
        factors.append(i)
print("Factors of {} = {}".format(num,factors))

#5)
import math
num = float(input("Enter the number: "))
Squareroot = math.pow(num,0.5)
print("The square root of a given number{0}={1}".format(num,Squareroot))

#6)
num=int(input("Enter the number: "))

flag=False

if num>1:
    for i in range(2, num):
        if(num % i) == 0:
            flag=True
            break
if flag:
    print(num, "is not a prime numbers")
else:
    print(num, "is a prime numbers")
