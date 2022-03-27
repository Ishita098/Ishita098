from errno import EROFS
from ftplib import error_perm


n=int(input("Enter any number:"))
i=1
rev=0
m=n
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
if m==rev:
    print("Palandrome.....")
else:
    print("non palandrome.....")
print("REVERSE=",rev) EROFS
