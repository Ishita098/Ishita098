n=int(input("How many record you want to enter"))
rec=[]
i=1
while i<n:
    Rollno=int(input("enter roll no.:"))
    Name=input("enter any name:")
    Fees=float(input("enter fees:"))
    data=[Rollno,Name,Fees]
    rec.append(data)
    i+=1
print("\tAll RECORD OF STUDENTS IS:")
print("\tRoll\tname\tmarks")
for x in rec:
    print("\t",x[0],"\t",x[1],"\t",x[2])
print("\tALL EVEN Roll NUMBER RECORD STUDENTS")
print("\tRoll\tname\tmarks")
for x in rec:
    if x[0]%2==0:
     print("\t",x[0],"\t",x[1],"\t",x[2])
    