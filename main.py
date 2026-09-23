"""
IT 401W - Targeted Practice (Weak Spots Review)
Focus areas based on your last activity:
  1. Boundary conditions in conditionals (off-by-one logic)
  2. List methods: remove() by value vs pop() by index
  3. Mutable default arguments (Python-specific gotcha)
  4. Lambda syntax (vs JS ternary / arrow functions)
  5. String methods: upper/lower/capitalize/title differences
  6. Built-in name shadowing (sum, list, str, etc.)

5 problems. No point values this time - the goal is understanding,
not scoring. Take your time on each one.
"""

# ---------------------------------------------------------
# Problem 1 - Boundary Conditions
# Write a function classify_temp(temp) that takes a temperature
# (Celsius) and returns:
#   "Freezing"   if temp <= 0
#   "Cold"       if temp is between 1 and 15 (inclusive)
#   "Mild"       if temp is between 16 and 25 (inclusive)
#   "Hot"        if temp >= 26
#
# Test it with EXACTLY these 5 values and print each result:
# 0, 15, 16, 25, 26
# Before running: predict on paper which category each boundary
# value falls into. Then check if your code agrees.
# ---------------------------------------------------------

def classify_temp(temp):
    if temp<=0:
        return 'Freezing'
    elif 1<=temp<=15:
        return 'Cold'
    elif 16<=temp<=25:
        return 'Mild'
    else:
        return 'Hot'
nums = [0,15,16,25,26]
for i in nums:
    result = classify_temp(i)
    print(f'Temp {i} is {result}')

# ---------------------------------------------------------
# Problem 2 - List Methods (remove vs pop)
# Start with this list:
groceries = ["milk", "eggs", "breAD", "milk", "butter"]
#
# Do the following, in order, printing the list after EACH step:
#   1. Remove the item "bread" using .remove() (by value)
#   2. Remove the item at index 0 using .pop() (by index)
#   3. Try to .remove("milk") - notice it only removes the FIRST
#      occurrence, not all of them. Print the list to confirm.
#   4. Explain in a comment: what's the difference between
#      .remove() and .pop()? What happens if you .remove() a
#      value that doesn't exist in the list? (you can test this
#      in a separate line to see the actual error)
# ---------------------------------------------------------

groceries.remove('breAD')
print(groceries)
#groceries.remove('breading')#value error not on the list also case sensitive
groceries.pop(0)
print(groceries)
#remove() removes it by value and pop() removes it by index and if doesnt exist throws value error


# ---------------------------------------------------------
# Problem 3 - Mutable Default Arguments (Python gotcha)
# Below is a BROKEN function using a mutable default argument.
# Run it as-is first and observe the output - it will look wrong.

def add_item(item, cart=[]):
    cart.append(item)
    return cart

print(add_item("apple"))
print(add_item("banana"))
print(add_item("cherry"))


# You'll notice the list keeps growing across calls, even though
# no list was passed in each time - this is because default
# arguments are created ONCE, not fresh per call.
#
# Now write a CORRECTED version below called add_item_fixed()
# that gives a fresh empty list every time it's called with no
# cart argument. (Hint: use None as the default instead of [])
# ---------------------------------------------------------

def add_item_fixed(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart
print(add_item("apple"))
print(add_item("banana"))
print(add_item("cherry"))


# ---------------------------------------------------------
# Problem 4 - Lambda Syntax Practice
# Python lambdas are NOT the same syntax as JS arrow functions
# or ternaries. Write the following as lambdas (one line each):
#
#   a) square       -> takes n, returns n * n
#   b) is_positive   -> takes n, returns True if n > 0 else False
#   c) full_name     -> takes first and last, returns "first last"
#
# Test each lambda with at least one sample input and print
# the result.
# ---------------------------------------------------------

square = lambda n : n * n
is_positive = lambda n : True if n > 0 else False
full_name = lambda first,last : first+' '+last

#test
print(square(2))
print(is_positive(-4))
print(full_name('juan','cruz'))

# ---------------------------------------------------------
# Problem 5 - String Methods + Avoiding Built-in Shadowing
# Ask the user to input their full name (e.g. "ralf gatmaitan").
# Then print:
#   - The name in Title Case using .title() (NOT .capitalize() -
#     look up the difference between these two before using one)
#   - The name in all uppercase
#   - The number of characters in the name EXCLUDING spaces
#     (hint: you'll need .replace() or a loop)
#
# IMPORTANT: name your variables carefully. Do NOT use "str",
# "list", "len", "input", or "type" as variable names - these
# are built-in Python names and reassigning them can break your
# code in ways that are hard to debug later.
# ---------------------------------------------------------

fname = input("Enter full name")
print(fname.title())
print(fname.upper())
no_spaces = fname.replace(' ', '')
print(len(no_spaces))