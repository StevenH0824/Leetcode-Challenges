# 1528. Shuffle String
# You are given a string and int array of the same length.
# The string will be shuffled such that the char position moves
# in the shuffled string.
# Return the suffled string

s1 = "codeleet"
indices1 = [4,5,6,7,0,2,1,3]
output1 = "leetcode"

s2 = "abc"
indices2 = [0,1,2]
output2 = "abc"

def display(func,result):
    print("Function:\t{}\tOutput:\t{}\tResult:\t{}".format(func,result,func==result))

def restoreString(s:str,indices: list[int]) -> str:
    newstr = ""
    count = 0
    
    while len(newstr) < len(s):
        if count in indices:
            newstr += s[indices.index(count)]
        count += 1
    return newstr

display(restoreString(s1,indices1),output1)
display(restoreString(s2,indices2),output2)