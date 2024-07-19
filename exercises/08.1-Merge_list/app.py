chunk_one = ['Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell']
chunk_two = ['Lucas', 'Jake', 'Scott', 'Amy', 'Molly', 'Hannah', 'Lucas']


def merge_list(list1, list2):
    # Your code here
    both_chunks = [person for person in list1] + [person for person in list2]

    return chunk_one + chunk_two

    
print(merge_list(chunk_one, chunk_two))
