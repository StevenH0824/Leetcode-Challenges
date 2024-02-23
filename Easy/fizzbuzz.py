# Leetcode 412. FizzBuzz
#Given an integer n, return a string array answer (1-indexed) where:
#answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
#answer[i] == "Fizz" if i is divisible by 3.
#answer[i] == "Buzz" if i is divisible by 5.
#answer[i] == i (as a string) if none of the above conditions are true.

def fizzBuzz(n=15) -> list[str]:
    results = []
    for num in range(1,n+1):
        if num % 3 == 0 and num % 5 == 0:
            results.append("FizzBuzz")
        elif num % 3 == 0:
            results.append("Fizz")
        elif num % 5 == 0:
            results.append("Buzz")
        else:
            results.append(str(num))
    return results

print(fizzBuzz())

# Formatted solution that I solved in Leetcode
# class Solution:
#     def fizzBuzz(self, n: int) -> List[str]:
#         results = []
#         for num in range(1,n+1):
#             if num % 3 == 0 and num % 5 == 0:
#                 results.append("FizzBuzz")
#             elif num % 3 == 0:
#                 results.append("Fizz")
#             elif num % 5 == 0:
#                 results.append("Buzz")
#             else:
#                 results.append(str(num))
#         return results

# Original solution
# name = "FizzBuzz"
# end = 15
# for num in range(1,end+1):
#     if num % 3 == 0 and num % 5 == 0:
#         print(name)
#     elif num % 3 == 0:
#         print(name[:4])
#     elif num % 5 == 0:
#         print(name[4:])
#     else:
#         print(str(num))
