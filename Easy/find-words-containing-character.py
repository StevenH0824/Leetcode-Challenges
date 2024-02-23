#2942. Find Words Containing Character
#You are given a 0-indexed array of strings words and a character x.
#Return an array of indices representing the words that contain the character x.
#Note that the returned array may be in any order.
"""
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result = []
        for word in range(len(words)):
            for char in range(len(words[word])):
                if word in result:
                    continue
                elif (words[word][char] == x):
                    result.append(word)
        return result
"""

words1 = ["leet","code"]
x1 = "e"
words2 = ["abc","bcd","aaaa","cbc"]
x2 = "a"
words3 = ["abc","bcd","aaaa","cbc"]
x3 = "z"

result1 = [0,1]
result2 = [0,2]
result3 = []

def findWordsContaining(words:list[str], x:str) -> list[int]:
    result = []
    for word in range(len(words)):
        #print(word)
        for char in range(len(words[word])):
            if word in result:
                continue
            elif (words[word][char] == x):
                result.append(word)
    return result

def check(words:list[str],words2:list[str]) -> bool:
    return words == words2

print(check(findWordsContaining(words1,x1),result1))
print(check(findWordsContaining(words2,x2),result2))
print(check(findWordsContaining(words3,x3),result3))