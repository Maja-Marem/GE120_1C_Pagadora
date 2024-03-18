"""
Lecture 1: Programming Basics
(c) Dominic Fargas Jr
February 21, 2022
"""

# PART 1: Cloning Repository

print('Kumusta World')
character_annie = 'Kiko' # naming the characters of out story
mother = 'Leni'

# They went to the market
sentence = character_annie + ' and ' + mother + ' went to the market.' 
# print(sentence)
# print(type(character_annie))

# Mga Bilihin ni Jo
list_of_bilihin = ["carrots", "cabbage", "patatas"]
# print(list_of_bilihin[1])

cabbages = 21
patatas = 365
# 1 nilaga = 2 cabbages and 3 patatas, how many nilaga can I make, and how many patatas left?
nilaga = cabbages // 2
number_of_patatas_left = patatas - nilaga*3

# print("Number of Nilaga:", nilaga)
# print("number of patatas left:", number_of_patatas_left)

name = "121-12-13"
letters = name.split('-')
print(letters)