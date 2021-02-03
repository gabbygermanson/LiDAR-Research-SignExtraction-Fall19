from ClusterManager import *
from Cluster import *
import pandas as pd

class Sign:
    """
    This class will hold the points associated to that sign along with a picture id. Now I'm thinking I will just pass
    over the clusters and their data.
    """
    def __init__(self, cluster: Cluster):
        self.dataframe = cluster.dataframe
        self.centroid_easting = cluster.centroid_easting
        self.centroid_northing = cluster.centroid_northing
        self.centroid_altitude = cluster.centroid_altitude
        self.avg_retro = cluster.avg_retro
        self.centroid_longitude = cluster.centroid_longitude
        self.centroid_latitude = cluster.centroid_latitude
        self.num_of_points = cluster.num_of_points

        # Assign a picture to the sign here.
        self.picture = -1

    # This function adds a point to the dataframe. Input is a row from a Dataframe, which is a series object
    def add_point(self, row):
        # Add row to Cluster df and increment num_of_points
        self.dataframe.append(row, ignore_index = True)
        self.num_of_points += 1

        # Calculate new centroid of cluster
        self. centroid_easting, self.centroid_northing, self.centroid_altitude, self.centroid_longitude, self.centroid_latitude,  = self.centroid()

        # Calculate the new average retro value
        self.dataframe['Retro'].mean()


    # This function calculates the centroid of the cluster. This could be improved by using the median of a data set
    # instead of the average
    def centroid(self):
        centroid_easting = self.dataframe['Easting'].mean()
        centroid_northing = self.dataframe['Northing'].mean()
        centroid_altitude = self.dataframe['Altitude'].mean()
        centroid_longitude = self.dataframe['Long'].mean()
        centroid_latitude = self.dataframe['Lat'].mean()

        return centroid_easting, centroid_northing, centroid_altitude, centroid_longitude, centroid_latitude


    # This method adds a pic num to the sign attribute as well with creating a new column in the dataframe to house the pic_num
    def add_pic(self, pic_num):
        self.picture = pic_num
        self.dataframe['Pic'] = pic_num

