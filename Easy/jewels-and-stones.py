#771. Jewels and Stones

# You're given strings jewels representing the types of stones that are
# jewels, and stones representing the stone you have. Each character in 
# stones is a type of stone you have. You want to know how many of the stones
# you have are also jewels.

# Letters are case sensitive, so "a" is considered a different type of stone
# from "A".

jewels1 = "aA"
stones1 = "aAAbbbb"
output1 = 3

jewels2 = "z"
stones2 = "ZZ"
output2 = 0

def display(func, result):
    print("Result is ",func==result, "\t Function Output:\t",func,"\t Desired Output:\t",result)


def numJewelsInStones(jewels: str, stones: str) -> int:
    storage = dict()
    count = 0

    for char in jewels:
        storage[str(char)] = 0

    for stone in stones:
        if stone in storage:
            count += 1
            # Update the dictionary in case you ever want to return the dictionary. 
            #storage[str(char)] = count 
    return count


display(numJewelsInStones(jewels1,stones1),output1)
display(numJewelsInStones(jewels2,stones2),output2)


"""
I like this solution a lot more than what I came up with. Making everything into a list
automatically seperating the values is so much better than using the for loop that I came up
with. 

def numJewelsInStones(self, jewels: str, stones: str) -> int:
        a=list(jewels)
        s=0
        for i in a:
            s+=stones.count(i)
        return s
"""
