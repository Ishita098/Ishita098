n=int(input("enter any number:"))
i=1
fact=1
sum=0
while i<=n:
    fact=fact*i
    if i%2==0:
        sum=sum-fact
    else:
        sum=sum+fact
    i+=1
print("SUM=",sum)

