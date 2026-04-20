import math
p=float(input("ENTER PRICIPLE AMOUNT:"))
n=float(input("ENTER NUMBER OF YEAR:"))
r=float(input("ENTER RATE OF INTEREST:"))
t=float(input("ENTER NUMBER OF OCCURANCE:"))
s=(p*n*r)/100
print (" SIMPLE INTEREST:",s)
z=(r*n)/100
y=n*t
x=(1+z)**y
c=p*x
d=c-p
print (" COMPOUND INTEREST: ",d)
