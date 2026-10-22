# Accept a sentence from the user
sentence = input("Enter a sentence: ")

# Remove spaces
print("\nRemoving spaces:")
print("lstrip():", sentence.lstrip())
print("rstrip():", sentence.rstrip())
print("strip():", sentence.strip())

sentence = sentence.strip()

# a) Search for substring

word = input("Enter word to search: ")
print("find():", sentence.find(word))
if word in sentence:
    print("index():", sentence.index(word))
else:
    print("index(): Word not found")

# b) Count occurrences
print("\nCounting words:")
count_word = input("Enter word to count: ")
print("count():", sentence.count(count_word))

# c) Replace word
print("\nReplacing word:")
old = input("Enter word to replace: ")
new = input("Enter new word: ")
print("replace():", sentence.replace(old, new))

# d) Split and join
print("\nSplit and join:")
words = sentence.split()
print("split():", words)
print("join():", " ".join(words))

# e) String immutability
print("\nString immutability:")
print("Trying to change sentence[0] = 'X'")
try:
    sentence[0] = 'X'
except:
    print("Error: Strings cannot be changed (immutable)")

# f) Sort words
print("\nSorting words:")
words = sentence.split()
words.sort()
print("Sorted:", " ".join(words))