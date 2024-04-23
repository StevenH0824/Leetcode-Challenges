# 1816 Truncate Sentence
# A sentence is a list of words that are seperated by a single space with no leading or 
# trailing spaces. Each of the words consists of only uppercase or lowercase English letters. 
# For example, "Hello World", "HELLO", and "hello world hello world" are all sentences.
# You are given a sentence s​​​​​​ and an integer k​​​​​​. You want to truncate s​​​​​​
# such that it contains only the first k​​​​​​ words. Return s​​​​​​ after truncating it.

s1 = "Hello how are you Contestant"
k1 = 4
result1 = "Hello how are you"

s2 = "What is the solution to this problem"
k2 = 4
result2 = "What is the solution"

s3 = "chopper is not a tanuki"
k3 = 5
result3 = "chopper is not a tanuki"


def truncateSentence(s: str, k: int) -> str:
    strValue = s.split()
    if k >= len(strValue):
        return s
    else:
        sentence = strValue[:k]
        return " ".join(sentence)

def display(func,result):
    if (func == result):
        print(True)
    else:
        print("Function:\t{}\tOutput:\t{}".format(func,result))

display(truncateSentence(s1,k1),result1)
display(truncateSentence(s2,k2),result2)
display(truncateSentence(s3,k3),result3)