#1768. Merge String Alternately

# You are given two strings word1 and word2. 
# Merge the strings by adding letters in alternating order, starting with word1. 
# If a string is longer than the other, 
# append the additional letters onto the end of the merged string.
#Return the merged string.


word1 = "abc"
word2 = "pqr"
output1 = "apbqcr"


word3 = "ab"
word4 = "pqrs"
output2 = "apbqrs"

word5 = "abcd"
word6 = "pq"
output3 = "apbqcd"

def mergeAlternately(word1: str, word2: str) -> str:
    finalword = ""
    # Find the max and min lenght of each string
    if (len(word1) >= len(word2)):
        for char in range(len(word1)):
            if char == len(word2):
                break
            else:
                finalword += word1[char] + word2[char]
        finalword += word1[len(word2):]
    else:
        for char in range(len(word2)):
            if char == len(word1):
                break
            else:
                finalword += word1[char] + word2[char]
        finalword += word2[len(word1):]
    return finalword

def display(func,result):
    #print("Function:\t",func,"Result:\t",result)
    print("Result", func == result)

display(mergeAlternately(word1,word2),output1)
display(mergeAlternately(word3,word4),output2)
display(mergeAlternately(word5,word6),output3)



"""
This solution works, I changed this to strings but I need to get it to work
with different string lengths. 
nlist = []
for char in range(len(word1)):
    nlist.append(word1[char])
    nlist.append(word2[char])
print(nlist)
"""