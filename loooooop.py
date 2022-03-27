n=int(input("Enter any number"))
i=1
sum=0
while i<=n:
    if i%2==0:
       sum=sum-i
    else:
        sum=sum+1
    i+=1
print("sum=",sum)
