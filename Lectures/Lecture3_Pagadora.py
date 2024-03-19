# lists - acces by index number []

list = ["mafe", "justin", "mika", "uste"]
print(list)
print(list[2])
print(list[0:2]) 
# "/:2"
print(list[2:3]) 
# "/2:"
print(list[-1])

list[0] = "chelzy"
print(list)



# tuple - access by index number ()
tuple_1 = ("maja", "gianna", "jewel")

# immutable
tuple_1 [0] = "quinmar"
# valus irreplacable unlike list

# NESTED Lists / also works on tuples
list1 = [["apple", "bola", "karton"], ["appricot", "banana", "cow"]]
print(list1[0][2])



# dictionary - consists of key value pairs, access by key {}
dog = {"name": "bogart", "age": "2", "color": "white", "fave_num": "3.14"}

print(dog["name"])
print(dog.values())
print(dog.keys())

dog["fave_num"] = 39

print(dog["fave_num"])

# Pseudocode - coding on paper, not actual syntax, logic of the code
# flow charts - visual representation of the coding logic
# Algorithms - solving base on steps on solving the problem


#  Structured Programming

# Control Structures : 
"""
SELECTION - depends on specific values
ITERATION - 
SEQUENCE - 
"""

degrees = int(AzS)
minutes = int((AzS - degrees)*60)
seconds = round(((((AzS - degrees)*60)-minutes)*60),2)
DMS = "S " + "-" + str(degrees) + "-" + str(minutes) + "-" + str(seconds) + " W"

# Lecture 3Notes

# LISTS
listahan = ["mafe", "justin", "mika", "uste"]
# print(listahan)

# gusto si mika makuha (position)
# print(listahan[2])

# subset of the list, mafe and si justin
# print(listahan[0:2])

# print(listahan[1:3])

# nagstastart sa simula
# print(listahan[:3])

# start from index, end sa dulo
# print(listahan[2:])

# print(listahan[-1])
# print(listahan[-2])

# gets first item, last item, then those in between
# print(listahan[-3:3])

# Addition of Lists
# print(listahan[0:2]+listahan[2:4])
# print(listahan[0:4])

listahan[0] = "chelzy"
# print(listahan)

# TUPLES
tuple_1 = ("maja", "gianna", "jewel")
# print(tuple_1)

# tuples are immutable
# tuple_1[0] = "quinmar"

# print(tuple_1)

# NESTED LISTS
list_1 = [ ["apple", "bola", "carton"] , ["apricot", "banana", "cow"]  ]
# print(list_1[0][2])

# NESTED TUPLES
tuple_2 = ((12.1244, -12.12414),(35.46261,-67.1231),(123.124, 56.232))
# print(tuple_2[2][0])

# DICTIONARIES - key value pairs
dog = {
        "name": "Bogart",
        "age": 2,
        "color": "white",
        "favorite_num": 3.14,
        1.113: 45  #pwede si number as key (float or int)
       }

# print(dog[1.113])
# print(dog.values())  #returns a list of values
# print(dog.keys())  #returns a list of keys

dog["favorite_num"] = 39

# print(dog["favorite_num"])


# LOOPS AND BREAK CONTINUE AND PASS

# for number in range(10):
#     if number == 5:
#         pass

rec = 0
while rec <= 5000:
    rec = int(input("enter REC: "))
    kulang = 5000 - rec
    if rec >= 4500:
        pass
        print("onti nalang kulang, kaya mo yan")
    print("kulang ka ng REC na", kulang)

print("PASOK NA REC")
print("-------END-----")

help(len)