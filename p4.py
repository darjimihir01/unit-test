# Accept two strings from the user
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

print("\n--- Starting Program ---\n")


# ==========================================================
# a) Display strings and their lengths
# ==========================================================
print("Part A: Display strings and their lengths")

print("First string:", str1)
print("Second string:", str2)
print("Length of first string:", len(str1))
print("Length of second string:", len(str2))
print("\n")


# ==========================================================
# b) Access characters using positive and negative indexing
# ==========================================================
print("Part B: Access characters using indexing")

print("Using first string:", str1)

# Positive indexing (starts from 0)
print("First character (index 0):", str1[0])
print("Second character (index 1):", str1[1])

# Negative indexing (starts from -1 at the end)
print("Last character (index -1):", str1[-1])
print("Second to last character (index -2):", str1[-2])
print("\n")


# ==========================================================
# c) Extract substrings using slicing
# ==========================================================
print("Part C: Extract substrings using slicing")

print("Using first string:", str1)

# Slicing [start:end]
print("Characters from index 0 to 3:", str1[0:4])
print("Characters from index 2 to end:", str1[2:])
print("Characters from start to index 3:", str1[:4])
print("Every second character:", str1[::2])
print("Reverse the string:", str1[::-1])
print("\n")


# ==========================================================
# d) Repeat a string using * and concatenate using +
# ==========================================================
print("Part D: Repetition and Concatenation")

# Repetition using *
repeated = str1 * 3
print("First string repeated 3 times:", repeated)

# Concatenation using +
combined = str1 + str2
print("First string + Second string:", combined)

# Concatenation with a space in between
combined_space = str1 + " " + str2
print("First string + space + Second string:", combined_space)
print("\n")


# ==========================================================
# e) Check whether a character or substring exists
# ==========================================================
print("Part E: Check membership using in and not in")

check_char = input("Enter a character or substring to check: ")

# Using 'in'
if check_char in str1:
    print("'", check_char, "' is found in the first string")
else:
    print("'", check_char, "' is NOT found in the first string")

# Using 'not in'
if check_char not in str2:
    print("'", check_char, "' is NOT found in the second string")
else:
    print("'", check_char, "' is found in the second string")
print("\n")


# ==========================================================
# f) Compare two strings
# ==========================================================
print("Part F: Compare two strings")

print("First string:", str1)
print("Second string:", str2)

if str1 == str2:
    print("Both strings are EQUAL (==)")
else:
    print("Both strings are NOT EQUAL (!=)")

if str1 != str2:
    print("Strings are different (!=)")

if str1 < str2:
    print("First string comes BEFORE second string (<)")
else:
    print("First string does NOT come before second string")

if str1 > str2:
    print("First string comes AFTER second string (>)")
else:
    print("First string does NOT come after second string")
print("\n")


# ==========================================================
# g) Convert strings to uppercase and lowercase
# ==========================================================
print("Part G: Convert to uppercase and lowercase")

print("First string in UPPERCASE:", str1.upper())
print("First string in lowercase:", str1.lower())
print("Second string in UPPERCASE:", str2.upper())
print("Second string in lowercase:", str2.lower())
print("\n")

print("--- Program Complete ---")