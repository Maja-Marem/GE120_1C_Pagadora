"""
Exercise 3
Maja Marem Jillzam B. Pagadora
2023-04953
BS Geodetic Engineering
"""
# class

class TextColor:
    RED = '\033[91m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    END = '\033[0m'

# "constants"
Start = 1
End = 2
D = 0
LatSum = 0
DepSum = 0

# "lists"
lines = []
ratios = []
cLat = []
cDep = []
corrs = []

from math import cos, sin, radians, sqrt, exp2, floor

# Functions

def color_print(text, color):
    print(color + text + TextColor.END)

def getLatitude(distance, azs):
    latitude = - distance*cos(radians(azs))
    return latitude

def getDeparture(distance, azs):
    departure = - distance*sin(radians(azs))
    return departure

def azimuthToBearing(azs):
    if azs == 0:
        bearing = "Due South"
        return bearing
    elif azs > 0 and azs < 90:
        az = azs
        degrees = int(az)
        minutes = int((az - degrees)*60)
        seconds = round(((((az - degrees)*60)-minutes)*60),2)
        dms = str(degrees) + "-" + str(minutes) + "-" + str(seconds)
        bearing = "S " + str(dms) + " W"
        return bearing
    elif azs == 90:
        bearing = "Due West"
        return bearing
    elif azs > 90 and azs < 180:
        az = 180 - azs
        degrees = int(az)
        minutes = int((az - degrees)*60)
        seconds = round(((((az - degrees)*60)-minutes)*60),2)
        dms = str(degrees) + "-" + str(minutes) + "-" + str(seconds)
        bearing = "N " + str(dms) + " W"
        return bearing
    elif azs == 180:
        bearing = "Due North"
        return bearing
    elif azs > 180 and azs < 270:
        az = azs - 180
        degrees = int(az)
        minutes = int((az - degrees)*60)
        seconds = round(((((az - degrees)*60)-minutes)*60),2)
        dms = str(degrees) + "-" + str(minutes) + "-" + str(seconds)
        bearing = "N " + str(dms) + " E"
        return bearing
    elif azs == 270:
        bearing = "Due East"
        return bearing
    else:
        az = 360 - azs
        degrees = int(az)
        minutes = int((az - degrees)*60)
        seconds = round(((((az - degrees)*60)-minutes)*60),2)
        dms = str(degrees) + "-" + str(minutes) + "-" + str(seconds)
        bearing = "S " + str(dms) + " E"
        return bearing
    
def getclat(ratio, lat):
    corL = -(ratio)*lat
    return corL

def getcdep(ratio, dep):
    corD = -(ratio)*dep
    return corD

while True:

    # line description

    print()
    color_print("LINE " + str(Start) + "-" + str(End), TextColor.CYAN)
    print()

    dist =(float(input("Enter Line Distance: ")))
    azs = input("Enter Azimuth from the South: ")

    if "-" in azs:
        degrees, minutes, seconds = azs.split("-")
        azs = int(degrees) + (int(minutes)/60) + (float(seconds)/3600)
    else:
        azs = float(azs) % 360

    # LatDep Bearing
    
    B = azimuthToBearing(azs)
    lat = getLatitude(dist, azs)
    dep = getDeparture (dist, azs)

    # line lists input for table

    line = ["LINE " + str(Start) + "-" + str(End) , dist, B, lat, dep]
    lines.append(line)

    # Continuation / End of Loop
    
    YN = (input("Add a New line? "))
    if YN.lower() == "yes" or YN.lower() == "y"or YN.lower() == "ye" or YN.lower() == "yah" or YN.lower() == "yeah":
        typ = (input("Will the new line be the closing line for a traverse ? "))
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

for line in lines:
    D += line[1]
for line in lines:
    LatSum += line[3]
for line in lines:
    DepSum += line[4]

for i in range(len(lines)):
    ratio = lines[i][1]/D
    ratios.append(ratio)

for i in range(len(ratios)):
    clat = getclat(ratios[i], LatSum)
    cdep = getcdep(ratios[i], DepSum)

    cLat.append(clat)
    cDep.append(cdep)
        
LEC = sqrt(exp2(LatSum) + exp2(DepSum))
REC = floor((D/LEC)/100)*100

print()
color_print ("{:-^150}".format("-----------------------"), TextColor.BLUE)

color_print (("{: ^5} {: ^6} {: ^5} {: ^7} {: ^5} {: ^15} {: ^5} {: ^7} {: ^5} {: ^7} {: ^5} {: ^10} {: ^5} {: ^10} {: ^5}". format(" ", "LINE", " ", "DISTANCE", " ", "BEARING", " ", "Latitude", " ", "Departure", " ", "cLat", " ", "cDep", " ")),TextColor.CYAN)

print ("{:-^150}".format("-----------------------"))
for line in lines:
    print ("{: ^5} {: ^6} {: ^5} {: ^7} {: ^5} {: ^15} {: ^5} {: ^7} {: ^5} {: ^7} {: ^5} {: ^10} {: ^5} {: ^10} {: ^5}". format("|", line[0], "|", round(line[1],3), "|", line[2], "|", round(line[3],3), "|", round(line[4],3), "|", round(clat,5), "|", round(cdep,5), "|"))

color_print ("{:-^150}".format("-----------------------"), TextColor.BLUE)
print()

# LEC REC CALCULATIONS

print("LEC: " + str(LEC))

print("REC: " + "1 : " + str(REC))

color_print ("{: ^150}".format("~ END ~"), TextColor.RED)