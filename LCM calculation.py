num1=int(input("ENTER NUMBER1:"))
num2=int(input("ENTER NUMBER2:"))
if(num1>num2):
   big=num1
else:
   big=num2
while True:
   if(big%num1==0 and big%num2==0):
      print("LCM OF THE GIVEN NUMBER:",big)
      break
   big+=1
