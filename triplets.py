#Programmer: Ana Timpano
#Course Code: ICS4UE
#Date: March 3, 2020
#Decription: Creates a three lined rhyme/poem

import random #Imports random function

print("This program will create a triplet(a three lined poem) by selecting random words from lists") #Displays to the user what the program is
print(" ")


nouns = [] #A list of different nouns under the variable nouns
nouns.append("bear")
nouns.append("hare")
nouns.append("water")
nouns.append("air")
nouns.append("heart")
nouns.append("lion")
nouns.append("sky")
nouns.append("time")
nouns.append("day")
nouns.append("world")
nouns.append("body")
nouns.append("sun")
nouns.append("face")
nouns.append("eyes")


pastVerbs = [] #A list of different past verbs under the variable pastVerbs
pastVerbs.append("floated")
pastVerbs.append("blinded")
pastVerbs.append("accepted")
pastVerbs.append("became")
pastVerbs.append("awoke")
pastVerbs.append("thought")
pastVerbs.append("caught")
pastVerbs.append("fed")
pastVerbs.append("forgave")
pastVerbs.append("showed")
pastVerbs.append("asked")
pastVerbs.append("called")
pastVerbs.append("took")

presentVerbs = [] #A list of different present verbs under the variable presentVerbs
presentVerbs.append("fly")
presentVerbs.append("grow")
presentVerbs.append("hold")
presentVerbs.append("hide")
presentVerbs.append("admire")
presentVerbs.append("amuse")
presentVerbs.append("run")
presentVerbs.append("sleep")
presentVerbs.append("jump")
presentVerbs.append("hunt")
presentVerbs.append("eat")

rhymingNouns = [] #A list of different rhyming nouns under the variable rhymingNouns
rhymingNouns.append("goat")
rhymingNouns.append("boat")
rhymingNouns.append("coat")
rhymingNouns.append("note")
rhymingNouns.append("moat")
rhymingNouns.append("vote")
rhymingNouns.append("quote")
rhymingNouns.append("oat")
rhymingNouns.append("remote")
rhymingNouns.append("throat")
rhymingNouns.append("lifeboat")
rhymingNouns.append("rowboat")
rhymingNouns.append("wild oat")
rhymingNouns.append("overcoat")
rhymingNouns.append("treasury note")
rhymingNouns.append("rocky mountain goat")

# pop a random noun from the nouns list using len() to get the number of elements
randomNum = random.randint(0, len(nouns) - 1)
noun = nouns.pop(randomNum)

# pop the first random verb from the pastVerbs list
randomNum = random.randint(0, len(pastVerbs) - 1)
pastVerb = pastVerbs.pop(randomNum)

# pop the second random verb from presentVerbs list
randomNum = random.randint(0, len(presentVerbs) - 1)
presentVerb = presentVerbs.pop(randomNum)

# pop the first rhyming noun from rhymingNouns list
randomNum = random.randint(0, len(rhymingNouns) - 1)
rhymingNoun1 = rhymingNouns.pop(randomNum)

# pop the second rhyming noun from rhymingNouns list
randomNum = random.randint(0, len(rhymingNouns) - 1)
rhymingNoun2 = rhymingNouns.pop(randomNum)

# pop the third rhyming noun from rhymingNouns list
randomNum = random.randint(0, len(rhymingNouns) - 1)
rhymingNoun3 = rhymingNouns.pop(randomNum)

# Displays the poem
print("The " + noun + " " + pastVerb + " to the " + rhymingNoun1)
print("So it could " + presentVerb + " the " + rhymingNoun2)
print("But it was a " + rhymingNoun3)
