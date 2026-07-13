
# String:
# ===============

# len, lower, upper, concat, find, replace, strip, split, join, startswith, endswith, isalpha, isdigit, isspace
# Single and Double quotes work identically
single_quoted = 'Chromium'
double_quoted = "Firefox"

# Triple quotes allow for MULTI-LINE strings (Perfect for raw SQL queries or HTML chunks in tests)
html_payload = """
<div data-test-id="success-banner">
    <p>Transaction Approved</p>
</div>
"""


print(single_quoted)



# The raw, messy string scraped from a webpage (common in UI testing)
raw_text = "   Yubi_Platform_2026   "

# 1. len() -> Gets the total count of characters (including spaces)
print(f"1. len: {len(raw_text)}")  # Output: 24

# 2. strip() -> Removes leading and trailing whitespaces/newlines
clean_text = raw_text.strip()
print(f"2. strip: '{clean_text}'")  # Output: 'Yubi_Platform_2026'

# 3. lower() -> Converts all characters to lowercase
print(f"3. lowercase: '{clean_text.lower()}'")  # Output: 'yubi_platform_2026'

# 4. upper() -> Converts all characters to uppercase
print(f"4. uppercase: '{clean_text.upper()}'")  # Output: 'YUBI_PLATFORM_2026'

# 5. Concatenation (+) -> Glues two or more strings together
base_url = "https://api.yubi.com"
endpoint = "/v1/auth"
print(f"5. concat: {base_url + endpoint}")  # Output: https://api.yubi.com/v1/auth

# 6. find() -> Returns the lowest index position of a substring (returns -1 if not found)
print(f"6. find ('Platform'): {clean_text.find('Platform')}")  # Output: 5

# 7. replace() -> Swaps an old substring with a new one
print(f"7. replace: {clean_text.replace('2026', 'Production')}")  # Output: Yubi_Platform_Production

# 8. split() -> Breaks a string into a List based on a delimiter
log_elements = clean_text.split("_")
print(f"8. split: {log_elements}")  # Output: ['Yubi', 'Platform', '2026']

# 9. join() -> Glues a List of strings together using a separator
print(f"9. join: {'/'.join(log_elements)}")  # Output: Yubi/Platform/2026

# 10. startswith() -> Returns True if the string begins with a specific prefix
print(f"10. startswith ('Yubi'): {clean_text.startswith('Yubi')}")  # Output: True

# 11. endswith() -> Returns True if the string ends with a specific suffix
print(f"11. endswith ('2026'): {clean_text.endswith('2026')}")  # Output: True

# 12. isalpha() -> Returns True if the string contains ONLY alphabet letters (No numbers/spaces/underscores)
print(f"12. isalpha: {'Yubi'.isalpha()}")  # Output: True (clean_text would be False due to digits/underscores)

# 13. isdigit() -> Returns True if the string contains ONLY numerical digits
print(f"13. isdigit: {'2026'.isdigit()}")  # Output: True

# 14. isspace() -> Returns True if the string contains ONLY whitespace characters
print(f"14. isspace: {'   '.isspace()}")  # Output: True





# List:
# ===============

append, extend, insert, remove, pop, index, count, sort, reverse, copy, slice, membership, iteration

# List (Ordered, mutable sequences)
# Items can be modified, appended, or reordered dynamically
browser_types = ["chromium", "firefox", "webkit"]  
print(f"List: {browser_types}, Type: {type(browser_types)}")



# -------------------------------------------------------------------------
# INITIAL DATA: A list of active test browsers
# -------------------------------------------------------------------------
browsers = ["chromium", "firefox", "webkit"]

# 1. append() -> Adds a SINGLE element to the absolute end of the list
browsers.append("edge")
print(f"1. append: {browsers}")  
# Output: ['chromium', 'firefox', 'webkit', 'edge']


# 2. extend() -> Appends MULTIPLE elements (another iterable) to the end
mobile_browsers = ["android-chrome", "ios-safari"]
browsers.extend(mobile_browsers)
print(f"2. extend: {browsers}")  
# Output: ['chromium', 'firefox', 'webkit', 'edge', 'android-chrome', 'ios-safari']


# 3. insert() -> Adds an element at a SPECIFIC index position: insert(index, object)
browsers.insert(1, "opera")
print(f"3. insert: {browsers}")  
# Output: ['chromium', 'opera', 'firefox', 'webkit', 'edge', 'android-chrome', 'ios-safari']


# 4. remove() -> Removes the FIRST matching item by its value. Throws ValueError if not found.
browsers.remove("opera")
print(f"4. remove: {browsers}")  
# Output: ['chromium', 'firefox', 'webkit', 'edge', 'android-chrome', 'ios-safari']


# 5. pop() -> Removes and RETURNS an element at a given index (defaults to the last item if left empty)
last_browser = browsers.pop()
print(f"5. pop (removed item: '{last_browser}'): {browsers}")  
# Output: ['chromium', 'firefox', 'webkit', 'edge', 'android-chrome']


# 6. index() -> Returns the position (index number) of the first matching value
webkit_position = browsers.index("webkit")
print(f"6. index of 'webkit': {webkit_position}")  
# Output: 2


# 7. count() -> Counts how many times a specific value appears in the list
print(f"7. count of 'chromium': {browsers.count('chromium')}")  
# Output: 1


# 8. sort() -> Sorts the actual list in place (Alphanumeric by default)
browsers.sort()
print(f"8. sort (In-place): {browsers}")  
# Output: ['chromium', 'edge', 'firefox', 'webkit']


# 9. reverse() -> Reverses the order of the list in place
browsers.reverse()
print(f"9. reverse (In-place): {browsers}")  
# Output: ['webkit', 'firefox', 'edge', 'chromium']


# # 10. copy() -> Creates a shallow copy (a brand new list object in memory)
# # Crucial because setting 'new_list = old_list' just copies the reference, meaning changing one changes both!
# cloned_browsers = browsers.copy()
# print(f"10. copy: {cloned_browsers is browsers}")  
# # Output: False (They are identical in content, but separate objects in memory)


# 11. Slicing ([start:stop:step]) -> Extracts a specific sub-section of the list
# Let's pull the first two elements
top_two = browsers[0:2]
print(f"11. slice [0:2]: {top_two}")  
# Output: ['webkit', 'firefox']


# # 12. Membership Operators (in / not in) -> Checks if an item exists inside the list (Returns Boolean)
# has_safari = "safari" in browsers
# print(f"12. membership ('safari' in list?): {has_safari}")  
# Output: False


# 13. Iteration (Looping) -> Stepping through each item sequentially
print("13. iteration:")
for browser in browsers:
    print(f"   -> Testing compatibility on: {browser}")