#1. two sum
# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.

# You can return the answer in any order.

nums = [2,7,11,15]
target = 9

nums2 = [3,2,4]
target2 = 6

nums3 = [3,3]
target3 = 6

def twoSum(nums: list[int], target: int) -> list[int]:
    for number in range(len(nums)):
        i = number
        while i < len(nums):
            if number == i:
                i += 1
            elif (nums[number] + nums[i] ) == target:
                return [number,i]
            else:    
                i += 1
    return []


print(twoSum(nums,target))
print(twoSum(nums2,target2))
print(twoSum(nums3,target3))

"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for number in range(len(nums)):
            i = number
            while i < len(nums):
                if number == i:
                    i += 1
                elif (nums[number] + nums[i] ) == target:
                    return [number,i]
                else:    
                    i += 1
        return []
"""