
def fun1(): #non return type function
    
    a=int(input("Enter a:"))
    b=int(input("Enter b:"))
    c=a+b
    print("Sum of ",a," and ",b," is ",c)

def fun2(): #return type function
    
    a=int(input("Enter a:"))
    b=int(input("Enter b:"))
    c=a-b
    return c


fun1()  #calling function
    
print("Sub = ",fun2())    
