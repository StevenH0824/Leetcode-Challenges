#709. To lower case

# Given a string s, return the string after replacing every uppercase letter with the same
# lowercase letter.

s1 = "Hello"
result1 = "hello"

s2 = "here"
result2 = "here"

s3 = "LOVELY"
result3 = "lovely"


def toLowerCase(s: str) -> str:
    return s.lower()

def display (func,result):
    if func == result:
        print(True)
    else:
        print("Function: {}\tOutput:  {}".format(func,result))

display(toLowerCase(s1),result1)
display(toLowerCase(s2),result2)
display(toLowerCase(s3),result3)