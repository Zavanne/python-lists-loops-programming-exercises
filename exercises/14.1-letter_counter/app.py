par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"

counts = {}

# Your code here
for letter in par:
    letter = letter.lower()
    if letter in counts:
        counts[letter] += 1
    elif letter == " ":
        continue
    else:
        counts[letter] = 1

print(counts)

# from collections import defaultdict

# par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"

# counts = defaultdict(int)

# print("using default dict " + counts)

# # Your code here
# for letter in par:
#     letter = letter.lower()
#     if letter != " ":
#         counts[letter] += 1

# print(dict(counts))

