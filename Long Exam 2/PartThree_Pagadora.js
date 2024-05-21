/*
The needed React Natives components would be 

View
- the most fundamental component for building UI
- Basically a Box
- this will contain the other components we need such as the text button tec
- container that supports layout of flexbox, style... more of Layout sya and how we will see things

Text
- label, display information/text
- both static and dynamic ung gagamitin static for the TITLE OF THE MAP and dynamic for output text

TextInput
- inputing text into the keyboard for the Azimuth Input

Button
- used to call the function that will convert the azimuth to DMS
- should render nicely on any platform

Style Sheet
- Design and Layout nung Magiging output naten

similar sa Machine Exercise 6 need ng 4 na main view boxes na mag cocontain different components
like one view for title, one for the input, one for the button, tas one den for output
although pwede ren naman na isa nalang medjo mas mahirap lang sya gawin
*/

function convertToBearing(AZS){
    /*
    convert the provided Azimuth from the South to it Bearing format

    Parameters: Azimuth from the South

    Output: Bearing
    */
    var elements = AZS.split("-")
    var D = elements[0]
    var M = elements[1]
    var S = elements[2]
    
    let DD = parseFloat(D) + parseFloat(M)/60 + parseFloat(S)/3600
    if (DD > 0 && DD < 90){
        let DDs = DD
        let degs = parseInt(DDs)
        let mins = parseInt((DDs - degs)*60)
        let secs = ((((DDs - degs)*60)-mins)*60).toFixed(0)
        let dms = String(degs) + "-" + String(mins) + "-" + String(secs)
        let bearing = "S " + dms + " W"
        return bearing
    }
    else if (DD > 90 && DD < 180){
        let DDs = 180 - DD
        let degs = parseInt(DDs)
        let mins = parseInt((DDs - degs)*60)
        let secs = ((((DDs - degs)*60)-mins)*60).toFixed(0)
        let dms = String(degs) + "-" + String(mins) + "-" + String(secs)
        let bearing = "N " + dms + " W"
        return bearing
    }
    else if (DD > 180 && DD < 270){
        let DDs = DD - 180
        let degs = parseInt(DDs)
        let mins = parseInt((DDs - degs)*60)
        let secs = ((((DDs - degs)*60)-mins)*60).toFixed(0)
        let dms = String(degs) + "-" + String(mins) + "-" + String(secs)
        let bearing = "N " + dms + " E"
        return bearing
    }
    else if (DD > 270 && DD < 360){
        let DDs = 360 - DD
        let degs = parseInt(DDs)
        let mins = parseInt((DDs - degs)*60)
        let secs = ((((DDs - degs)*60)-mins)*60).toFixed(0)
        let dms = String(degs) + "-" + String(mins) + "-" + String(secs)
        let bearing = "S " + dms + " E"
        return bearing
    }
    else if (DD == 0){
        let bearing = "DUE SOUTH"
        return bearing
    }
    else if (DD == 90){
        let bearing = "DUE WEST"
        return bearing
    }
    else if (DD == 180){
        let bearing = "DUE NORTH"
        return bearing
    }
    else if (DD == 270){
        let bearing = "DUE EAST"
        return bearing
    }
    else{
        let bearing = "UNKNOWN"
        return bearing
    }
    
}

let DMS = "115-02-03"
let bearing = convertToBearing(DMS)

console.log(bearing)