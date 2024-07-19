incoming_ajax_data = [
    { "name": 'Mario', "last_name": 'Montes' },
    { "name": 'Joe', "last_name": 'Biden' },
    { "name": 'Bill', "last_name": 'Clon' },
    { "name": 'Hilary', "last_name": 'Mccafee' },
    { "name": 'Bobby', "last_name": 'Mc birth' }
]

# Your code here
# def data_transformer(list):
#     formatted_names = []
#     for person in list:
#         formatted_names.append(person['name'] + " " + person['last_name'])
#     return formatted_names

# print(data_transformer(incoming_ajax_data))

# def data_transformer(person):
#     return person['name'] + " " + person['last_name']

# formatted_names = list(map(data_transformer, incoming_ajax_data))
# print(formatted_names)

def data_transformer(list_of_names):
    return list(map(lambda person: person['name'] + " " + person['last_name'] , list_of_names))

print(data_transformer(incoming_ajax_data))





