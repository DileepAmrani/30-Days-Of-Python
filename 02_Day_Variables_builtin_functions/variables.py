# Day 2 - 30 days of python challenge
first_name="Dileep"
last_name="Kumar"
full_name="Dileep Kumar"
country="Pakistan"
city="Karachi"
age=25
year=2025
is_married=False
is_true=True
is_light_on=True
a,b,c=1,2,3

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))

print(len(first_name))

print(len(first_name) == len(last_name))

num_one=5
num_two=4

total= num_one + num_two
diff=num_one - num_two
product=num_one * num_two
division=num_one / num_two
remainder=num_one % num_two
exp=num_one ** num_two
floor_division=num_one // num_two

radius=30
area_of_circle=3.14 * radius ** 2
circum_of_circle=2 * 3.14 * radius
radius=int(input("Enter the radius: "))
area_of_circle=3.14 * radius ** 2
print("Area of circle:", area_of_circle)

first_name=str(input("Enter your first name: "))
last_name=str(input("Enter your last name: "))
age=int(input("Enter your age: "))

help('keywords')