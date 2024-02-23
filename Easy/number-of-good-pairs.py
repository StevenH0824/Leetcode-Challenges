#1512. Number of Good Pairs
"""
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        total = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (nums[i] == nums[j]) and (i < j):
                    total += 1
        return total
"""

nums = [1,2,3,1,1,3]
total = 0
for i in range(len(nums)):
    for j in range(len(nums)):
        if (nums[i] == nums[j]) and (i < j):
            total += 1
print(total)