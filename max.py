x=int(input("ENTER THE FIRST NUMBER:"))
y=int(input("ENTER THE SECOND NUMBER:"))
z=int(input("ENTER THE THIRD NUMBER:"))
if(x>y and x>z):
   print("LARGEST NUMBER:",x)
elif(y>x and y>z):
   print("LARGEST NUMBER:",y)
else:
   print("LARGEST NUMBER:",z)
