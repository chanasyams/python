n=raw_input("ENTER ELEMENTS: ").split()
t=tuple(n)
print t
x=int(input("ENTER 1ST INDEX: "))
y=int(input("ENTER 2ND INDEX: "))
print "AFTER SLICING...: ",t[x:y]
