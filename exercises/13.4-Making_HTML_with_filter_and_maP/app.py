all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

# Your code here
def filter_colors(list_of_colors):
    return [color['label'] for color in list_of_colors if color['sexy'] == True]
    
def generate_li(sexy_colors):
    return list(map(lambda color: f"<li>{color}</li>", sexy_colors))
    

# print(filter_colors(all_colors))

print(generate_li(filter_colors(all_colors)))

# chat AI enhanced

# Filtering colors that are 'sexy'
# def filter_colors(list_of_colors):
#     return [color['label'] for color in list_of_colors if color['sexy']]

# # Generating <li> elements for the filtered colors
# def generate_li(sexy_colors):
#     return list(map(lambda color: f"<li>{color}</li>", sexy_colors))

# # Get filtered colors
# sexy_colors = filter_colors(all_colors)

# # Print the filtered colors
# print(sexy_colors)

# # Print the generated <li> elements
# print(generate_li(sexy_colors))