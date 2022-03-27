ls=[67,23,45,567,69,27,16,98,49]
print(ls)
print("All objects of list are:")
for x in ls:
    print (x)
print("All even object element are:")
for x in ls:
    if x%2==0:
        print (x)
print("ALL odd object element are:")
for x in ls:
    if x%2!=0:
        print(x)
