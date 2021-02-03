import utm as UTM

f = open("V_20180816_I285_EB_run1(0)_2nd_leg.csv", "r")
f.readline()

newf = open("UTMpython.csv","w")
newf.write("ID,Easting,Northing,Retro,Angle,UTC,X,Y,Z,Distance\n");

for line in f:
    lineData = line.split(",")
    conversion = (UTM.from_latlon(float(lineData[2]), float(lineData[1])))

    newf.write(lineData[0])
    newf.write(",")

    newf.write(str(conversion[0]))
    newf.write(",")
    newf.write(str(conversion[1]))
    newf.write(",")

    newf.write(lineData[6])
    newf.write(",")
    newf.write(lineData[4])
    newf.write(",")
    newf.write(lineData[7].strip())
    newf.write(",")
    newf.write(lineData[1])
    newf.write(",")
    newf.write(lineData[2])
    newf.write(",")
    newf.write(lineData[3])
    newf.write(",")
    newf.write(lineData[5])
    newf.write("\n")


newf.close()
f.close()