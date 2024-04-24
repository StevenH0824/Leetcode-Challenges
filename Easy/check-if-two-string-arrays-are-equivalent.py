# Check if two string arrays are equivalent

# Given two strings arrays word1 and word2, return true if the two arrays represent
# the same string, and false, otherwise.

# A string is a represented by an array if the array elements concatenated in order forms
# the string

worda = ["ab", "c"]
wordb = ["a", "bc"]
result1 = True

wordc = ["a", "cb"]
wordd = ["ab", "c"]
result2 = False

worde  = ["abc", "d", "defg"]
wordf = ["abcddefg"]
result3 = True

def arrayStringsAreEqual(word1: list[str], word2: list[str]) -> bool:
    return "".join(word1) == "".join(word2)
    # Function is a bit longer but more readable to me. 
    str1 = "".join(word1)
    str2 = "".join(word2)
    if str1 == str2:
        return True
    else:
        return False

def display(func,result):
    if (func == result):
        print("True")
    else:
        print("Function: {}\tOutput:{}".format(func,result))

display(arrayStringsAreEqual(worda,wordb),result1)
display(arrayStringsAreEqual(wordc,wordd),result2)
display(arrayStringsAreEqual(worde,wordf),result3)