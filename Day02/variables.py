import math # used for solving area of circle problem
'''
Q:Write a python comment saying 'Day 2: 30 Days of python programmin'''
# Day 2: 30 Days of python programming

'''
Q:Declare a first name variable and assign a value to it
'''

var = 7

'''
Q:Declare a last name variable and assign a value to it'''

last_name = "PRABHAKAR"

'''
Q:Declare a full name variable and assign a value to it'''

full_name = 'VISHWA KIRTI PRABHAKAR'

'''
Q:Declare a country variable and assign a value to it
'''
country = 'INDIA'

'''
Q:Declare a city variable and assign a value to it
'''

City = 'PATNA'

'''
Q:Declare an age variable and assign a value to it
'''

age = 24

'''
Q:Declare a year variable and assign a value to it
'''
year = 2023

'''
Q:Declare a variable is_married and assign a value to it
'''

is_married = False


'''
Q:Declare a variable is_true and assign a value to it
'''
is_true = False

'''
Q:Declare a variable is_light_on and assign a value to it
'''
is_light_on = True

'''
Q:Declare multiple variable on one line
'''
name,age,country = 'Vishwa',24,'India'


'''
Q:Check the data type of all your variables using type() built-in function
'''

print(type(name),type(age),type(country),type(is_light_on),type(is_married),type(is_true),type(full_name),type(var))


''''
Q:Using the len() built-in function, find the length of your first namesing the len() built-in function, find the length of your first name
'''

print(len(name))

'''
Q:Compare the length of your first name and your last name
'''
if len(name) > len(last_name):
    print(name,len(name))
else:
    print(last_name,len(last_name))


'''
Q:Declare 5 as num_one and 4 as num_two
- Add num_one and num_two and assign the value to a variable total
- Subtract num_two from num_one and assign the value to a variable diff
- Multiply num_two and num_one and assign the value to a variable product
- Divide num_one by num_two and assign the value to a variable division
- Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
- Calculate num_one to the power of num_two and assign the value to a variable exp
- Find floor division of num_one by num_two and assign the value to a variable floor_division

'''

num1  = 5
num2 = 10
add_total = num1 + num2
sub_total = num2 - num1
mul_total = num1 * num2
divide_total = num2 / num1
mod_total = num2%num1
power_total = num1**num2
floor_division = num2//num1
print('Addition:',add_total)
print('subtraction:',sub_total)
print('multilication:',mul_total)
print('division:',divide_total)
print('mod_total',mod_total)
print('power_total:',power_total)
print('floor_division:',floor_division)


'''
Q:The radius of a circle is 30 meters.
- Calculate the area of a circle and assign the value to a variable name of area_of_circle
- Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
- Take radius as user input and calculate the area.
'''
radius_user_in = int(input("Enter the radius:"))
ar_of_circle = math.pi * radius_user_in * radius_user_in
circ_of_circle = 2 * math.pi * radius_user_in
print('Area of circle:',ar_of_circle)
print('Circumference of circle:',circ_of_circle)


'''
Q:Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
'''
first_name_user_in = input('Enter the name:')
last_name_user_in = input('Enter the last name:')
country_user_in = input('Enter the country:')
age_user_in = input('Enter the age:')

print('Name:',first_name_user_in+"\n"+"last Name:",last_name_user_in
+"\n"+'country:',country_user_in+"\n"+'Age:',age_user_in)