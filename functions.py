# -------------------------------------------------------------------------
# 1. BASIC FUNCTION
# -------------------------------------------------------------------------
def add():
    a = 10
    b = 20
    c = a + b
    print(f"Basic Add Output: {c}")

add()

# -------------------------------------------------------------------------
# 2. FUNCTION WITH ARGUMENTS
# -------------------------------------------------------------------------
def add_arg(a, b):
    c = a + b
    print(f"Parameterized Add Output: {c}")

add_arg(2, 6)
add_arg(1000, 5000)

# -------------------------------------------------------------------------
# 3. FUNCTION WITH RETURN VALUE
# -------------------------------------------------------------------------
def add_arg_retu(a, b):
    c = a + b
    return c

result = add_arg_retu(2, 4)
print(f"Returned Result: {result}")

# -------------------------------------------------------------------------
# 4. FUNCTION WITH DEFAULT PARAMETERS
# -------------------------------------------------------------------------
def add_default(a=0, b=1):
    c = a + b
    return c

result1 = add_default()
print(f"Default Parameters Result: {result1}")