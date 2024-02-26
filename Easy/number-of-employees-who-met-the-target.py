#2798. Number of employees Who met the target

# There are n employees in a company, numbered from 0 to n - 1. 
# Each employee i has worked for hours[i] hours in the company.

# The company requires each employee to work for at least target hours.

# You are given a 0-indexed array of non-negative integers hours of length n 
# and a non-negative integer target.

# Return the integer denoting the number of employees who worked at least target hours.

"""
class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        total = 0
        for employee in range(len(hours)):
            if hours[employee] >= target:
                total += 1
        return total
"""

hours1 = [0,1,2,3,4]
hours2 = [5,1,4,2,2]
hours3 = [98]

target1 = 2
target2 = 6
target3 = 5

output1 = 3
output2 = 0
output3 = 1

def numberOfEmployeesWhoMetTarget(hours: list[int], target: int) -> int:
    total = 0
    for employee in range(len(hours)):
        if hours[employee] >= target:
            total += 1
    return total

def check(func,result):
    print(func == result)

check(numberOfEmployeesWhoMetTarget(hours1,target1),output1)
check(numberOfEmployeesWhoMetTarget(hours2,target2),output2)
check(numberOfEmployeesWhoMetTarget(hours3,target3),output3)