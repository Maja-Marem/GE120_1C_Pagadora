/* 
Exercise 3
Maja Marem Jillzam B. Pagadora
2023-04953
BS Geodetic Engineering
*/

 // constants  "set variables as initial quantity in loop"
 var data = [
     [13.23, 124.795], 
     [15.57, 14.143], 
     [43.36, 270.000], 
     [23.09, 188.169], 
     [10.99, 180.000], 
     [41.40, 50.562], 
 ]
 var Dis = 0
 var LatSum = 0
 var DepSum = 0
 
  // lists used  "Storage Data Base"
 var lines = []
 var LotDesc = []


 // Imports "Relevant functions outside python"
 const { abs, floor, cos, sin, atan, sqrt, pow } = Math
 const radians = Math.PI/180
 const degrees = 180/Math.PI

 // Functions  "Set Functions catered to the Machine Exercise"
function getLatitude(distance, azs){
    /*
    Calculates the Latitude of the line using the set parameters

    The product of negative distance and cos azimuth from the
    south in radians

    Parameters: distance, azimuth
    */
    let latitude = (- distance*cos(radians*azs))
    return latitude
}
function getDeparture(distance, azs){
    /*
    Calculates the Departure of the line using the set parameters

    The product of negative distance and sin azimuth from the
    south in radians

    Parameters: distance, azimuth
    */
    let departure = (- distance*sin(radians*azs))
    return departure 
}
function azimuthToBearing(azs){
    /*
    Converts Azimuth from the South to Bearing

    Given Azimuth in DD - calculate bearing based on: if elif else conditions

    Parameters: azimuth
    */
    if (azs == 0){
        let bearing = "Due South"
        return bearing
    }
    else if (azs > 0 && azs < 90){
        let az = azs
        let degs = parseInt(az)
        let mins = parseInt((az - degs)*60)
        let secs = ((((az - degs)*60)-mins)*60).toFixed(2)
        let dms = degs + "-" + mins + "-" + secs
        let bearing = "S" + dms + "W"
        return bearing
    }
    else if (azs == 90){
        let bearing = "Due West"
        return bearing
    }
    else if (azs > 90 && azs < 180){
        let az = 180 - azs
        let degs = parseInt(az)
        let mins = parseInt((az - degs)*60)
        let secs = ((((az - degs)*60)-mins)*60).toFixed(2)
        let dms = degs + "-" + mins + "-" + secs
        let bearing = "N" + dms + "W"
        return bearing
    }
    else if (azs == 180){
        let bearing = "Due North"
        return bearing
    }
    else if (azs > 180 && azs < 270){
        let az = azs - 180
        let degs = parseInt(az)
        let mins = parseInt((az - degs)*60)
        let secs = ((((az - degs)*60)-mins)*60).toFixed(2)
        let dms = degs + "-" + mins + "-" + secs
        let bearing = "N" + dms + "E"
        return bearing
    }  
    else if (azs == 270){
        let bearing = "Due East"
        return bearing
    }
    else if (azs > 270 && azs < 360){
        let az = 360 - azs
        let degs = parseInt(az)
        let mins = parseInt((az - degs)*60)
        let secs = ((((az - degs)*60)-mins)*60).toFixed(2)
        let dms = degs + "-" + mins + "-" + secs
        let bearing = "S" + dms + "E"
        return bearing
    }
    else {
        let bearing = "unknown"
        return bearing
    }
}
function AdjDist(distance, azs, Dis, LatSum, DepSum){
    /*
    Calculates the addjusted distance 

    parameters: distance, azs, dis, latsum, depSum
    */
    let lat = - distance*cos(radians*azs)
    let dep = - distance*sin(radians*azs)
    let corrLat = -(distance/Dis)*LatSum
    let AdjLat = corrLat + lat
    let corrDep = -(distance/Dis)*DepSum
    let AdjDep = corrDep + dep
    let Dist_new = sqrt((pow(AdjLat,2)) + (pow(AdjDep,2))).toFixed(3)
    return Dist_new
}
function AdjBearing(distance, azs){
    /*
    Calculates the adjusted Line distance
    
    parameters; distance, azs
    */
    let L = - distance*cos(radians*azs)
    let D = - distance*sin(radians*azs)
    if (L> 0 && D > 0) {
        let Dg = degrees*atan(abs(D/L))
        let deg = parseInt(Dg)
        let min = parseInt((Dg - deg)*60)
        let sec = ((((Dg - deg)*60)-min)*60).toFixed(2)
        let b = deg + "-" + min + "-" + sec
        let NB = "N " + b + " E"
        return NB
    }
    else if (L > 0 && D < 0) {
        let Dg = degrees*atan(abs(D/L))
        let deg = parseInt(Dg)
        let min = parseInt((Dg - deg)*60)
        let sec = ((((Dg - deg)*60)-min)*60).toFixed(2)
        let b = deg + "-" + min + "-" + sec
        let NB = "N " + b + " W"
        return NB
    }
    else if (L < 0 && D < 0){
        let Dg = degrees*atan(abs(D/L))
        let deg = parseInt(Dg)
        let min = parseInt((Dg - deg)*60)
        let sec = ((((Dg - deg)*60)-min)*60).toFixed(2)
        let b = deg + "-" + min + "-" + sec
        let NB = "S " + b + " W"
        return NB
    }
    else if (L < 0 && D > 0){
        let Dg = degrees*atan(abs(D/L))
        let deg = parseInt(Dg)
        let min = parseInt((Dg - deg)*60)
        let sec = ((((Dg - deg)*60)-min)*60).toFixed(2)
        let b = deg + "-" + min + "-" + sec
        let NB = "S " + b + " E"
        return NB
    }
    else if (L== 0 && D > 0){
        let NB = "Due East"
        return NB
    }
    else if (L == 0  && D < 0){
        let NB = "Due West"
        return NB
    }
    else if (L > 0 && D == 0){
        let NB = "Due North"
        return NB
    }
    else if (L < 0 && D== 0) {
       let NB = "Due South"
       return NB
    }
    else{
        let NB = "unknown"
        return NB
    }
}

 // title of the Activity
console.log()
console.log()
console.log("MACHINE EXERCISE 5: Balancing the Survey using JAVA SCRIPT",  ) 

for (let i = 0; i < data.length; i++) {
// LINE DESCRIPTION - APPENDED LINES
     let line = data[i]
     let distance = line[0]
     let azimuth = line[1]

     let bearing = azimuthToBearing(azimuth)
     let latitude = getLatitude(distance, azimuth)
     let departure = getDeparture(distance, azimuth)

     Dis += distance
     LatSum += latitude
     DepSum += departure 

     lines.push([(i+1), distance, bearing, latitude, departure])
}

// Calculating the LEC and REC
let LEC = sqrt((pow(LatSum, 2)) + (pow(DepSum,2)))
let REC = floor((abs(Dis/LEC))/100)*100

for (let i = 0; i < data.length; i++) {
// gathering data for new/adjusted lot description
    let line = data[i]
    let distance = line[0]
    let azimuth = line[1]
    
    NewDist = AdjDist(distance, azimuth, Dis, LatSum, DepSum)
    NewBearing = AdjBearing(distance, azimuth)
    LDes = ([(i+1), NewDist, NewBearing])
    LotDesc.push(LDes) 
}

// print output/final output

console.log()
console.log("---------------------------------------------------------------------------------------")
console.log("|".padEnd(5), "LINE".padEnd(6), "|".padEnd(5), "DISTANCE".padEnd(10), "|".padEnd(5), "BEARING".padEnd(15), "|".padEnd(5), "Latitude".padEnd(10), "|".padEnd(5), "Departure".padEnd(10), "|".padEnd(5))
console.log("---------------------------------------------------------------------------------------")
for (var line of lines){
    console.log("|".padEnd(5),String(line[0]).padEnd(6), "|".padEnd(5), String(line[1]).padEnd(10), "|".padEnd(5), String(line[2]).padEnd(15), "|".padEnd(5), String(line[3].toFixed(3)).padEnd(10), "|".padEnd(5), String(line[4].toFixed(3)).padEnd(10), "|".padEnd(5))
}
console.log("---------------------------------------------------------------------------------------")

console.log()
console.log("LEC: " + LEC)
console.log("REC : 1:" + REC)

console.log()
console.log("ADJUSTED LOT DESCRIPTION")
console.log("--------------------------------------------------------")
console.log("|".padEnd(5), "LINE".padEnd(6), "|".padEnd(5), "DISTANCE".padEnd(10), "|".padEnd(5), "BEARING".padEnd(18), "|".padEnd(5))
console.log("--------------------------------------------------------")
for (var LDes of LotDesc){
    console.log("|".padEnd(5),String(LDes[0]).padEnd(6), "|".padEnd(5), String(LDes[1]).padEnd(10), "|".padEnd(5), String(LDes[2]).padEnd(18), "|".padEnd(5))
}
console.log("--------------------------------------------------------")