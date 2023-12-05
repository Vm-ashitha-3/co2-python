x=int(input("enter first number"))
y=int(input("enter second number"))
z=int(input("enter third number"))

if (x>y):
  if (x>z):
      print(x,"is biggest")
  else:
    print(z,"is biggest")
else:
    if(y>z):
        if(y>x):
         print(y,"is biggest")
    else:
     print(z,"is biggest")
        
