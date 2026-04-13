class person:
   def __init__(point,name,age,weight,height):
      point.name=name
      point.age=age
      point.weight=weight
      point.height=height
   def display_details(point):
      print "DETAILS..."
      print "NAME:",point.name
      print "AGE:",point.age
      print "WEIGHT:",point.weight,"Kg"
      print "HEIGHT:",point.height,"Ft"
   def get_bmi_result(point):
      h=(point.height*0.3048)
      bmi=(point.weight/(h**2))
      if(bmi<18.5):
         print "UNDERWEIGHT..."
      elif(18.5<=bmi<=25):
         print "HEALTHY..."
      else:
         print "OBIES..."
obj=person('Chanasya',19,48,5)
obj.display_details()
obj.get_bmi_result()
