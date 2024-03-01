# 1480. Running Sum of 1D array
#   Given an array nums. We define a running sum of an array as 
#   runningSum[i] = sum(nums[0]…nums[i]).
#   Return the running sum of nums.

#class Solution:
#    def runningSum(self, nums: List[int]) -> List[int]:

def display(func, result):
    print(func == result)


def runningSum(nums: list[int]) -> list[int]:
    newlist = []
    for number in range (len(nums)):
        if number == 0:
            newlist.append(nums[number])
        else:
            index = number
            total = nums[number]
            while index > 0:
                total += nums[number - index]
                index -= 1
            newlist.append(total)
    return newlist

input1 = [1,2,3,4]          # [1, 1+2, 1+2+3, 1+2+3+4]
output1 = [1,3,6,10]

input2 = [1,1,1,1,1]
output2 = [1,2,3,4,5]

input3 = [3,1,2,10,1]
output3 = [3,4,6,16,17]


display(runningSum(input1),output1)
display(runningSum(input2),output2)
display(runningSum(input3),output3)




"""
My first solution which lead me to the second solution. I was thinking of using recursion
as well.
for number in range (len(nums)):    
        if number == 0:
            total.append(nums[number])
        if (number == 1):
            total.append(nums[number] + nums[number-1])
        if (number == 2):
            total.append(nums[number] + nums[number-1] + nums[number-2])
        if (number == 3):
            total.append(nums[number] + nums[number-1] + nums[number-2] + nums[number-3])
"""