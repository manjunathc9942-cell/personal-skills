# Defining the missing dictionary and list variables
dic = {1: "Test", 2: "Mark", 3: "Rank"}
li = ["Apple", "Banana", "Cherry",5,6,86,86]

# 1. Iterate over the list
for val in li:
    print(val)

# 2. Iterate using an index range
for i in range(10):
    print(i)

# 3. Iterate over the dictionary using key and value unpacking
for key, value in dic.items():
    print(f"Key: {key}, Value: {value}")




# question:
# ===============

# Input the range
start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

count = 0

for num in range(start, end + 1):
    if num % 2 != 0:  # Check if the number is odd
        if count % 2 == 0:  # Print alternate odd numbers
            print(num)
        count += 1




paragraph = input("Enter a paragraph: ")

repeated = []

for char in paragraph:
    if char != " " and paragraph.count(char) > 1 and char not in repeated:
        repeated.append(char)

print("Repeated characters:")
for char in repeated:
    print(char)






n = int(input("Enter the number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c