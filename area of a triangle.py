#Calculate the area of a triangle given its base and height using a function

def area_of_triangle(Base, Height):
    Area = 0.5 * Base * Height
    return Area

b = float(input("Enter the base of a triangle: "))
h = float(input("Enter the height of a triangle: "))

print(f"Area of a triangle is {area_of_triangle(b,h):.2f}")
