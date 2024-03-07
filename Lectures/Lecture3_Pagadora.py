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