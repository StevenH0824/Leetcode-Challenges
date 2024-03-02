#1678. Goal Parser Interpretation
# You own a Goal Parser that can interpret a string command.
# The command consists of an alphabet of "G", "()" and/or "(al)"
# in some order. The Goal Parser will interpret "G" as the string
# "G", "()" as the string "o" and "(al)" as  the string "al".
# The interpreter strings are then concatenated in the original
# order.
# Given the string command, return the Goal Parser's interpretation
# of command.


command1 = "G()(al)"
output1 = "Goal"

command2 = "G()()()()(al)"
output2 = "Gooooal"

command3 = "(al)G(al)()()G"
output3 = "alGalooG"

def display(func,result):
    print("Result:\t",func==result,"\tFunction:\t",func,"\t\tResult:\t",result)

def interpret(command: str) -> str:
    # I wanted to use this and only got the 2 base cases to work but not the 3rd.
    #commandValue = {'G': 'G',"()": 'o',"(al)":'al'}
    return command.replace('()','o').replace("(al)",'al')


display(interpret(command1),output1)
display(interpret(command2),output2)
display(interpret(command3),output3)

