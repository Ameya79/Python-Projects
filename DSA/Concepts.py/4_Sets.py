# Create a set
s = set([1, 2, 3, 3])   # duplicate 3 is removed
print(s)                # Output: {1, 2, 3}

# Check membership
print(2 in s)           # True
print(5 in s)           # False

# Add to set
s.add(4)

# Intersection with another set
a = set([1, 2, 3])
b = set([2, 3, 4])
print(a & b)            # Output: {2, 3}

# Convert back to list
list(a & b)             # [2, 3]
