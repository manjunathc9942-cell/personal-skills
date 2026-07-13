
# -------------------------------------------------------------------------
# 1. IF..ELSE STATEMENT
# -------------------------------------------------------------------------
# if..else statement

a = int(input("Enter a number: "))
b = int(input("Enter b number: "))

if a < b:
    print('a is smallest')
else:
    print('b is smallest')


# -------------------------------------------------------------------------
# 2. NESTED IF STATEMENT
# -------------------------------------------------------------------------
# nested if statement

age = int(input("Enter your age: "))

if age > 18:
    print("he is eligible")
    if age > 45:
        print("senior citizen")
else:
    print('not eligible for voting')


# -------------------------------------------------------------------------
# 3. ELSE IF STATEMENT
# -------------------------------------------------------------------------
# else if statement

Number = int(input("Enter a number: "))

if num > 0:
    print('number is positive')
elif num == 0:
    print("zero")
else:
    print('negative number')