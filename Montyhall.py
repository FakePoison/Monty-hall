import random

#a list of doors to choose from, 2 winners 1 loser
#0 is a loser 1 is a winner
doorslist = [0, 0, 1]
#the order of winners and losers should not matter since the doors will be selected randomly anyway
#TODO randomize door list as well to prove this

#select a door
selecteddoor = random.choice(doorslist)
print(selecteddoor)

#next, remove the door from the list
doorslist.remove(selecteddoor)

#finally remove a losing door from the list, leaving one option
doorslist.remove(0)

#show the selected door and what was behind the remaining door
print(f'The chosen door was {selecteddoor} and the last door was {doorslist[0]}')