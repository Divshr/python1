#1)factorial using recursion

def r_fact(n):
    if n==1:
        return n
    else:
        return n*r_fact(n-1)

n=int(input("Enter the number: "))
if n<0:
    print("negative number")
elif n==0:
    print("factorial of 0 is 1")
else:
    print("factorial of ",n ,"is", r_fact(n))

#2) factorial of a number
n=int(input("Enter the number: "))
fact=1
if n<0:
    print("negative number")
elif n==0:
    print("factorial of 0 is 1")
else:
    for i in range(1, n+1):
        fact=fact*i
    print("factorial of ", n, "is", fact)


#3) Area of triangle,square,rectangle

def area(name):

    name=name.lower()

    if name == "rectangle":
        l=int(input("Enter the length: "))
        b=int(input("Enter the breadth: "))

        r_area=l*b
        print("The area of rectangle: ",r_area)

    elif name == "square":
        l = int(input("Enter the length: "))

        s_area = l * l
        print("The area of square: ", s_area)

    elif name == "triangle":
        h=int(input("Enter the height: "))
        b=int(input("Enter the breadth: "))

        t_area=0.5*h*b
        print("The area of triangle: ",t_area)

    else:
        print("Enter the only following options Triangle,rectangle,Square")

if __name__=="__main__":
    print("calculate area")
    shape_name = input("Enter the shape you want to find the area: ")

    area(shape_name)

#4) Multiple and multilevel inheritance

class Class1:
    def m(self):
        print("In class1")

class Class2(Class1):
    def m(self):
        print("In class2")

class Class3(Class1):
    def m(self):
        print("In class3")

class Class4(Class2, Class3):
    pass

obj= Class4()
obj.m()


#5)Sum of natural numbers

n=int(input("Enter the number: "))

if n<0:
    print("Enter the positive number")
else:
    sum = 0
    while(n>0):
        sum=sum+n
        n=n-1
    print("The sum is ",sum)