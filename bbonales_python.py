
#Bryant Bonales_python6/15/2015


def bigger(a,b):

    if a>b:
        print "%d is greater than %d" %(a,b)
    else:
        print "%d is greater than %d" %(b,a)






#older

x=int(input("Enter 1st Year:"))
y=int(input("Enter 2nd Year:"))
num=2015
age1=num-y
age2=num-x

if x>y:
    print "The person born in %d is older and %d years old" %(y,age1)
elif y>x:
    print "The person born in %d is older and %d years old" %(x,age2)
else:
    print "Same age"



#bigger

x=int(input("Enter Number 1:"))
y=int(input("Enter Number 2:"))
z=int(input("Enter Number 3:"))

if x>y and x>z:
    print "%d is the biggest number" %(x)
elif y>z and y>x:
    print "%d is the biggest number" %(y)
else:
    print "%d is the biggest number" %(z)
