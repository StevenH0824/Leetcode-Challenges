#1920. Build Array from Permutation
"""
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        newlist = []
        for number in range(len(nums)):
            newlist.append(nums[nums[number]])
        return newlist
"""
mylist = [0,2,1,5,3,4]
newlist = []
for number in range(len(mylist)):
    newlist.append(mylist[mylist[number]])
print(newlist)
