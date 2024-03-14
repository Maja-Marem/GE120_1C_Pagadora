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
clat = []
cdep = []
ADJLat = []
ADJDep = []
corrs = []
ADJDis = []
ADJB = []

from math import cos, sin, atan, radians, degrees, sqrt, exp2, floor

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

def getclat(rat, lat):
    corL = -(rat)*lat
    return corL

def getcdep(rat, dep):
    corD = -(rat)*dep
    return corD

def BalL(Lat, corL):
    AdjL = corL + Lat
    return AdjL

def BalD(Dep, corD):
    AdjD = Dep + corD
    return AdjD

def AdjDist(LAT, DEP):
    distan = sqrt(exp2(LAT) + exp2(DEP))
    return distan

# MAIN LOOP
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
    # TOTAL Distance, Latitude, Departure
        for line in lines:
            D += line[1]
        for line in lines:
            LatSum += line[3]
        for line in lines:
            DepSum += line[4]

    # For Corrections
        for i in range(len(lines)):
            ratio = lines[i][1]/D
            ratios.append(ratio)

        for i in range(len(ratios)):
            cl = getclat(ratios[i], LatSum)
            clat.append(cl) 

            cd = getcdep(ratios[i], DepSum)
            cdep.append(cd)

        for i in range(len(lines)) and range(len(clat)):
            AdjLat = BalL(lines[i][3], clat[i])
            ADJLat.append(AdjLat)

        for i in range(len(lines)) and range(len(cdep)):
            AdjDep = BalD(lines[i][4], cdep[i])
            ADJDep.append(AdjDep)

        for i in range(len(ADJLat)) and range(len(ADJDep)):
            Adj_distance = AdjDist(ADJLat[i], ADJDep[i])

        for i in range(len(lines)) and range(len(clat)) and range(len(cdep)) and range(len(ADJLat)) and range(len(ADJDep)):
            corr = (lines[i][0], clat[i], cdep[i], ADJLat[i], ADJDep[i],)
            corrs.append(corr)
        break

# ERRORS OF CLOSURE - Calculating LEC AND REC
LEC = sqrt(exp2(LatSum) + exp2(DepSum))
REC = round((abs(D/LEC)), -3)


# PRINT Line tables
    
print()
color_print ("{:-^88}".format("-----------------------"), TextColor.BLUE)

color_print (("{: ^5} {: ^6} {: ^5} {: ^7} {: ^5} {: ^15} {: ^5} {: ^7} {: ^5} {: ^10} {: ^5} ". format(" ", "LINE", " ", "DISTANCE", " ", "BEARING", " ", "Latitude", " ", "Departure", " ", "cLat", " ", "cDep", " ")),TextColor.CYAN)

print ("{:-^88}".format("-----------------------"))
for line in lines:
    print ("{: ^5} {: ^6} {: ^5} {: ^7} {: ^5} {: ^15} {: ^5} {: ^7} {: ^5} {: ^10} {: ^5}". format("|", line[0], "|", round(line[1],3), "|", line[2],"|", round(line[3],3), "|", round(line[4],3), "|"))

color_print ("{:-^88}".format("-----------------------"), TextColor.BLUE)
print()

# LEC REC CALCULATIONS2

print()

print("LEC: " + str(LEC))
print("REC: " + "1 : " + str(REC))

print()
color_print ("{:-^92}".format("-----------------------"), TextColor.BLUE)

color_print(("{: ^5} {: ^10} {: ^5} {: ^10} {: ^5} {: ^10} {: ^5} {: ^10} {: ^5} {: ^10} {: ^5}". format(" ", "LINE", " ", "cLat", " ", "cDep", " ", "Adj Lat", " ", "Adj Dep", " ")), TextColor.CYAN)
print ("{:-^92}".format("-----------------------"))
for corr in corrs:
    print("{: ^5} {: ^10} {: ^5} {: ^10} {: ^5} {: ^10} {: ^5} {: ^10} {: ^5} {: ^10} {: ^5}". format("|", corr[0], "|", round(corr[1],5), "|", round(corr[2],5), "|", round(corr[3],3), "|", round(corr[4],3), "|"))

color_print ("{:-^92}".format("-----------------------"), TextColor.BLUE)

print()

color_print ("{: ^92}".format("~ END ~"), TextColor.RED)