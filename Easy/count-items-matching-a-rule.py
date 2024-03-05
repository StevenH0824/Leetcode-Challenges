# 1773. Count Items Matching a Rule
# You are given an array, where each list describes the type,
# color, and name of the item. You are also given a rule that is
# represented by two strings. 
# Item is said to match the rule if one of the following conditions
# are true. Return the number of items that match the given rule. 
# items[i] = [typei, colori, namei]


items1 = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
ruleKey1 = "color"
ruleValue1 = "silver"
output1 = 1

items2 = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]]
ruleKey2 = "type"
ruleValue2 = "phone"
output2 = 2


def display(func, result):
    print("Function:\t{}\tOutput:\t{}\tResult:{}\n".format(func,result, func==result))

def countMatches(items: list[list[str]], ruleKey: str, ruleValue: str) -> int:

    total = mtype = 0 

    # I need to find out what the rule key is to solve the problem.
    # Can I solve it while finding the rule value as well
    if ruleKey =="type":
        mtype = 0
    elif ruleKey == "color":
        mtype = 1
    else:
        mtype = 2
    
    for element in items:
        if element[mtype] == ruleValue:
            total += 1
    return total
display(countMatches(items1,ruleKey1,ruleValue1),output1)
display(countMatches(items2,ruleKey2,ruleValue2),output2)


"""
I really liked this solution. It made everything easier and more efficient. 

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if (ruleKey == "type"):
            k = 0
        elif (ruleKey == "color"):
            k = 1
        else:
            k = 2
        
        c = 0

        for i in items:
            if (i[k] == ruleValue):
                c += 1
        return c

# My first solution that worked after finding the mtype.

if ruleKey =="type":
    mtype = 0
elif ruleKey == "color":
    mtype = 1
else:
    mtype = 2

for index in range(len(items)):
        print(items[index])
        for element in range(len(items[index])):
            if mtype == element and items[index][element] == ruleValue:
                total += 1 
            #print(items[index][element], element, mtype)
"""