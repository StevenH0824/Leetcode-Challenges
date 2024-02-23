# 1470. Shuffle the Array
# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
# Return the array in the form [x1,y1,x2,y2,...,xn,yn].
"""
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums2 = nums[n:]
        result = []
        for number in range(len(nums2)):
            result.append(nums[number])
            result.append(nums2[number])
        return result
"""

def shuffle (nums = list[int], n = 4) -> list[int]:
    nums2 = nums[n:]
    result = []
    for number in range(len(nums2)):
        result.append(nums[number])
        result.append(nums2[number])
    return result

def compare (num1 = list[int], num2 = list[int]) -> bool:
    return num1 == num2    

print(compare(shuffle([2,5,1,3,4,7],3),[2,3,5,4,1,7]))
print(compare(shuffle([1,2,3,4,4,3,2,1],4),[1,4,2,3,3,2,4,1]))
print(compare(shuffle([1,1,2,2],2),[1,2,1,2]))





