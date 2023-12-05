list=[]
n=int(input("enter number of elements:"))
for i in range(o,n):
    x=int(input())
    if x>=100:
        x='over'
        list.append(x)
        print(list)
