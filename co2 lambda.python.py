print("lambda function to find areas os square,rectangle,triangle")
print("area of rectangle")
rect = lambda l,b:l*b
l = float(input("enter the length :"))
b = float(input("enter the breadth :"))
print("area of rectangle is :",rect(l,b))
print("")
print("area of square")
square = lambda a:a*a
a = float(input("enter the area :"))
print("area of the square with side",a,"is",square(a))
print("")
print("are of triangle")
triangle = lambda b,h:0.5*b*h
b = float(input("enter the base :"))
h = float(input("enter the height:"))
print("area of the triangle is :",triangle(b,h))
