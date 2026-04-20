a=input("ENTER SET1 ELEMENTS: ")
set1=set(a.split(','))
b=input("ENTER SET1 ELEMENTS: ")
set2=set(b.split(','))
print("SET1= ",set1)
print("SET2= ",set2)
c=set1.issubset(set2)
if (c==True):
   print("SET1 IS A SUBSET OF SET2...")
else:
   print("SET1 IS NOT A SEBSET OF SET2...")
d=set2.issubset(set1)
if(d==True):
   print("SET2 IS A SUBSET OF SET1...")
else:
   print("SET2 IS NOT A SEBSET OF SET1...")
