#1365. How Many Numbers Are Smaller than the Current Number

# Given the array nums, for each nums[i] find out how many numbers in the
# array are smaller than it. That is, for each nums[i] you have to count the
# number of valid j's such that j != i and nums[j] < nums[i].

nums1 = [8,1,2,2,3]
output1 = [4,0,1,1,3]

nums2 = [6,5,4,8]
output2 = [2,1,0,3]

nums3 = [7,7,7,7]
output3 = [0,0,0,0]


def display(func,result):
    print("Function:\t{}\tOutput:\t{}\tResult:\t{}".format(func,result,func==result))


# Solution works but it's slow because of the O(n^2)
def smallerNumbersThanCurrent(nums: list[int]) -> list[int]:
    newList = []
    count = 0
    for index in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if (nums[index] > nums[j]):
                count += 1
        newList.append(count)
    return newList


display(smallerNumbersThanCurrent(nums1),output1)
display(smallerNumbersThanCurrent(nums2),output2)
display(smallerNumbersThanCurrent(nums3),output3)


"""
Uses a dictionary but improves on the general solution made by making it more efficient.

def smallerNumbersThanCurrent(nums: list[int]) -> list[int]:
    # Count occurrences of each number
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
    
    # Sort unique numbers
    unique_nums = sorted(counts.keys())
    
    # Build prefix sum of counts
    prefix_sum = {}
    total_count = 0
    for num in unique_nums:
        prefix_sum[num] = total_count
        total_count += counts[num]
    
    # Generate result using prefix sum
    result = [prefix_sum[num] for num in nums]
    
    return result
"""