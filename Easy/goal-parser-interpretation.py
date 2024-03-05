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



"""
I really liked this solution since I was on this path originally before thinking of the
replace function in python. One thing that would have taken time would have been the 
conditional statement in order to get the right string. 
class Solution:
    def interpret(self, command: str) -> str:
        re=""
        for i in range(len(command)):
            if command[i]=='(' and command[i+1]==')':
                re+='o'
            elif command[i]=='(' and command[i+1]=='a':
                re+='al'
            elif command[i]=='G':
                re+=command[i]
        return re 

"""