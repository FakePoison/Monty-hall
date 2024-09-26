import random


#a list of doors to choose from, 2 winners 1 loser
#0 is a loser 1 is a winner
doorslist = [0, 0, 1]
#the order of winners and losers should not matter since the doors will be selected randomly anyway
#TODO randomize door list as well to prove this

#function to run iterations of the problem
def montyiter(repeats):
    i = repeats
    x = 0
    while i > 0:
        dlist = doorslist.copy()
#select a door
        selecteddoor = random.choice(doorslist)

#next, remove the door from the list
        dlist.remove(selecteddoor)

#finally remove a losing door from the list, leaving one option
        dlist.remove(0)

#show the selected door and what was behind the remaining door
#print(f'The chosen door was {selecteddoor} and the last door was {doorslist[0]}')
        if selecteddoor == 1:
            x += 1
        
        i -= 1
    
    print(f'Guessed correct {x} out of {repeats} times')

montyiter(1000)