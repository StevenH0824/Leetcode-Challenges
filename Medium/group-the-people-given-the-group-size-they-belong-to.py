# Learn more about hashmaps and get more practice with using dictionaries in python.
# 1282. Group the people Given the Group Size They Belong To

# I got the concept of what the question was asking but I was unable to solve it.
# I need to relearn hash tables and have more practice with using python dictionaries
#   

import collections

groupSizes = [3,3,3,3,3,1,3]
outputResult = [[5],[0,1,2],[3,4,6]]


def groupThePeople(groupSizes: list[int]) -> list[list[int]]:
    res = []
    hashmap = collections.defaultdict(list)

    for person,group in enumerate(groupSizes):
        if group in hashmap and len(hashmap[group]) == group:
            res.append(hashmap[group])
            hashmap[group] = []
        hashmap[group].append(person)
    
    for li in hashmap.values():
        if li: res.append(li)
    
    return res


print(groupThePeople(groupSizes))
