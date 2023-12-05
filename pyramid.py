rows=int(input("enter a number"))
for i in range(rows+1):
    for j in range(1,i+1):
        print(j*i,end="")
    print("")
