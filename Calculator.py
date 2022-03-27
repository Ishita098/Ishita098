while(True):
 print("\nYour choices are:")
 print("1 for Addition:\n2 for substraction:\n3 for Multiplication:")
 print("4 for Division:\n5 for modulas:\n6 for floor:")
 print("7 for exit:")
 ch=int(input("Enter your choice:"))
 if ch==1:
     a=float(input("Enter first number:"))
     b=float(input("Enter second number:"))
     c=a+b
     print("Addition=",c)
 elif ch==2:
     a=float (input("Enter first number:"))
     b=float(input("Enter second number:"))
     c=a-b
     print("Substraction:",c)
 elif ch==3:
     a=float (input("Enter first number:"))
     b=float(input("Enter second number:"))
     c=a*b
     print("Multiplication:",c)
 elif ch==4:
     a=float (input("Enter first number:"))
     b=float(input("Enter second number:"))
     c=a/b
     print("Division:",c)
 elif ch==5:
     a=float (input("Enter first number:"))
     b=float(input("Enter second number:"))
     c=a%b
     print("Modulas:",c) 
 elif ch==6:
     a=float (input("Enter first number:"))
     b=float(input("Enter second number:"))
     c=a//b
     print("Floor:",c) 
 elif ch==7:
     break
 else:
        print("You are wrong person")

