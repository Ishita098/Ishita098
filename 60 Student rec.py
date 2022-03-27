n=int(input("How many record you want to enter"))
rec=[]
i=1
while i<n:
    Rollno=int(input("enter roll no.:"))
    Name=input("enter any name:")
    Marks=float(input("enter marks in all 3 subjects:"))
    data=[Rollno,Name,Marks]
    rec.append(data)
    i+=1
while(True):
 print("\nYour choices are:")
 print("1 for printing all record of student and there total marks:\n2 for printing only those record who are passed in 1st div:\n3 for printing only those record who are passed in 2nd div :")
 print("4 for printing only those record who are passed in 3rd div:")
 print("5 for printing record who are fail in all subjects:")
 print("6 for printing record of those students who got marks greater than 150/300")
 print("7 for printing the record of those students who got total marks between 200-250")
 print("8 for exit")
 ch=int(input("Enter your choice:"))



print("\tAll RECORD OF STUDENTS IS:")
print("\tRoll\tname\tmarks")
for x in rec:
    print("\t",x[0],"\t",x[1],"\t",x[2])
print("\tALL EVEN Roll NUMBER RECORD STUDENTS")
print("\tRoll\tname\tmarks")
for x in rec:
    if x[0]%2==0:
     print("\t",x[0],"\t",x[1],"\t",x[2])