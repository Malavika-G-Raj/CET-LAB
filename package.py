from graphics import circle,rectangle
from graphics.graphics_3d import sphere,cuboid
a=float(input("\nEnter radius of circle:"))
print("\narea of circle=",circle.area(a))
print("\nperimeter of circle=",circle.perimeter(a))
 
b=int(input("\n Enter the length:"))
c=int(input("\n Enter the breadth:"))
print("\n Area of rectangle=",rectangle.area(b,c))
print("\nperimeter of rectangle=",rectangle.perimeter(b,c))

d=float(input("\n Enter the radius of sphere:"))
print("\n Area of sphere=",sphere.area(d))
print("\nperimeter of sphere=",sphere.perimeter(d))

e=int(input("\n Enter the length:"))
f=int(input("\n Enter the width:"))
g=int(input("\n Enter the height:"))
print("\n Area of cuboid=",cuboid.area(e,f,g))
print("\nperimeter of cuboid=",cuboid.perimeter(e,f,g))




