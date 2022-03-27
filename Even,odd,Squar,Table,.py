while(True):
 print("\nYour choices are:")
 print("1 for even:\n2 for Odd:\n3 for Square:")
 print("4 for Table:")
 print("5 for exit:")
 ch=int(input("Enter your choice:"))
 if ch==1:
     n=int("Enter any value:")
     for i in range(2,n+1):
       j=2*i
       print(j)
     
 elif ch==2:
      n=int("Enter any value:")
      for i in range(1,n+1):
          j=2*i-1
          print(j)
 elif ch==3:
      n=int("Enter any value:")
      for i in range(1,n+1):
          j=i*i
          print(j)
     
 elif ch==4:
     n=int(input("enter any number:"))
     i=1
     sum=0
     while i<=10:
        j=n*i
        print(n,"*",i,"=",j)
        sum=sum+j
        i+=1
        print("SUM=",sum)
 elif ch==5:
     break
 else:
        print("You are wrong person")
