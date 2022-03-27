n=int(input("Enter any number:"))
i=1
fact=1
while i<=n:
    fact=fact*i
    sum=sum+fact
    i+=1
    print("SUM=",sum)