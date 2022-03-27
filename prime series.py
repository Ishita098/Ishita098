n = int(input("Enter Number upto: "))
i=2
while i<=n:
    j=2
    while j<i:
        if i%j==0:
            break
        j+=1
    if j==i:
            print(i)
    i+=1

   