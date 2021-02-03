from decimal import Decimal
import pandas as pd

"""
The cluster class is essentially a grouping of points that should represent an object in the real world.
Each cluster contains the points that belong to that cluster in a pandas dataframe
The centroid of the cluster is also maintained along with the average retro intensity value and the number of points in the cluster.
"""



class Cluster:

    # cluster
    def __init__(self, df):
        self.dataframe = df

        # If the df is empty, then initialize all values to 0. Otherwise, calculate the attributes
        if self.dataframe.empty:
            self.centroid_easting = 0.0
            self.centroid_northing = 0.0
            self.centroid_altitude = 0.0
            self.avg_retro = 0.0
            self.centroid_longitude = 0.0
            self.centroid_latitude = 0.0
            self.num_of_points = 0
        else:
            self.centroid_easting = self.dataframe['Easting'].mean()
            self.centroid_northing = self.dataframe['Northing'].mean()
            self.centroid_altitude = self.dataframe['Altitude'].mean()
            self.avg_retro = self.dataframe['Retro'].mean()
            self.centroid_longitude = self.dataframe['Long'].mean()
            self.centroid_latitude = self.dataframe['Lat'].mean()
            self.num_of_points = len(self.dataframe.index)



    """
    This function adds a point to the point list. 

    Input: A row from a Dataframe, which is a Series object
    Output: None
    """
    def add_point(self, row):
        # Add row to Cluster df and increment num_of_points
        self.dataframe = self.dataframe.append(row, ignore_index = True)
        self.num_of_points += 1

        # Calculate new centroid of cluster
        self.centroid_easting, self.centroid_northing, self.centroid_altitude, self.centroid_longitude, self.centroid_latitude  = self.centroid()

        # Calculate the new average retro value
        self.avg_retro = self.dataframe['Retro'].mean()


    """
    This function calculates the centroid of the cluster. This could be improved by using the median of a data set
    instead of the average
    """
    def centroid(self):
        centroid_easting = self.dataframe['Easting'].mean()
        centroid_northing = self.dataframe['Northing'].mean()
        centroid_altitude = self.dataframe['Altitude'].mean()
        centroid_longitude = self.dataframe['Long'].mean()
        centroid_latitude = self.dataframe['Lat'].mean()

        return centroid_easting, centroid_northing, centroid_altitude, centroid_longitude, centroid_latitude

