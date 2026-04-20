def add_key(d):
    key = int(input("ENTER NEW KEY: "))
    value = int(input("ENTER NEW VALUE: "))
    d[key] = value
    return d
def sort_value(item):
    return item[1]
d = {}
n = int(input("ENTER NUMBER OF PAIRS: "))
for i in range(n):
    k = int(input("ENTER KEY: "))
    v = int(input("ENTER VALUE: "))
    d[k] = v
print("Original Dictionary:", d)
asc_list = dict(sorted(d.items(), key=sort_value))
print("Ascending Order:", asc_list)
asc = dict(asc_list)
asc = add_key(asc)
print("After Adding New Key:", asc)
desc= dict(sorted(asc.items(), key=sort_value, reverse=True))
print("Descending Order:", desc)
