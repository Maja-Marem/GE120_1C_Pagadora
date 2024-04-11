# OBJECT ORIENTED PROGRAMMING

" class - blue print/template in creating a specific type of object "
" object - specimen of a class"

# creating classes
" make sure the name of class is capital - by standard "

class  Crayon:
    pass    #  blueprint/template of the class - attributes
"wala syang gagawin"

redcrayon = Crayon()
print(type(redcrayon))

"""
atribute: characteristics - defined using the self node (self.atribute 
under the definition)
methods: Actions/Behavior - self is a parameter
"""

# creating ML Heroes
"""
class ML_Hero:
    def __init__(self):
        self.name = "LUNOX"
        self.description = "Twilight Goddess"
        self.role = "Mage"
        self.specialty = "Damage/Poke"
        self.statistics = {"durability": 60, "offense": 50}
"""

class MLHero:
    def __init__(self, name, description = "Twilight Goddess"):
        self.name = name
        self.description = description
        self.role = "Mage"
        self.specialty = "Damage/Poke"
        self.statistics = {"durability": 60, "offense": 50}

    def __str__(self):
        return(self.name + "the " + self.description)

    def skill(self):
        print("ATTACK")

hero = MLHero("Lunox ", "Masipag na UP Student")

print(hero)
print("Hero Name:", hero.name)

hero.skill()

# split is just METHOD of the class string
text = "HELLO, PLUS, ME"
text.split()

# Relationships
"""
relationship - Generalizatoin-Specialization (super/subclass)
Inheritance - Superclass is general can have additional super class
superclass:person
subclas: student, faculty, staff

Person - student
Person - Staff

Class Docstrings

"""