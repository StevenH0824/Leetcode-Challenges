#2114. Maximum Number of Words Found in Sentences
# A sentence is a list of words that are seperated by a single space
# with no leading or trailing spaces.
# You are given an array of strings sentences, where each sentence[i]
# represents a single sentence.
# Returns the maximum number of words that appear in a single sentence.

sentences1 = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
output1 = 6

sentences2 = ["please wait", "continue to fight", "continue to win"]
output2 = 3


def display(func, result):
    print("Result:\t", func == result, "\tFunction:\t",func, "\tDesired:\t",result)

def mostWordsFound(sentences: list[str]) -> int:
    max = 0
    words = ""
    for sentence in sentences:
        words = sentence.split()
        if max < len(words):
            max = len(words)
    return max


display(mostWordsFound(sentences1),output1)
display(mostWordsFound(sentences2),output2)

"""
Important to know the max function. I though of this idea first but I neglected to add +1 
to make the solution work. 
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max([s.count(" ") + 1 for s in sentences])
"""