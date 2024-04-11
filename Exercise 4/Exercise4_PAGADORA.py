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


# Imports "Relevant functions outside python"
from math import cos, sin, atan, radians, degrees, sqrt


# class 
"spcified classifications for color_print"

class TextColor:
    RED = '\033[91m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    END = '\033[0m'

class Line:
    def __int__(self, distance, azimuth):
        self.distance = distance
        self.azimuth = azimuth

    def getlatitude(self):
        '''
        Calculates the Latitude of the line using the set parameters

        The product of negative distance and cos azimuth from the
        south in radians

        Parameters: distance, azimuth
        '''
        latitude = - self.distance*cos(radians(self.azimuth))
        return latitude
    
    def getDeparture(self):
        '''
        Calculates the Departure of the line using the set parameters

        The product of negative distance and sin azimuth from the
        south in radians

        Parameters: distance, azimuth
        '''
        departure = - self.distance*sin(radians(self.azimuth))
        return departure
    
    def azimuthToBearing(self):
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
    
class Cardinal(Line):
    def azimuthToBearing(self):
        if azs == 0:
            bearing = "Due South"
        elif azs == 90:
            bearing = "Due West"
        elif azs == 180:
            bearing = "Due North"
        else:
            bearing = "Due East"
        return super().azimuthToBearing()

# Functions - MAIN CODE
"Set Functions catered to the Machine Exercise"

def color_print(text, color):
    'print colored text: text, color'
    print(color + text + TextColor.END)

def floatInput(prompt):
    '''
    convert input into float
    '''
    prompt = float(input(prompt))
    return prompt

# title of the Activity
print()
color_print("MACHINE EXERCISE 3: Balancing the Survey", TextColor.RED) 

# MAIN LOOP "Flow / Scheme of the Code"
while True:

# Line Description  
    'line from Point to Point, Distance, Azimuth/Bearing'
    print()
    color_print("LINE " + str(Start) + "-" + str(End), TextColor.CYAN)

    dist =floatInput("Enter Line Distance: ")
    azs = floatInput("Enter Azimuth from the South: ")

    if "-" in azs:
        degrs, minutes, seconds = azs.split("-")
        azs = (int(degrs) + (int(minutes)/60) + (float(seconds)/3600)) % 360
    else:
        azs = float(azs) % 360

# LatDep Bearing
    'Calculating the Latitude, Departure and Bearing using set functions'
    B = azimuthToBearing(azs)
    lat = getLatitude(dist, azs)
    dep = getDeparture (dist, azs)

# line lists - preBalancing lot description 
    'listing / storing line descriptions'
    line = [str(Start) + "-" + str(End) , dist, B, lat, dep]
    lines.append(line)

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
    # Calculate LEC and REC
        for line in lines:
            Dis += line[1]

        for line in lines:
            LatSum += line[3]

        for line in lines:
            DepSum += line[4]

        LEC = sqrt((pow(LatSum, 2)) + (pow(DepSum,2)))
        REC = round((abs(Dis/LEC)), -2)

    # Calculate Corrections
        for i in range(len(lines)):
            cl = getclat(lines[i][1], Dis, LatSum)
            clat.append(cl) 

            cd = getcdep(lines[i][1], Dis, DepSum)
            cdep.append(cd)

        for i in range(len(lines)) and range(len(clat)):
            AdjLat = BalL(lines[i][3], clat[i])
            ADJLat.append(AdjLat)

        for i in range(len(lines)) and range(len(cdep)):
            AdjDep = BalD(lines[i][4], cdep[i])
            ADJDep.append(AdjDep)

        for i in range(len(lines)) and range(len(clat)) and range(len(cdep)) and range(len(ADJLat)) and range(len(ADJDep)):
            corr = (lines[i][0], clat[i], cdep[i], ADJLat[i], ADJDep[i],)
            corrs.append(corr)

    # Adjusted Lot Description
        for i in range(len(ADJLat)) and range(len(ADJDep)):
            Adj_distance = AdjDist(ADJLat[i], ADJDep[i])
            ADJDis.append(Adj_distance)
        
            Adj_bear = AdjBearing(ADJLat[i], ADJDep[i])
            ADJb.append(Adj_bear)

        for i in range(len(ADJLat)) and range(len(ADJDep)) and range(len(lines)):
            Lot_Description = (lines[i][0], ADJDis[i], ADJb[i])
            LotDesc.append(Lot_Description)

        break

# PRINT Line Description Table
color_print ("{:-^88}".format("-----------------------"), TextColor.BLUE)

color_print (("{: ^5} {: ^6} {: ^5} {: ^7} {: ^5} {: ^15} {: ^5} {: ^10} {: ^5} {: ^10} {: ^5} ". format(" ", "LINE", " ", "DISTANCE", " ", "BEARING", " ", "Latitude", " ", "Departure", " ", "cLat", " ", "cDep", " ")),TextColor.CYAN)

print ("{:-^88}".format("-----------------------"))

for line in lines:
    print ("{: ^5} {: ^6} {: ^5} {: ^7} {: ^5} {: ^15} {: ^5} {: ^10} {: ^5} {: ^10} {: ^5}". format("|", line[0], "|", round(line[1],3), "|", line[2],"|", round(line[3],3), "|", round(line[4],3), "|"))

color_print ("{:-^88}".format("-----------------------"), TextColor.BLUE)
print()



# PRINT the Linear Error of Closure and REC
color_print("LEC: ", TextColor.RED)
color_print(str(LEC), TextColor.CYAN)
color_print("REC: " , TextColor.RED)
color_print("1 : " + str(REC), TextColor.CYAN)
print()

# LOT DESCRIPTION TABLE - FINAL OUTPUT
color_print ("{:-^77}".format("-----------------------"), TextColor.BLUE)

color_print(("{: ^5} {: ^15} {: ^5} {: ^15} {: ^5} {: ^20} {: ^5}". format(" ", "LINE", " ", "DISTANCE", " ", "BEARING", " ")), TextColor.CYAN)
print ("{:-^77}".format("-----------------------"))
for Lot_Description in LotDesc:
    print("{: ^5} {: ^15} {: ^5} {: ^15} {: ^5} {: ^20} {: ^5}". format("|", Lot_Description[0], "|", round(Lot_Description[1],3), "|", Lot_Description[2], "|"))

color_print ("{:-^77}".format("-----------------------"), TextColor.BLUE)
print()

color_print ("{: ^77}".format("~ END ~"), TextColor.RED)
