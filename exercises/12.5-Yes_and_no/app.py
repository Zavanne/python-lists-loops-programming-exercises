the_bools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

# Your code here
wiki_woko_list = []

for bool in the_bools:
    if bool == 0:
        wiki_woko_list.append('woko')
    else:
        wiki_woko_list.append('wiki')

wiki_woko_list = []

# Using list comprehension
wiki_woko_list = ['woko' if bool == 0 else 'wiki' for bool in the_bools]

wiki_woko_list = []

# Using lambda with map
wiki_woko_list = list(map(lambda x: 'woko' if x == 0 else 'wiki', the_bools))

print(wiki_woko_list)

