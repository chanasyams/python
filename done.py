lst = []
print "TO FINISH TYPE 'done'...."
while True:
   item = raw_input("ENTER ELEMENT: ")
   if (item.lower() == 'done'):
      break
   lst.append(item)
tup=tuple(lst)
print "CREATED TUPLE:",tup
