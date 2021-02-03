import utm as UTM
import math

def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier


if __name__ == "__main__":
    f = open("E:/School/VIP/Data/LiDAR_Data/original/CSV/V_20180816_I285_EB_run1(0)_2nd_leg.csv", "r")
    f.readline()

    newf = open("E:/School/VIP/Data/LiDAR_Data/output/UTMpython.txt","w")
    newf.write("ID Easting Northing Altitude Retro Angle Distance UTC Long Lat\n");

    for line in f:
        lineData = line.split(",")
        conversion = (UTM.from_latlon(float(lineData[2]), float(lineData[1])))
        # Conversion's x and y coordinates are float values
        delimiter = " "

        # For saving as a txt file
        # Write ID
        newf.write(lineData[0])
        newf.write(delimiter)

        # Write Easting
        newf.write(str(round_half_up(conversion[0], 3)))
        newf.write(delimiter)
        # Write Northing
        newf.write(str(round_half_up(conversion[1], 3)))
        newf.write(delimiter)

        # Write Altitude
        newf.write(str(round_half_up(float(lineData[3]), 3)))
        newf.write(delimiter)

        # Write Retro
        newf.write(lineData[6])
        newf.write(delimiter)

        # Write Angle
        newf.write(lineData[4])
        newf.write(delimiter)

        # Write Distance
        newf.write(lineData[5])
        newf.write(delimiter)

        # Write UTC
        newf.write(lineData[7].strip())
        newf.write(delimiter)

        # Write Long
        newf.write(lineData[1])
        newf.write(delimiter)

        # Write Lat
        newf.write(lineData[2])
        newf.write("\n")

    newf.close()
    f.close()


