# -------------------------------------------------------------------------
# 1. NUMERIC TYPES
# -------------------------------------------------------------------------

# Integer (Whole numbers, notice the typo 'Interger' in the chart graphic)
# type1:

a = 3
print(type(a))  # Output: <class 'int'>


user_id = 101  
print(f"Integer: {user_id}, Type: {type(user_id)}")

# Float (Decimal numbers)
interest_rate = 8.75  
print(f"Float: {interest_rate}, Type: {type(interest_rate)}")

# Complex Number (Numbers with a real and imaginary part, represented by 'j')
coordinate_vector = 3 + 4j  
print(f"Complex Number: {coordinate_vector}, Type: {type(coordinate_vector)}")


# -------------------------------------------------------------------------
# 2. DICTIONARY (Key-Value Pairs)
# -------------------------------------------------------------------------
# Unordered, mutable collections mapped via unique keys
test_payload = {
    "status": "PENDING",
    "retry_count": 3,
    "is_active": True
}
print(f"Dictionary: {test_payload}, Type: {type(test_payload)}")

print(test_payload["status"])


# -------------------------------------------------------------------------
# 3. BOOLEAN (Conditional Truth Values)
# -------------------------------------------------------------------------
# Represents evaluate-able states: True or False
is_test_passed = True  
print(f"Boolean: {is_test_passed}, Type: {type(is_test_passed)}")


# -------------------------------------------------------------------------
# 4. SET (Unique Collections)
# -------------------------------------------------------------------------
# Unordered collection of unique items; automatically drops duplicates
unique_status_codes = {200, 201, 400, 200, 404}  # The second 200 is automatically removed
print(f"Set: {unique_status_codes}, Type: {type(unique_status_codes)}")


# -------------------------------------------------------------------------
# 5. SEQUENCE TYPES (Ordered Collections)
# -------------------------------------------------------------------------

# Strings (Text characters wrapped in quotes)
locator_name = "Submit Button"  
print(f"String: '{locator_name}', Type: {type(locator_name)}")

# List (Ordered, mutable sequences)
# Items can be modified, appended, or reordered dynamically
browser_types = ["chromium", "firefox", "webkit"]  
print(f"List: {browser_types}, Type: {type(browser_types)}")

# Tuple (Ordered, immutable sequences)
# Once declared, the contents CANNOT be changed or modified (read-only)
environment_dimensions = (1280, 720)  
print(f"Tuple: {environment_dimensions}, Type: {type(environment_dimensions)}")




# NoneType (Absence of value)
applied_coupon = None
print(f"Missing Type: {applied_coupon}, Type: {type(applied_coupon)}")

# Example QA Assertion:
assert applied_coupon is None, "Error: Coupon should not be applied to this transaction!"