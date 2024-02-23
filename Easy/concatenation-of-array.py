#1929. Concatenation of Array
"""
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_list = nums.copy()
        for number in range(0,len(nums)):
            new_list.append(nums[number])
        return new_list
"""
nums = [1,2,1]
new_array = []
new_array = nums.copy()
for number in range(0,len(nums)):
    new_array.append(nums[number])
print(new_array)

# This solution is way more efficient, forgot this was a feature of python.
new_array2 = nums + nums
print(new_array2)
