def sums(lst1):
    add=0
    for i in lst1:
        add=add+i
    return add
num=int(input("ENTER RANGE:"))
d=dict()
for j in range (1,num+1):
    d[j]=j*j
print "DICTIONARY: ",d
lst=list(d.values())
a=sums(lst)
print "SUM OF VALUES: ",a
