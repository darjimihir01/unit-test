import array

# Create integer array with 8 elements
arr = array.array('i', [10, 20, 30, 40, 50, 60, 70, 80])
print("Array:", arr)

# a) Indexing and slicing
print("\na) Indexing and Slicing")
print("arr[0]:", arr[0])
print("arr[-1]:", arr[-1])
print("arr[2:5]:", arr[2:5])

# b) Insert element
print("\nb) Insert")
arr.insert(2, 25)
print("After insert:", arr)

# c) Remove and pop
print("\nc) Remove and Pop")
arr.remove(40)
print("After remove(40):", arr)
arr.pop()
print("After pop():", arr)

# d) Search element
print("\nd) Search")
num = int(input("Enter number to search: "))
if num in arr:
    print("Found at index:", arr.index(num))
else:
    print("Not found")

# e) Check membership
print("\ne) Membership")
print("10 in arr:", 10 in arr)
print("100 not in arr:", 100 not in arr)

# f) Max, min, length
print("\nf) Max, Min, Length")
print("Max:", max(arr))
print("Min:", min(arr))
print("Length:", len(arr))

# g) Reverse
print("\ng) Reverse")
arr.reverse()
print("Reversed:", arr)