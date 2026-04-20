import math
x=int(input("ENTER NUMBER OF INPUTS(2 0R 3):"))
if(x==3):
   a=int(input("ENTER A:"))
   b=int(input("ENTER B:"))
   c=int(input("ENTER C:"))
   if(a<0 or b<0 or c<0):
      print("NEGATIVE ARGUMENT")
   elif(a==0 or b==0 or c==0):
      print("ZERO ARGUMENT")
   else:
      s=(a+b+c)*0.5
      n=(s*(s-a)*(s-b)*(s-c))
      area=math.sqrt(n)
      print("ARER OF THE TRIANGLE:",n)
elif(x==2):
   h=float(input("ENTER THE HEIGHT OF THE TRIANGLE:"))
   b=float(input("ENTER THE BREADTH OF THE TRIANGLE:"))
   if(h<0 or b<0):
      print("NEGATIVE ARGUMENT")
   elif(h==0 or b==0):
      print("ZERO ARGUMENT")
   else:
      area=(0.5*b*h)
      print("AREA OF THE TRIANGLE:",area)
else:
   print("INVALID...")
