"""
Exercise 1
Maja Marem Jillzam B. Pagadora
2023-04953
BS Geodetic Engineering
"""
print()
print()
print("LINE DESCRIPTIONS: (closed polygon - line Series)")

# constants/lists

Start = 1
End = 2
lines=[]

while True:

# line description

    print()
    print()
    print("LINE " + str(Start) + "-" + str(End))
    print()

    dist = round((float(input("Enter Line Distance: "))),2)
    azs = round((float(input("Enter Azimuth from the South: ")) % 360),6)
    print()

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
    if YN == "yes":
        typ = (input("Is this a closing line for a polygon ? "))
        if typ == "yes":
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
print ("{:-^80}".format("-----------------------"))
print ("{: ^10} {: ^10} {: ^10} {: ^10} {: ^10} {: ^15} {: ^10}". format("|", "LINE" , "|", "DISTANCE", "|", "BEARING", "|"))
for line in lines:
    print ("{: ^10} {: ^10} {: ^10} {: ^10} {: ^10} {: ^15} {: ^10}". format("|", line[0], "|", line[1], "|", line[2], "|"))
print ("{:-^80}".format("--------- END ---------"))