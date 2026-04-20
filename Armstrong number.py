num=int(input("ENTER NUMBER:"))
temp1=num
count=0
digit=0
armstrong=0
while temp1>0:
   count+=1
   temp1//=10
temp2=num
while temp2>0:
   digit=temp2%10
   armstrong+=digit**count
   temp2//=10
if(num==armstrong):
   print("THE GIVEN NUMBER IS ARMSTRONG")
else:
   print("THE GIVEN NUMBER IS NOT ARMSTRONG")
