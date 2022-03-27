#greeting="good morning,"
#name="harry"
#print(type(name))
#concatenating two strings
#c=greeting+name
#print (c)
name="harry"
#print(name[4])
#name[3]="d"--> does not work
#print(name[1:3])
print(name[0:])#same as name[0:4]
print(name[:4])#same as name[0:4]
print(name[1:])#same as name[1:5]
#negative indices
c=name[-4:-1]#is same as name[1:4] i.e 1 to 3
print(c)
#skipping the values
name="HARRYISGOOD"
D=name[0::2]
print(D)

name="AMAZING"
D=name[0::2]
print(D)

name="AMAZING"
D=name[1:6:2]
print(D)