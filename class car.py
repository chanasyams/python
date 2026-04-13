class vechicle:
   def get_details(point,name,model,year,colour):
      point.name=name
      point.model=model
      point.year=year
      point.colour=colour
   def print_details(point):
      print "DETAILS OF THE CAR...."
      print "NAME:",point.name
      print "MODEL:",point.model
      print "YEAR:",point.year
      print "COLOUR:",point.colour
car=vechicle()
car.get_details('thar','mahindra','2022','black')
car.print_details()
