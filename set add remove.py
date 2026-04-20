def adding(s,val):
   if val in s:
      print("ALREADY EXIST...")
   else:
      s.add(val)
      print("AFTER ADDING : ",s)
def delete(s,val):
   if val in s:
      s.remove(val)
      print("AFTER REMOVING:",s)
   else:
      print("ELEMENT NOT EXIST...")
lst=input("ENTER VALUES WITH COMMA SEPERATED: ").split(',')
s=set()
for i in lst:
   s.add(int(i))
print("ORIGINAL SET: ",s)
v1=int(input("ENTER VALUE FOR ADDING: "))
adding(s,v1)
v2=int(input("ENTER VALUE FOR REMOVING: "))
delete(s,v2)
