"""
Exercise 1
Maja Marem Jillzam B. Pagadora
2023-04953
BS Geodetic Engineering
"""

print("Kindly follow the indicated format for each inputs.")

print("")

# Decimal Degrees to Degrees-Minutes-Seconds
print("DD-DMS Conversion")

print("")

# DD-DMS Input
dd_input = float(input("Input DDD.dddddd: "))

# DD-DMS Conversion
degrees = int(dd_input)

minutes = int((dd_input - degrees)*60)

seconds = round(((((dd_input - degrees)*60)-minutes)*60),2)

# DD-DMS Output
print("DMS: " + str(degrees) + "-" + str(minutes) + "-" + str(seconds))

print("")

# Degrees-Minutes-Seconds to Decimal Degrees
print("DMS-DD Conversion")

print("")

# DMS-DD Input
dms_input = (input("Input DDD"+"-"+"MM"+"-"+"SS.ss: "))

# DMS-DD Conversion
values = dms_input.split("-")

degrees = int(values[0])
minutes = int(values[1])
seconds = float(values[2])

DD = round(degrees + (minutes/60) + (seconds/3600),6)

# DMS-DD Output
print("DD: " + str(DD))