# -------------------------------------------------------------------------
# 1. ARITHMETIC OPERATORS (Math Computations)
# -------------------------------------------------------------------------
# Used for mathematical calculations (e.g., calculating cart totals or pagination offsets)
item_price = 500
tax_rate = 0.18

total = item_price + 100    # Addition
discounted = item_price - 50 # Subtraction
tax_amount = item_price * tax_rate # Multiplication
divided_pages = 25 / 5      # Division (Always returns a float: 5.0)
integer_division = 25 // 4  # Floor Division (Drops decimals: 6)
remainder = 25 % 4          # Modulo (Returns remainder: 1)
squared_value = 5 ** 2      # Exponentiation (5 to the power of 2: 25)


# -------------------------------------------------------------------------
# 2. COMPARISON OPERATORS (Value Assertions)
# -------------------------------------------------------------------------
# Crucial for test assertions. They compare values and always return a Boolean (True/False)
expected_count = 5
actual_count = 5

print(f"Equal to: {actual_count == expected_count}")       # True
print(f"Not equal to: {actual_count != 10}")              # True
print(f"Greater than: {actual_count > 3}")                 # True
print(f"Less than: {actual_count < 10}")                   # True
print(f"Greater than or equal: {actual_count >= 5}")       # True


# -------------------------------------------------------------------------
# 3. LOGICAL OPERATORS (Combining Conditions)
# -------------------------------------------------------------------------
# Used to build complex execution gates (e.g., checking if a user is logged in AND has premium status)
is_logged_in = True
has_valid_token = False

# 'and' -> Returns True ONLY if both sides are True
print(f"Logical AND: {is_logged_in and has_valid_token}")  # False

# 'or' -> Returns True if AT LEAST one side is True
print(f"Logical OR: {is_logged_in or has_valid_token}")    # True

# 'not' -> Reverses the boolean state
print(f"Logical NOT: {not is_logged_in}")                  # False

# -------------------------------------------------------------------------
# 4. Assignmet OPERATORS (Shorthand for Updating Values)
# -------------------------------------------------------------------------

# -------------------------------------------------------------------------
# 1. BASIC ASSIGNMENT (=)
# -------------------------------------------------------------------------
# Assigns the value on the right to the variable on the left
current_page = 1
max_retries = 3
test_failures = 0


# -------------------------------------------------------------------------
# 2. COMPOUND ASSIGNMENT OPERATORS (The Shortcuts)
# -------------------------------------------------------------------------

# Add and Assign (+=) -> Useful for incrementing page numbers or retry attempts
# Equivalent to: current_page = current_page + 1
current_page += 1  
print(f"Add and Assign (New Page): {current_page}")  # Output: 2

# Subtract and Assign (-=) -> Useful for decremental countdown loops
# Equivalent to: max_retries = max_retries - 1
max_retries -= 1  
print(f"Subtract and Assign (Retries Left): {max_retries}")  # Output: 2

# Multiply and Assign (*=) -> Useful for exponential wait times (Backoff strategies)
backoff_delay = 2
backoff_delay *= 2  
print(f"Multiply and Assign (New Delay): {backoff_delay}s")  # Output: 4s

# Divide and Assign (/=) -> Divides and assigns as a Float
total_execution_time = 120.0
total_execution_time /= 2  
print(f"Divide and Assign: {total_execution_time}")  # Output: 60.0

# Modulo and Assign (%=) -> Divides and assigns the remainder
batch_pool = 15
batch_pool %= 4  
print(f"Modulo and Assign (Remainder): {batch_pool}")  # Output: 3



# -------------------------------------------------------------------------
# 5. MEMBERSHIP OPERATORS (Collection Validation)
# -------------------------------------------------------------------------
# Evaluates whether a target sequence exists within a collection (Strings, Lists, Sets, Dicts)
error_logs = ["ERR_TIMEOUT", "ERR_401_UNAUTHORIZED", "ERR_500_INTERNAL"]

print(f"Is present: {'ERR_TIMEOUT' in error_logs}")         # True
print(f"Is not present: {'SUCCESS' not in error_logs}")     # True


# -------------------------------------------------------------------------
# 6. IDENTITY OPERATORS (Memory Verification)
# -------------------------------------------------------------------------
# Checks if two variables point to the exact same object in computer memory
list_x = [1, 2, 3]
list_y = [1, 2, 3]
list_z = list_x

print(f"Identity 'is': {list_x is list_z}")   # True (They point to the exact same memory address)
print(f"Identity 'is': {list_x is list_y}")   # False (Identical content, but separate objects in memory!)
print(f"Value Equality: {list_x == list_y}")   # True (Their values are identical)