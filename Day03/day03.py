import math # for using math.pi
'''
Q:Declare your age as integer variable
'''



age_user_in = int(input("Enter the age:"))
print(age_user_in)

'''
Q:Declare your height as a float variable
'''
height_user_in = float(input("Enter your height"))
print(height_user_in)

'''
Q:Declare a variable that store a complex number
'''
store_complex = complex(input("Enter the complex number:"))
print(store_complex)
print(type(store_complex))


'''
Q:Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
'''
height_of_tr = float(input('Enter the height of triangle:'))
base_of_tr = float(input('Enter the base:'))
ar_of_tr = 0.5 * height_of_tr * base_of_tr
print('Area of Triangle:',ar_of_tr)



'''
Q:Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
'''
side_a = float(input('Enter the side a:'))
side_b = float(input('Enter the side b:'))
side_c = float(input('Enter the side c:'))
perimeter_of_tr = side_a + side_b +side_c
print('Perimeter of triangle:',perimeter_of_tr)


'''
Q:Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
'''
length = float(input('Enter the length:'))
width = float(input('Enter the width:'))
area = length * width
perimeter = 2 * length * width
print('Area:',area)
print('Perimter:',perimeter)


'''
Q:Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
'''
radius = float(input('Enter the radius:'))
area = math.pi * radius * radius
perimter_ar = 2 * math.pi * radius
print('Area:',area)
print('Perimerter:',perimter_ar)

'''
Q:Calculate the slope, x-intercept and y-intercept of y = 2x -2
'''
slope = 2 #coeff of x
x_intercept = 2 / 2    #taking y=0
y_intercept = (2 * 0) - 2   #taking x=0
print('slope:',slope)
print('x_intercept:',x_intercept)
print('Y_intercept:',y_intercept)


'''
Q:Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
'''
slope_0 = (6-2)/(10-2)
eculidean_dist_x = 6-2
eculidean_dist_y = 10-2
print('slope',slope_0)
print('eculidean dist:',eculidean_dist_x,eculidean_dist_y)

'''
Q:Compare the slopes in tasks 8 and 9.
'''
if slope > slope_0:
     print(f'Slope:{slope} is bigger')
elif slope_0 > slope:
    print(f'slope:{slope_0} is bigger')
else:
    print('both are equal')


'''
Q:Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
'''
x = int(input('Enter the value of x in the equation y= x^2 + 6x + 9:'))
y = x**2 + 6*x + 9
if y==0:
    print(f'{x} is the value it became 0')
else:
    print(y)


'''
Q:Find the length of 'python' and 'dragon' and make a falsy comparison statement.
'''
x = len('python')
y = len('dragon')
if x > y:
    print(f'python is larger: {x}')
elif y >x:
    print(f'dragon is larger: {y}')
else:
    print('both are equal')


'''
Q:Use and operator to check if 'on' is found in both 'python' and 'dragon'
'''
word_1 = 'python'
word_2 = 'dragon'
if 'on' in word_1 and word_2:
    print('True')
else:
    print('False')


'''
Q:I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
'''

words_sen = 'I hope this course is not full of jargon'
if 'jargon' in words_sen:
    print('Present')
else:
    print('Not Present')


'''
Q:There is no 'on' in both dragon and python
'''
word_1 = 'python'
word_2 = 'dragon'
if 'on' in word_1 and word_2:
    print('True')
else:
    print('False')


'''
Q:Find the length of the text python and convert the value to float and convert it to string
'''
len_word = 'python'
print(str(float(len(len_word))))



'''
Q:Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
'''
num = int(input('Enter the number:'))
if num%2 == 0:
    print('Even')
else:
    print('Odd')


'''
Q:Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
'''
total = 7 //3
print(int(total))


'''
Q:Check if type of '10' is equal to type of 10
'''
print('10'==10)


'''
Q:Check if int('9.8') is equal to 10
'''

str_num = '9.8'
str_num = int(str_num)
# print(str_num == 10) # will raise the value error

'''
Q:Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
'''
user_in_hour = int(input('Enter the hours:'))
user_in_rate = int(input('Enter the hour rate:'))
total_pay = user_in_hour * user_in_rate
print(f'Total rate:{total_pay}')


'''
Q:Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
'''
user_in_year = int(input('Enter the year:'))
year_in_sec = 31536000
cal_no_of_second = user_in_year * year_in_sec
print(cal_no_of_second)


'''
Q:Write a Python script that displays the following table
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
'''
for i in range(1, 6):
    row = ""
    for j in range(1, 6):
        if j ==1:
            row += str(i**(j)) + " "
        row += str(i**(j-1)) + " "
    print(row)