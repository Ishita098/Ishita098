year=int(input("Enter year:"))
if (year % 400 == 0) and (year % 100 == 0):
    print("This is a leap year")
else:
    print("This is not a leap year")