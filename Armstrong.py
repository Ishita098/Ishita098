n=int(input("Enter any number:"))
i=1
sum=0
m=n
while n>0:
    r=n%10
    k=r*r*r
    sum=sum+r
    n=n//10
if m==sum:
    print("Armstrong.....")
else:
    print("not armstrong....")
print("SUM=",sum)