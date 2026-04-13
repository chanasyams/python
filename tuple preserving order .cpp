tuple1=(10,20,30,40,10,60,20,80)
unique=[]
for i in tuple1:
   if i not in unique:
      unique.append(i)
t=tuple(unique)
print "PRESERVING ORDER...",t
