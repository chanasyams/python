import math
a=int(input("ENTER A:"))
b=int(input("ENTER B:"))
c=int(input("ENTER C:"))
e=((b*b)-(4*a*c))
if(e==0):
   x=(-b/(2*a))
   print ("REAL AND EQUAL ROOTS:",x)
elif(e>0):
   s=math.sqrt(e)
   x=((-b+s)/(2*a))
   y=((-b-s)/(2*a))
   print ("REAL AND DISTINCT ROOTS:",x,",",y)
else:
   s=math.sqrt(-e)
   x=(-b/(2*a))
   y=s/(2*a)
   print ("COMPLEX ROOTS:",x,"+j",y,",",x,"-j",y)
[23bee002@mepcolinux ~]$python3 eqn.py
