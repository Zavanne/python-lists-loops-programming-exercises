my_list = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]

# Your code here

new_list = []

for item in my_list:
    if type(item) == list or type(item) == dict:
        new_list.append(item)

print(new_list)