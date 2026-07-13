# Defining the missing dictionary and list variables
dic = {1: "Test", 2: "Mark", 3: "Rank"}
li = ["Apple", "Banana", "Cherry"]

# 1. Iterate over the list
for val in li:
    print(val)

# 2. Iterate using an index range
for i in range(10):
    print(i)

# 3. Iterate over the dictionary using key and value unpacking
for key, value in dic.items():
    print(f"Key: {key}, Value: {value}")