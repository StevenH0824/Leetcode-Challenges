#2011. Final Value of Variable After Performing Operations
#There is a programming language with only four operations and one variable X:
# ++X and X++ increments the value of the variable X by 1.
# --X and X-- decrements the value of the variable X by 1.
# value of x is 0 initially

# Given an array of strings operations containing a list of operations, 
# return the final value of X after performing all the operations.
"""
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        result = 0
        for number in range(len(operations)):
            if (operations[number] == '--X') or (operations[number] == 'X--'):
                result -= 1
            elif (operations[number] == 'X++' or (operations[number] == '++X')):
                result += 1
        return result
"""

operations = ["--X","X++","X++"]

result = 0
for number in range(len(operations)):
    if (operations[number] == '--X') or (operations[number] == 'X--'):
        result -= 1
    elif (operations[number] == 'X++' or (operations[number] == '++X')):
        result += 1
print(result)