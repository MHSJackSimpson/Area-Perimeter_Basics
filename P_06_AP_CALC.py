# ask user for widith and height
# (assume they put in valid data)
widith = float(input("widith: "))
height = float(input("height: "))

# calculate the area / perimeter
area = widith * height
perimeter = 2 * (widith + height)

# output the area and perimeter
print()
print(f"Perimeter: {perimeter} units")
print(f"Area: {area} units")