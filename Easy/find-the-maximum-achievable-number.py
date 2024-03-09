# 2769. Find the Maximum Achievable Number

# You are given two integers, num and t

# An integer x is called achievable if it can become equal to num after applying
# the following operation no more than t times

# increase or decrease x by 1, and simultaneously increase or decrease num by 1.

# Return the maximum possible achievable number. It can be proven that there exists at 
# least one achievable number.

num1 = 4
t1 = 1
output1 = 6

num2 = 3
t2 = 2
output2 = 7

def display(func,result):
    print("Function:\t{}\tDesired:\t{}\tResult:\t{}".format(func,result,func==result))


def theMaximumAchievableX(num: int, t: int) -> int:
    return num + t + t

display(theMaximumAchievableX(num1,t1),output1)
display(theMaximumAchievableX(num2,t2),output2)