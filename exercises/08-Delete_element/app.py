people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

# def delete_person(person_name):
#     # Your code here
#     new_people = []

#     for person in people:
#         if person != person_name:
#             new_people.append(person)
#     return new_people

def delete_person(person_name):
    # Creating a new list by including only those persons whose name is not the one to be deleted
    new_people = [person for person in people if person != person_name]
    return new_people
    

    
# Don't delete anything below
print(delete_person("daniella"))
print(delete_person("juan"))
print(delete_person("emilio"))
