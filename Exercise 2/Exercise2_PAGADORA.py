"""
Exercise 1
Maja Marem Jillzam B. Pagadora
2023-04953
BS Geodetic Engineering
"""

# LINE DESCRIPTION

Start = 1
End = 2
lines=[]

while True:
    print()
    print("LINE " + str(Start) + "-" + str(End))
    dist = (input("Enter Line Distance: "))
    azs = float(input("Enter Azimuth from the South: ")) % 360

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


    line = ("LINE " + str(Start) + "-" + str(End) , dist, bearing)
    lines.append(line)
    
    YN = (input("Add a new line? "))
    if YN == "yes" or YN.lower == "y":
        Start = Start + 1
        End = End + 1
        continue
    else:
        break

print ("{:-^80}".format("-----------------------"))
print ("{: ^10} {: ^10} {: ^10} {: ^10} {: ^10} {: ^15} {: ^10}". format("|", "LINE" , "|", "DISTANCE", "|", "BEARING", "|"))
for line in lines:
    print ("{: ^10} {: ^10} {: ^10} {: ^10} {: ^10} {: ^15} {: ^10}". format("|", line[0], "|", line[1], "|", line[2], "|"))
print ("{:-^80}".format("----------END----------"))