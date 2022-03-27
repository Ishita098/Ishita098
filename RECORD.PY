n=int(input("How many record you want to enter"))
rec=[]
i=1
while i<n:
    rno=int(input("enter roll no.:"))
    name=input("enter any name:")
    marks=float(input("enter marks:"))
    data=[rno,name,marks]
    rec.append(data)
    i+=1
print(rec)