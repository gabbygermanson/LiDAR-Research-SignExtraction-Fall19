from decimal import *
from ClusterManager import *
from Cluster import *
from Camera import *
from Sign import *
import pyproj
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import csv
import math

# Rounding Function
def round_half_up(n, decimals=3):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier

if __name__ == '__main__':
    # Reading in data into a dataframe and formatting it.
    df = pd.read_csv('E:/School/VIP/Data/LiDAR_Data/original/XYZ/V_20180816_I285_EB_run1(0)_2nd_leg.txt', sep=" ")
    df = df.astype({'ID': int})
    # TODO: Figure out how to read in data with only a certain number of demicals. This takes a lot of time.
    df['Easting'] = df['Easting'].apply(round_half_up)
    df['Northing'] = df['Northing'].apply(round_half_up)
    df['Altitude'] = df['Altitude'].apply(round_half_up)
    df['Retro'] = df['Retro'].apply(round_half_up)

    # ========================================== Filtering ===============================================================
    # Filtering by Retro values
    df = df.loc[df['Retro'] > 0.7]
    df = df.reset_index(drop=True)
    # ====================================================================================================================
    cluster_manager = ClusterManager()
    cluster_manager.cluster_list, empty_list_count, found_cluster_count, no_found_cluster_count = cluster_manager.progressive_kdmean(df)
    # print(len(cluster_manager.cluster_list))
    # print("Clusters created from an empty list: {} \nPoints inserted into a cluster: {} \nClusters created because no cluster was found: {}".format(empty_list_count, found_cluster_count, no_found_cluster_count))


