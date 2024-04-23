#2824. Count Pairs Whose Sum is Less than Target

# Given a 0-indexed integer array nums of length n and an integer target,
# return the number of pairs (i,j) where 0 <= i < j < n and
# nums[i] + nums[j] < target.


nums1 = [-1,1,2,3,1]
target1 = 2
output1 = 3

nums2 = [-6,2,5,-2,-7,-1,3]
target2 = -2
output2 = 10

nums3 = [9,-5,-5,5,-5,-4,-6,6,-6]
target3 = 3
output3 = 27

def display(func,result):
    print("Function:\t{}\tOutput:\t{}\tResult:\t{}".format(func,result,func==result))


#  0 <= i < j < n and nums[i] + nums[j] < target
# failed a test case
def countPairs(nums: list[int], target: int) -> int:
    total = 0
    for i in nums:
        for j in nums:
            if ( i < j ) and ((i + j) < target):
                total += 1
    return total


def countPairs1(nums: list[int], target: int) -> int:
    total = 0
    for i in nums:
        for j in nums:
            if (i < j) and ((i + j) <= target):
                total += 1
    return total


#display(countPairs(nums1,target1),output1)
#display(countPairs(nums2,target2),output2)
display(countPairs1(nums3,target3),output3)