n=int(input("Enter any number:"))
i=1
sum=0
while i<=n:
    j=2*i
    if i<n:
        print(j,end="+")
    else:
        print(j,end="=")
    sum=sum+j
    i+=1
    print(sum)