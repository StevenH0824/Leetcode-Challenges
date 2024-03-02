#1108. Defanging an IP Address
# Given a valid IP address, return a defanged version of that IP address
# A defanged IP address replaces every period "." with "[.]".


address1 = "1.1.1.1"
output1 = "1[.]1[.]1[.]1"

address2 = "255.100.50.0"
output2 = "255[.]100[.]50[.]0"

def display(func, result):
    print("The Result is ",func == result)

def defangIPaddr(address: str) -> str:
    newip = ""

    for char in address:
        if char != ".":
            newip += char
        else:
            newip += "[.]"
    return newip



display(defangIPaddr(address1),output1)
display(defangIPaddr(address2),output2)
        
