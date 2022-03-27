p=int(input("Enter the marks of physics: "))
c=int(input("Enter the marks of chemistry: "))
m=int(input("Enter the marks of maths: "))
if p<33:
    if c<33:
        if m<33:
            print("Fail in all subjects...")
	else:
	    print("Fail in two subjects...")
    elif m<33:
        print("Fail in two subjects...")     
    else:
        print("Fail in two subjects...")    
elif c<33:
    if m<33:
        print("Fail in two subjects...")
    else:
        print("Fail in one subject...")
elif m<33:
       print("Fail in one subject...")
else:
    total=p+c+m
    per=total/3
    print("Total marks=",total)
    print("Total percentage=",per)
    if per>=60:
       print("Pass in first div...")
    elif per>=45:
       print("Pass in second div...")
    else:
       print("Pass in third div...")2