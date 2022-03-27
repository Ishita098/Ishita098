for x in range(1,11):
    for y in range(1,11):
        for z in range(1,11):
            print(x," ",y,"",z)
            if z>=1:
                break
        if y>=2:
                break
    if x>=3:
            break