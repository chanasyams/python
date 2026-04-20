n=int(input("ENTER NUMBER: "))
temp=0
for x in range(2,n-1):
    if(n%x==0):
        temp=1
    break
if(temp==1):
    print ("NOT A PRIME NUMBER")
else:
    print ("PRIME NUMBER")
