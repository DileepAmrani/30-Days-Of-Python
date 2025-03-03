# Day 3 - 30 days of python challenge

age=25
heigt=5.6
comp=1j

print(type(age))
print(type(heigt))
print(type(comp))

base = int(input("Enter base: "))
height = int(input("Enter height: "))
area=0.5 * base * height
print(area)

sideA=int(input("Enter side A: "))
sideB=int(input("Enter side B: "))
sideC=int(input("Enter side C: "))
perimeter=sideA+sideB+sideC
print(perimeter)


length=int(input("Enter length: "))
width=int(input("Enter width: "))
area=length * width
print(area)

radius=int(input("Enter radius: "))
area=3.14 * radius * radius
print(area)


slope = 2

y_intercept = 2 * 0 - 2

x_intercept = (0 + 2) / 2

print(f"Slope: {slope}")
print(f"X-Intercept: {x_intercept}")
print(f"Y-Intercept: {y_intercept}")

x_value=5
y= x_value**2 + 6*x_value + 9
print("Y-value at x={x_value}: {y}")

text_one="python"
text_two="dragon"

print(len(text_one) == len(text_two))

# Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in text_one and 'on' in text_two)