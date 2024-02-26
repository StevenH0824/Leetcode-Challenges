#1672. Richest Customer Wealth
#You are given an m x n integer grid accounts where accounts[i][j] is the amount of money
# the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

#A customer's wealth is the amount of money they have in all their bank accounts.
# The richest customer is the customer that has the maximum wealth.

accounts1 = [[1,2,3],[3,2,1]]
accounts2 = [[1,5],[7,3],[3,5]]
accounts3 = [[2,8,7],[7,1,3],[1,9,5]]

result1 = 6
result2 = 10
result3 = 17

# accounts[account][user]
def maximumWealth(accounts: list[list[int]]) -> int:
    max = total = 0
    for account in range(len(accounts)):
        # Don't need to use the second for loop
        # total = sum(accounts[account])
        for user in range(len(accounts[account])):
            total += accounts[account][user]
        if total > max:
            max = total
        total = 0
    return max

def check (func, result):
    print(func == result)

check(maximumWealth(accounts1),result1)
check(maximumWealth(accounts2),result2)
check(maximumWealth(accounts3),result3)

