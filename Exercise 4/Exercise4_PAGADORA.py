"""
Exercise 4
Maja Marem Jillzam B. Pagadora
2023-04953
BS Geodetic Engineering
"""


# constants 
"set variables as initial quantity in loop"

Start = 1
End = 2
Dis = 0
LatSum = 0
DepSum = 0



# lists used 

"Storage Data Base"

lines = []
Corr = []



# Imports "Relevant functions outside python"

from math import cos, sin, atan, radians, degrees, sqrt



# class 

class TextColor: #"spcified classifications for color_print"
    RED = '\033[91m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    END = '\033[0m'


class Line: # line descriptions - distance bearing, lat-dep
    def __init__(self, distance, azs):
        self.distance = distance
        self.azs = azs

    def latitude(self):
        '''
        Calculates the Latitude of the line using the set parameters

        The product of negative distance and cos azimuth from the
        south in radians

        Parameters: distance, azimuth
        '''
        latitude = - distance*cos(radians(azs))
        return latitude
    
    def departure(self):
        '''
        Calculates the Departure of the line using the set parameters

        The product of negative distance and sin azimuth from the
        south in radians

        Parameters: distance, azimuth
        '''
        departure = - distance*sin(radians(azs))
        return departure
    
    def bearing(self):
        '''
        Converts Azimuth from the South to Bearing

        Given Azimuth in DD - calculate bearing based on: if elif else conditions

        Parameters: azimuth
        '''

        if azs > 0 and azs < 90:
            az = azs
            degs = int(az)
            mins = int((az - degs)*60)
            secs = round(((((az - degs)*60)-mins)*60),2)
            dms = str(degs) + "-" + str(mins) + "-" + str(secs)
            bearing = "S " + str(dms) + " W"
        elif azs > 90 and azs < 180:
            az = 180 - azs
            degs = int(az)
            mins = int((az - degs)*60)
            secs = round(((((az - degs)*60)-mins)*60),2)
            dms = str(degs) + "-" + str(mins) + "-" + str(secs)
            bearing = "N " + str(dms) + " W"
        elif azs > 180 and azs < 270:
            az = azs - 180
            degs = int(az)
            mins = int((az - degs)*60)
            secs = round(((((az - degs)*60)-mins)*60),2)
            dms = str(degs) + "-" + str(mins) + "-" + str(secs)
            bearing = "N " + str(dms) + " E"
        else:
            az = 360 - azs
            degs = int(az)
            mins = int((az - degs)*60)
            secs = round(((((az - degs)*60)-mins)*60),2)
            dms = str(degs) + "-" + str(mins) + "-" + str(secs)
            bearing = "S " + str(dms) + " E"
        return bearing


class Cardinal(Line): #bearing of lines if azs divisible by 90"
    def __init__(self, distance, azs):
        super().__init__(distance, azs)

    def bearing(self):
        if azs == 0:
            bearing = "Due South"
        elif azs == 90:
            bearing = "Due West"
        elif azs == 180:
            bearing = "Due North"
        elif azs == 270:
            bearing = "Due East"
        else:
            bearing = "EWAN KO"
        return bearing
        
class Corrections(Line): # corrections in balancing the survey
    def __init__(self, distance, azs, LatSum, DepSum, Dis):
        super().__init__(distance, azs)
        self.LatSum = LatSum
        self.DepSum = DepSum
        self.Dis = Dis

    def corrLat(self):
        corrLat = -(distance/Dis)*LatSum
        return corrLat
    
    def corrDep(self):
        corrDep = -(distance/Dis)*DepSum
        return corrDep
    
class Adjusted(Corrections):

# Functions Set Functions catered to the Machine Exercise

def color_print(text, color):
    '''
    print colored text: text, color
    '''
    print(color + text + TextColor.END)

def floatInput(prompt):
    '''
    convert input into float
    '''
    prompt = float(input(prompt))
    return prompt



# title of the Activity
print()
color_print("MACHINE EXERCISE 4: Balancing the Survey using classes", TextColor.RED) 



# "MAIN LOOP Flow / Scheme of the Code"

while True:
    print()

# Line Descriptions(line from Point to Point, Distance, Azimuth/Bearing')
    color_print("LINE " + str(Start) + "-" + str(End), TextColor.CYAN)

    distance = floatInput("Enter Line Distance: ")
    azs = input("Enter Azimuth from the South: ")

    if "-" in azs:
        degrs, minutes, seconds = azs.split("-")
        azs = float((int(degrs) + (int(minutes)/60) + (float(seconds)/3600))) % 360
    else:
        azs = float(azs) % 360

    if azs % 90 == 0:
        line = Cardinal(distance, azs)
    else:
        line = Line(distance, azs)

    LatSum += line.latitude()
    DepSum += line.departure()
    Dis += float(line.distance)

# line lists'listing / storing line descriptions'

    lines.append((str(Start) + "-" + str(End), line.distance, line.bearing(), line.latitude(), line.departure()))

# Continuation / End of Loop 'the loop shall continue if:..., else: break'
    YN = (input("Add a New line? "))
    if YN.lower() == "yes" or YN.lower() == "y"or YN.lower() == "ye" or YN.lower() == "yah" or YN.lower() == "yeah":
        typ = (input("Will the new line be the closing line of the traverse ? "))
        if typ.lower() == "yes" or typ.lower() == "y" or typ.lower() == "ye" or typ.lower() == "yah" or typ.lower() == "yeah":
            Start = Start + 1
            End =  1
            continue
        else :
            Start = Start + 1
            End = End + 1
            continue
    else:  
        break

#  LEC and REC

LEC = sqrt((pow(LatSum, 2)) + (pow(DepSum,2)))
REC = round((abs(Dis/LEC)), -2)

#  BALANCING THE SURVEY

Correction = Corrections(distance, azs, LatSum, DepSum, Dis)
Corr.append((Correction.corrLat(), Correction.corrDep()))


# PRINT Line Description Table
color_print ("{:-^88}".format("-----------------------"), TextColor.BLUE)

color_print (("{: ^5} {: ^6} {: ^5} {: ^7} {: ^5} {: ^15} {: ^5} {: ^10} {: ^5} {: ^10} {: ^5} ". format(" ", "LINE", " ", "DISTANCE", " ", "BEARING", " ", "Latitude", " ", "Departure", "" )),TextColor.CYAN)

print ("{:-^88}".format("-----------------------"))

for line in lines:
    print ("{: ^5} {: ^6} {: ^5} {: ^7} {: ^5} {: ^15} {: ^5} {: ^10} {: ^5} {: ^10} {: ^5}". format("|", line[0], "|", round(line[1],3), "|", line[2],"|", round(line[3],3), "|", round(line[4],3), "|"))

color_print ("{:-^88}".format("-----------------------"), TextColor.BLUE)
print()

print ()

# PRINT the Linear Error of Closure and REC
print("LEC: "+ str(LEC))
print("REC: "+ "1 : " + str(REC))

# LOT DESCRIPTION TABLE - FINAL OUTPUT
print (Corr[0])
print (Corr[1])
color_print ("ADJUST LOT DESCRIPTION", TextColor.RED)

color_print ("{:-^77}".format("-----------------------"), TextColor.BLUE)

color_print(("{: ^5} {: ^15} {: ^5} {: ^15} {: ^5} {: ^20} {: ^5}". format(" ", "LINE", " ", "DISTANCE", " ", "BEARING", " ")), TextColor.CYAN)
print ("{:-^77}".format("-----------------------"))
for Lot_Description in LotDesc:
    print("{: ^5} {: ^15} {: ^5} {: ^15} {: ^5} {: ^20} {: ^5}". format("|", Lot_Description[0], "|", round(Lot_Description[1],3), "|", Lot_Description[2], "|"))

color_print ("{:-^77}".format("-----------------------"), TextColor.BLUE)
print()

color_print ("{: ^77}".format("~ END ~"), TextColor.RED)
