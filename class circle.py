class circle:
   def get_radius(point):
      point.radius=int(input("ENTER RADIUS:"))
   def cal_area(point):
      a=3.14*point.radius*point.radius
      print "AREA OF THE CIRCLE:",a
   def cal_circumference(point):
      c=2*3.14*point.radius
      print "CIRCUMFERENCE OF THE CIRCLE:",c
d=circle()
d.get_radius()
d.cal_area()
d.cal_circumference()
