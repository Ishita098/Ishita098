n=int(input("Enter any number"))
i=1
esum=0
osum=0
while i<=n:
    if i%2==0:
       esum=esum+i
    else:
        osum=osum+1
    i+=1
print("Esum=",esum)
print("Osum",osum)