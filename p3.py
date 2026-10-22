# Create a tuple with at least 10 values including repeated numbers
my_tuple = (5, 10, 15, 10, 20, 25, 10, 30, 35, 40)

print("Original tuple:", my_tuple)
print("\n")


# a) Display tuple and access elements

# Positive indexing (starts from 0)
print("First element (index 0):", my_tuple[0])
print("Third element (index 2):", my_tuple[2])
print("Last element (index 9):", my_tuple[9])

# Negative indexing (starts from -1 at the end)
print("Last element (index -1):", my_tuple[-1])
print("Second to last (index -2):", my_tuple[-2])
print("Fifth from last (index -5):", my_tuple[-5])

# Slicing
print("Elements from index 2 to 5:", my_tuple[2:6])
print("First 4 elements:", my_tuple[:4])
print("Last 3 elements:", my_tuple[-3:])
print("Every second element:", my_tuple[::2])
print("\n")


# b) Tuple concatenation and repetition


tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Concatenation using +
combined = tuple1 + tuple2
print("tuple1 + tuple2 =", combined)

# Repetition using *
repeated = tuple1 * 3
print("tuple1 * 3 =", repeated)
print("\n")


# c) Check if element exists using in and not in


check_value = 10

if check_value in my_tuple:
    print(check_value, "is in the tuple")
else:
    print(check_value, "is NOT in the tuple")

check_value2 = 100

if check_value2 not in my_tuple:
    print(check_value2, "is NOT in the tuple")
else:
    print(check_value2, "is in the tuple")
print("\n")


# d) Find maximum, minimum, and length

maximum = max(my_tuple)
minimum = min(my_tuple)
length = len(my_tuple)

print("Maximum value:", maximum)
print("Minimum value:", minimum)
print("Length of tuple:", length)
print("\n")


# e) Count occurrences of a value

search_value = int(input("Enter a value to count: "))
occurrences = my_tuple.count(search_value)
print("The value", search_value, "appears", occurrences, "time(s) in the tuple")
print("\n")


# f) Search for element using index()

search_element = int(input("Enter a value to find its index: "))

if search_element in my_tuple:
    position = my_tuple.index(search_element)
    print("The value", search_element, "is found at index:", position)
else:
    print("Sorry,", search_element, "is not found in the tuple")
print("\n")

print("--- Program Complete ---")



