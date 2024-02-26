# 1431 Kids with the greatest number of candies

# There are n kids with candies. 
# You are given an integer array candies, where each candies[i] represents 
# the number of candies the ith kid has, and an integer extraCandies, 
# denoting the number of extra candies that you have.

# Return a boolean array result of length n, where result[i] is true if,
# after giving the ith kid all the extraCandies, 
# they will have the greatest number of candies among all the kids, or false otherwise.

# Note that multiple kids can have the greatest number of candies.

candies = [2,3,5,1,3]
extraCandies = 3

candies2 = [4,2,1,1,2]
extraCandies2 = 1

candies3 = [12,1,12]
extraCandies3 = 10

output = [True,True,True,False,True] 
output2 = [True,False,False,False,False] 
output3 = [True,False,True]

def kidsWithCandies(candies: list[int], extraCandies: int) -> list[bool]:
    result = []
    for kid in range(len(candies)):
        if (candies[kid] + extraCandies) >= max(candies):
            result.append(True)
        else:
            result.append(False)
    return result

def check(func,output):
    print(func == output)

check(kidsWithCandies(candies, extraCandies),output)
check(kidsWithCandies(candies2, extraCandies2),output2)
check(kidsWithCandies(candies3, extraCandies3),output3)


