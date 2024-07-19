# Your code here
def matrix_builder(matrix_integer):

    new_matrix =[]
    x = 0
    while x < matrix_integer:
        new_matrix.append([])
        y = 0
        while y < matrix_integer:
            new_matrix[x].append(1)
            y += 1
        x += 1
    return new_matrix

print(matrix_builder(5))

def matrix_builder_two(matrix_integer):
    return [[1] * matrix_integer for _ in range(matrix_integer)]

print(matrix_builder_two(5))

# List Comprehension:
# The outer list comprehension for _ in range(matrix_integer) creates each row.
# Inside, [1] * matrix_integer creates a row with matrix_integer ones.
# This approach eliminates the need for explicit while loops and manual index management.