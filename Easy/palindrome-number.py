# 9. Palindrome Number
# Given an integer x, return true if x is a palindrome, and false otherwise.

"""
def isPalindrome(x: int) -> bool:
    snum = str(x)
    return snum == snum[::-1]
"""

input1 = 121
result1 = True

input2 = -123
result2 = False

input3 = -10
result3 = False

def display(func, result):
    print(func == result)
    #func ==result


def isPalindrome(x: int) -> bool:
    # without using a string

    num2 = x
    if (x < 0):
        return False
    elif (x == 0):
        return True
    else:
        while(num2 > 0):
            num2 = int(num2 / x)
            if (num2 == 1):
                return True
            else:
                return False
    #print(x,num2)
    return True



display(isPalindrome(input1),result1)
display(isPalindrome(input2),result2)
display(isPalindrome(input3),result3)