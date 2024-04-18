/* 
Exercise 3
Maja Marem Jillzam B. Pagadora
2023-04953
BS Geodetic Engineering
*/

 // class  "spcified classifications for console.log"

 // constants  "set variables as initial quantity in loop"

var Start = 1
var End = 2
var data = [
    [13.23, 124.795], 
    [15.57, 14.143], 
    [43.36, 270.000], 
    [23.09, 188.169], 
    [10.99, 180.000], 
    [41.40, 50.562], 
]
var lines = []
var Dis = 0
var LatSum = 0
var DepSum = 0

 // lists used  "Storage Data Base"

lines = []
clat = []
cdep = []
ADJLat = []
ADJDep = []
corrs = []
ADJDis = []
ADJb = []
LotDesc = []

 // Imports "Relevant functions outside python"
from math import cos, sin, atan, radians, degrees, sqrt

 // Functions - MAIN CODE
"Set Functions catered to the Machine Exercise"


function getLatitude(distance, azs){
    /*
    Calculates the Latitude of the line using the set parameters

    The product of negative distance and cos azimuth from the
    south in radians

    Parameters: distance, azimuth
    */
    return (- distance*cos(radians(azs)))
}

function getDeparture(distance, azs){
    /*
    Calculates the Departure of the line using the set parameters

    The product of negative distance and sin azimuth from the
    south in radians

    Parameters: distance, azimuth
    */
    return (departure = - distance*sin(radians(azs)))
    
}
function azimuthToBearing(azs){
    /*
    Converts Azimuth from the South to Bearing

    Given Azimuth in DD - calculate bearing based on: if elif else conditions

    Parameters: azimuth
    */
    if (azs == 0){
        return ("Due South".toString)
    }
    else if (azs > 0 && azs < 90){
        az = azs
        degs = int(az)
        mins = int((az - degs)*60)
        secs = round(((((az - degs)*60)-mins)*60),2)
        dms = str(degs) + "-" + str(mins) + "-" + str(secs)
        return ("S".toString + "dms".toString + "W".toString)
    }
    else if (azs == 90){
        return ("Due West".toString)
    }
    else if (azs > 90 && azs < 180){
        az = 180 - azs
        degs = int(az)
        mins = int((az - degs)*60)
        secs = round(((((az - degs)*60)-mins)*60),2)
        dms = str(degs) + "-" + str(mins) + "-" + str(secs)
        bearing = "N " + str(dms) + " W"
    }
        
    else if azs == 180:
        bearing = "Due North"
    else if azs > 180 and azs < 270:
        az = azs - 180
        degs = int(az)
        mins = int((az - degs)*60)
        secs = round(((((az - degs)*60)-mins)*60),2)
        dms = str(degs) + "-" + str(mins) + "-" + str(secs)
        bearing = "N " + str(dms) + " E"
    else if azs == 270:
        bearing = "Due East"
    else:
        az = 360 - azs
        degs = int(az)
        mins = int((az - degs)*60)
        secs = round(((((az - degs)*60)-mins)*60),2)
        dms = str(degs) + "-" + str(mins) + "-" + str(secs)
        bearing = "S " + str(dms) + " E"
    return bearing
}
function getclat(d, Dis, lat):
    'Calculates the Correction in Latitude of each line of the traverse'
    corL = -(d/Dis)*lat
    return corL

function getcdep(d, Dis, dep):
    'Calculates the Correction in Departure of a line of the traverse'
    corD = -(d/Dis)*dep
    return corD

function BalL(Lat, corL):
    'Balances the Latitudes to get the Adjusted Lat-Values'
    AdjL = corL + Lat
    return AdjL

function BalD(Dep, corD):
    'Balances the Departure to get the Adjusted Dep-Values'
    AdjD = Dep + corD
    return AdjD

function AdjDist(LAT, DEP):
    'Calculates the adjusted Line distance'
    distan = sqrt((pow(LAT,2)) + (pow(DEP,2)))
    return distan

function AdjBearing(L, D):
    'Calculates the adjusted Line distance'
    if L> 0 and D > 0:
        Dg = degrees(atan(abs(D/L)))
        deg = int(Dg)
        min = int((Dg - deg)*60)
        sec = round(((((Dg - deg)*60)-min)*60),2)
        b = str(deg) + "-" + str(min) + "-" + str(sec)
        NB = "N " + str(b) + " E"
    else if L > 0 and D < 0:
        Dg = degrees(atan(abs(D/L)))
        deg = int(Dg)
        min = int((Dg - deg)*60)
        sec = round(((((Dg - deg)*60)-min)*60),2)
        b = str(deg) + "-" + str(min) + "-" + str(sec)
        NB = "N " + str(b) + " W"
    else if L < 0 and D < 0:
        Dg = degrees(atan(abs(D/L)))
        deg = int(Dg)
        min = int((Dg - deg)*60)
        sec = round(((((Dg - deg)*60)-min)*60),2)
        b = str(deg) + "-" + str(min) + "-" + str(sec)
        NB = "S " + str(b) + " W"
    else if L < 0 and D > 0:
        Dg = degrees(atan(abs(D/L)))
        deg = int(Dg)
        min = int((Dg - deg)*60)
        sec = round(((((Dg - deg)*60)-min)*60),2)
        b = str(deg) + "-" + str(min) + "-" + str(sec)
        NB = "S " + str(b) + " E"
    else if L== 0 and D > 0:
        NB = "Due East"
    else if L == 0 and D < 0:
        NB = "Due West"
    else if L > 0 and D == 0:
        NB = "Due North"
    else:
        NB = "Due South"
    return NB

 // title of the Activity
print()
print("MACHINE EXERCISE 3: Balancing the Survey",  ) 

 // MAIN LOOP "Flow / Scheme of the Code"
while True:

 // Line Description  
    'line from Point to Point, Distance, Azimuth/Bearing'
    print()
    console.log("LINE " + str(Start) + "-" + str(End), console.log)

    dist =(float(input("Enter Line Distance: ")))
    azs = input("Enter Azimuth from the South: ")

    if "-" in azs:
        degrs, minutes, seconds = azs.split("-")
        azs = (int(degrs) + (int(minutes)/60) + (float(seconds)/3600)) % 360
    else:
        azs = float(azs) % 360

 // LatDep Bearing
    'Calculating the Latitude, Departure and Bearing using set functions'
    B = azimuthToBearing(azs)
    lat = getLatitude(dist, azs)
    dep = getDeparture (dist, azs)

 // line lists - preBalancing lot description 
    'listing / storing line descriptions'
    line = [str(Start) + "-" + str(End) , dist, B, lat, dep]
    lines.append(line)

 // Continuation / End of Loop 'the loop shall continue if:..., else: break'
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
     // Calculate LEC and REC
        for line in lines:
            Dis += line[1]

        for line in lines:
            LatSum += line[3]

        for line in lines:
            DepSum += line[4]

        LEC = sqrt((pow(LatSum, 2)) + (pow(DepSum,2)))
        REC = round((abs(Dis/LEC)), -2)

     // Calculate Corrections
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

     // Adjusted Lot Description
        for i in range(len(ADJLat)) and range(len(ADJDep)):
            Adj_distance = AdjDist(ADJLat[i], ADJDep[i])
            ADJDis.append(Adj_distance)
        
            Adj_bear = AdjBearing(ADJLat[i], ADJDep[i])
            ADJb.append(Adj_bear)

        for i in range(len(ADJLat)) and range(len(ADJDep)) and range(len(lines)):
            Lot_Description = (lines[i][0], ADJDis[i], ADJb[i])
            LotDesc.append(Lot_Description)

        break

 // PRINT Line Description Table
console.log ("{:-^88}".format("-----------------------"),  )

console.log (("{: ^5} {: ^6} {: ^5} {: ^7} {: ^5} {: ^15} {: ^5} {: ^10} {: ^5} {: ^10} {: ^5} ". format(" ", "LINE", " ", "DISTANCE", " ", "BEARING", " ", "Latitude", " ", "Departure", " ", "cLat", " ", "cDep", " ")), )

print ("{:-^88}".format("-----------------------"))

for line in lines:
    print ("{: ^5} {: ^6} {: ^5} {: ^7} {: ^5} {: ^15} {: ^5} {: ^10} {: ^5} {: ^10} {: ^5}". format("|", line[0], "|", round(line[1],3), "|", line[2],"|", round(line[3],3), "|", round(line[4],3), "|"))

console.log ("{:-^88}".format("-----------------------"),  )
print()

 // CORRECTIONS and Adjuseted Lat-Dep TABLE
console.log ("{:-^92}".format("-----------------------"),  )

console.log(("{: ^5} {: ^10} {: ^5} {: ^10} {: ^5} {: ^10} {: ^5} {: ^10} {: ^5} {: ^10} {: ^5}". format(" ", "LINE", " ", "cLat", " ", "cDep", " ", "Adj Lat", " ", "Adj Dep", " ")),  )
print ("{:-^92}".format("-----------------------"))

for corr in corrs:
    print("{: ^5} {: ^10} {: ^5} {: ^10} {: ^5} {: ^10} {: ^5} {: ^10} {: ^5} {: ^10} {: ^5}". format("|", corr[0], "|", round(corr[1],5), "|", round(corr[2],5), "|", round(corr[3],3), "|", round(corr[4],3), "|"))

console.log ("{:-^92}".format("-----------------------"),  )
print()

 // PRINT the Linear Error of Closure and REC
console.log("LEC: ",  )
console.log(str(LEC),  )
console.log("REC: " ,  )
console.log("1 : " + str(REC),  )
print()

 // LOT DESCRIPTION TABLE - FINAL OUTPUT
console.log ("{:-^77}".format("-----------------------"),  )

console.log(("{: ^5} {: ^15} {: ^5} {: ^15} {: ^5} {: ^20} {: ^5}". format(" ", "LINE", " ", "DISTANCE", " ", "BEARING", " ")),  )
print ("{:-^77}".format("-----------------------"))
for Lot_Description in LotDesc:
    print("{: ^5} {: ^15} {: ^5} {: ^15} {: ^5} {: ^20} {: ^5}". format("|", Lot_Description[0], "|", round(Lot_Description[1],3), "|", Lot_Description[2], "|"))

console.log ("{:-^77}".format("-----------------------"),  )
print()

console.log ("{: ^77}".format("~ END ~"),  )