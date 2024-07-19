my_list = [4,5,734,43,45,100,4,56,23,67,23,58,45]

# Your code here
def sum_odds (arr):
    odd_total = 0
    for item in arr:
        if item % 2 is not 0:
            odd_total += item
    return odd_total

print(sum_odds(my_list))
