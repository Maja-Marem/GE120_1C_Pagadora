"""
Exercise 2
Maja Marem Jillzam B. Pagadora
2023-04953
BS Geodetic Engineering
"""

# constants/lists/Class

"class"
class TextColor:
    RED = '\033[91m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    END = '\033[0m'

def color_print(text, color):
    print(color + text + TextColor.END)

"constants"
Start = 1
End = 2

"lists"
lines=[]

# title of program

print()
color_print("LINE DESCRIPTIONS: (closed polygon - line Series)", TextColor.RED)


# main loop

while True:

    # line description

    print()
    color_print("LINE " + str(Start) + "-" + str(End), TextColor.CYAN)
    print()

    distance =(float(input("Enter Line Distance: ")))
    dist = round(distance, 6)
    azs = float(input("Enter Azimuth from the South: ")) % 360

    # Azimuth from the South in Decimal Degrees to Bearing in DMS
    
    if azs == 0:
        bearing = "Due South"
    elif azs > 0 and azs < 90:
        az = azs
        degrees = int(az)
        minutes = int((az - degrees)*60)
        seconds = round(((((az - degrees)*60)-minutes)*60),2)
        dms = str(degrees) + "-" + str(minutes) + "-" + str(seconds)
        bearing = "S " + str(dms) + " W"
    elif azs == 90:
        bearing = "Due West"
    elif azs > 90 and azs < 180:
        az = 180 - azs
        degrees = int(az)
        minutes = int((az - degrees)*60)
        seconds = round(((((az - degrees)*60)-minutes)*60),2)
        dms = str(degrees) + "-" + str(minutes) + "-" + str(seconds)
        bearing = "N " + str(dms) + " W"
    elif azs == 180:
        bearing = "Due North"
    elif azs > 180 and azs < 270:
        az = azs - 180
        degrees = int(az)
        minutes = int((az - degrees)*60)
        seconds = round(((((az - degrees)*60)-minutes)*60),2)
        dms = str(degrees) + "-" + str(minutes) + "-" + str(seconds)
        bearing = "N " + str(dms) + " E"
    elif azs == 270:
        bearing = "Due East"
    else:
        az = 360 - azs
        degrees = int(az)
        minutes = int((az - degrees)*60)
        seconds = round(((((az - degrees)*60)-minutes)*60),2)
        dms = str(degrees) + "-" + str(minutes) + "-" + str(seconds)
        bearing = "S " + str(dms) + " E"

    # line lists input for table

    line = ("LINE " + str(Start) + "-" + str(End) , str(dist), bearing)
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


# table of values
print()

color_print ("{:-^71}".format("-----------------------"), TextColor.BLUE)
color_print (("{: ^5} {: ^10} {: ^5} {: ^20} {: ^5} {: ^15} {: ^5}". format(" ", "LINE", " ", "DISTANCE", " ", "BEARING", " ")),TextColor.CYAN)
print ("{:-^71}".format("-----------------------"))
for line in lines:
    print ("{: ^5} {: ^10} {: ^5} {: ^20} {: ^5} {: ^15} {: ^5}". format("|", line[0], "|", line[1], "|", line[2], "|"))
color_print ("{:-^71}".format("-----------------------"), TextColor.BLUE)
print()

color_print ("{: ^65}".format("~ END ~"), TextColor.RED)