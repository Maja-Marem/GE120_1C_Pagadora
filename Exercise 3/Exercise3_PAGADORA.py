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

# "lists"
lines=[]
from math import cos, sin, radians

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
    
while True:

    # line description

    print()
    color_print("LINE " + str(Start) + "-" + str(End), TextColor.CYAN)
    print()

    distance =(float(input("Enter Line Distance: ")))
    dist = round(distance, 3)
    azs = float(input("Enter Azimuth from the South: ")) % 360

    # LatDep Bearing
    
    B = azimuthToBearing(azs)
    lat = round(getLatitude(distance, azs),3)
    dep = round(getDeparture (distance, azs),3)

    # line lists input for table

    line = ("LINE " + str(Start) + "-" + str(End) , str(dist), B, lat, dep)
    lines.append(line)

    # Continuation / End of Loop
    
    YN = (input("Add a New line? "))
    if YN.lower() == "yes" or YN.lower() == "y"or YN.lower() == "ye" or YN.lower() == "yah" or YN.lower() == "yeah":
        typ = (input("Is this a closing line for a polygon ? "))
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
 

print()

color_print ("{:-^150}".format("-----------------------"), TextColor.BLUE)
color_print (("{: ^5} {: ^10} {: ^5} {: ^10} {: ^5} {: ^15} {: ^5} {: ^10} {: ^5} {: ^10} {: ^5}". format(" ", "LINE", " ", "DISTANCE", " ", "BEARING", " ", "Latitude", " ", "Departure", " ")),TextColor.CYAN)
print ("{:-^150}".format("-----------------------"))
for line in lines:
    print ("{: ^5} {: ^10} {: ^5} {: ^10} {: ^5} {: ^15} {: ^5} {: ^10} {: ^5} {: ^10} {: ^5}". format("|", line[0], "|", line[1], "|", line[2], "|", line[3], "|", line[4], "|"))
color_print ("{:-^150}".format("-----------------------"), TextColor.BLUE)
print()

color_print ("{: ^150}".format("~ END ~"), TextColor.RED)