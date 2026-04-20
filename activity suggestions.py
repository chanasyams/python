t=str(input("ENTER TEMPERATURE(WARM OR COLD):"))
h=str(input("ENTER HUMIDITY(DRY OR HUMID):"))
if(t=="Warm"):
   if(h=="Dry"):
      print("PLAY BASKETBALL")
   elif(h=="Humid"):
      print("PLAY TENIS")
elif(t=="Cold"):
   if(h=="Dry"):
      print("PLAY CRIKET")
   elif(h=="Humid"):
      print("SWIM")
else:
   print("INVALID")

