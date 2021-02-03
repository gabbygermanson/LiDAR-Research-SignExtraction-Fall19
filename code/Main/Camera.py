import csv
import pyproj
from decimal import *


class Camera:
    """
    The idea behind this class is to contain the pictures and to have a method to return a picture that is closest to
    a given coordinate. So if I think have a sign somewhere, then I can assign that picture to that sign. That way, I can
    check to see if that sign is a valid sign.


    """
    def __init__(self, file_name):
        self.file_name = file_name
        self.pic_dict = self.pic_coords(file_name)


    # This method reads in the data from coords.csv and puts data into a dictionary as {pic_num: (long, lat, alt)}
    def pic_coords(self, file_name):
        coords_file = open(file_name, 'r')
        reader = csv.reader(coords_file)
        pics_dict = {}
        row_num = 0
        for row in reader:
            if row_num != 0:
                pics_dict[int(row[1])] = (row[2], row[3], row[4])
            row_num += 1

        coords_file.close()

        return pics_dict

    """
    This method returns the picture number corresponding to the closest picture to the input long & lat coordinates

    Inputs: Long and Lat measurements in degrees
    Outputs: A number that corresponds to the file name of the picture that shows the sign.
    """
    def get_closest_pic(self, long, lat):
        distance = float("inf")
        pic_num = -1
        geod = pyproj.Geod(ellps='WGS84')

        for i in range(len(self.pic_dict)):
            pic_long = Decimal(self.pic_dict[i][0])
            pic_lat = Decimal(self.pic_dict[i][1])
            temp = geod.inv(long, lat, pic_long, pic_lat)
            if temp[2] < distance:
                distance = temp[2]
                pic_num = i

        return pic_num
