n=int(input("enter the number(n):"))
sum=0
for i in range(1,n+1):
    print(n,"**",i,"=",n**i)
    sum+=n**i
print(sum)
