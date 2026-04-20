def exist(s,elem):
   if elem in s:
      print("ELEMENT EXIST...")
   else:
      print("ELEMENT NOT EXIST...")
n=int(input("ENTER NO. OF ELEMENTS:"))
lst=[]
for i in range(n):
   lst.append(int(input("ENTER VALUES:")))
s=set(lst)
for i in lst:
   s.add(int(i))
print("CREATED SET: ",s)
a=len(s)
print("LENGTH OF THE SET: ",a)
val=int(input("ENTER ELEMENT TO CHEACK: "))
exist(s,val)
