# Create a program that takes two numbers as input and 
# prints whether the first number is greater than, 
# less than, or equal to the second number.


# first = int(input("enter the first number="))
# second = int(input("enter the second number="))
# if first > second:
#     print("The first number is greater than the second number.")
# elif first < second:
#     print("The first number is less than the second number.")
# elif first ==second:
#     print("The first number is equal to the second number.")
# else:
#     print("Invalid input.")


    # Use the ternary operator to find the maximum of three numbers entered by the user.

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number: "))
# max_num = num1 if (num1 >= num2 and num1 >= num3) else (num2 if num2 >= num3 else num3)
# print("The maximum number is:", max_num)


# Develop a Python script that calculates the square and cube of a given number.
# number = int(input("Enter a number: "))
# square = number ** 2
# cube = number ** 3
# print("The square of", number, "is", square)
# print("The cube of", number, "is", cube)


# Problem to find the MAX three

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number: "))
# if num1 >= num2 and num1 >= num3:
#     max_num = num1
# elif num2 >= num1 and num2 >= num3:
#     max_num = num2
# else:    max_num = num3
# print("The maximum number is:", max_num)    



# Create a program that determines whether a given year is a leap year.

# A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
# Use an if-else statement to make this determination.

# Input = 2024
# Output = Leap year


# year = int(input("Enter a year: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("Leap year")
# else:
#     print("Not a leap year")



# Write a program that classifies a triangle based on its side lengths.

# Given three input values representing the lengths of the sides, determine if the triangle is equilateral (all sides are equal), isosceles (exactly two sides are equal), or scalene (no sides are equal).

# Use an if-else statement to classify the triangle.
# 3 Input
# side 1, side 2 and side 3
# output - Eq, Iso, Scalene -
# Eq. = side 1 == side 2 = side 3


# side1 = float(input("Enter the length of the first side: "))
# side2 = float(input("Enter the length of the second side: "))
# side3 = float(input("Enter the length of the third side: "))    

# if side1 == side2 == side3:
#     print("The triangle is equilateral.")
# elif side1 == side2 or side2 == side3 or side1 == side3:
#     print("The triangle is isosceles.")
# else:
#     print("The triangle is scalene.")



# for num in range(2, 10):
#    if num % 2 == 0:
#         print("Found an even number", num)
#         continue
# print("Found an odd number", num)


# from re import match


# user_input = input("Enter the name of a web browser: ")
# browser = user_input.lower()  # Convert input to lowercase for case-insensitive matching
# match browser:
#     case "chrome":
#         print("You have selected Google Chrome.")
#     case "firefox":
#         print("You have selected Mozilla Firefox.")
#     case "safari":
#         print("You have selected Apple Safari.")
#     case _:
#         print("Invalid browser selection.")


# def minimum(first, second):
#     if (first < second):
#         print(first)
#     else:
#         print(second)





# first = int(input("enter the first number="))
# second = int(input("enter the second number="))
# minimum(first, second)

# user_input1 = int(input("enter the first number="))
# user_input2 = int(input("enter the second number="))
# user_input3 = int(input("enter the third number="))
# user_input4 = int(input("enter the fourth number="))
# maximum = max(user_input1, user_input2, user_input3,user_input4)  # Example: comparing user input with a fixed number (10)
# print("The maximum number is:", maximum)



def my_functio(country="India"):
    print("I am from " + country)


my_functio("USA")
my_functio("UK")
my_functio()
my_functio("Australia")
