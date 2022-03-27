n = int(input("Enter Number upto: "))
count=1
i=2
while count<n:
    j=2
    while j<i:
        if i%j==0:
            break
        j+=1
    if j==i:
            print(i)
            count+=1
    i+=1