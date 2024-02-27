"""
Maja Marem Jillzam B. Pagadora
BS Geodetic Engineering - 1st Year
2023-04953
"""

# Decimal Degrees to Degrees-Minutes-Seconds

dd_input = 118.42069

# DD-DMS Conversion
degrees = int(dd_input)

minutes = int((dd_input - degrees)*60)

seconds = round(((((dd_input - degrees)*60)-minutes)*60),2)

# DD-DMS Output
print("DMS: " + str(degrees) + "-" + str(minutes) + "-" + str(seconds))



# Degrees-Minutes-Seconds to Decimal Degrees

dms_input = "118-25-14.48"

# DMS-DD Conversion
values = dms_input.split("-")

degrees = int(values[0])
minutes = int(values[1])
seconds = float(values[2])

DD = round(degrees + (minutes/60) + (seconds/3600),6)

# DMS-DD Output
print("DD: " + str(DD))