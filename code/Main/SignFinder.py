from Cluster import *
from ClusterManager import *
from Sign import *
from SignManager import *
from Camera import *
from decimal import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import csv
import argparse
import math
import pandas as pd

"""
This is the test bed that we will use to test different algorithms.
The code is broken down into the following sections:

1. Command line arguements and initialization
    - This code allows this test bed to be run with different inputs and eventually with different algorithms. The idea is to be able to quickly
    swap between different cluster and classifying combinations in order to do quick analysis.
    - This is where all the files are read in and the data can be formatted (in our case, we round all x, y, and z to 3 decimal places. Yes this is slow. Hopefully we can make this round fn faster).

2. Algorithm Implementation - There are three parts to this part
    a) Filtering
    b) Clustering
    c) Classifying

    It is important to understand the purpose of each section AND it's inputs and outputs.

    Filtering
        - There are no inputs and outputs to filtering. We simply filter the dataframe by columns. We can filter by any column value.

    Clustering
        - The algorithms that are implemented in this section should be defined in the ClusterManager class.
        - Each clustering algorithm should take in a pandas dataframe and should return a list of clusters.
        - A cluster manager object will hold the list of clusters returned from the clustering algorithm. Look in the section below for details.

    Classifying
        - This section is to implement algorithms that will determine if a cluster is a sign and the sign's shape/classification.
        - The input for a classfying algorithm is a list of clusters and the output is a list of signs.
        - A sign manager object will hold the list of signs returned from the classifying algorithm. Look in the section below for details.

3. Book-keeping
    - We do other little things here like:
        - pair a picture to which sign we think it is
        - Writing results out to a file.

"""


# Rounding Function
def round_half_up(n, decimals=3):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier

if __name__ == '__main__':
    # # Command line arg code
    # parser = argparse.ArgumentParser(description='Finding Signs in LiDAR data!')
    # parser.add_argument("--i", help = "Input file.")
    # parser.add_argument("--o", help = "Output file")
    # input_file = args.i
    # output_file = args.o
    # if input_file is None:
    #     input_file = input("Enter input file: ")
    #
    # if output_file is None:
    #     output_file = input("Enter output file: ")

    # Global variables
    # cluster_list = []

    # Reading in data into a dataframe and formatting it.
    df = pd.read_csv('E:/School/VIP/Data/LiDAR_Data/original/XYZ/V_20180816_I285_EB_run1(0)_2nd_leg.txt', sep = " ")
    df = df.astype({'ID': int})
    # TODO: Figure out how to read in data with only a certain number of demicals. This takes a lot of time.
    df['Easting'] = df['Easting'].apply(round_half_up)
    df['Northing'] = df['Northing'].apply(round_half_up)
    df['Altitude'] = df['Altitude'].apply(round_half_up)
    df['Retro'] = df['Retro'].apply(round_half_up)

# Command line and initialization ^^^

# ========================================== Filtering ===============================================================
    # Filtering by Retro values
    df = df.loc[df['Retro'] > 0.7]
    df = df.reset_index(drop=True)
# ====================================================================================================================

# ========================================= Clustering ===============================================================
    cluster_manager = ClusterManager()
    cluster_manager.cluster_list = cluster_manager.progressive_kdmean(df)
# ====================================================================================================================

# ========================================== Classifying =============================================================
    sign_manager = SignManager()
    sign_manager.sign_list = sign_manager.num_points(cluster_manager.cluster_list)
# ====================================================================================================================

# Book keeping vvvv
# ========================================== Adding photos ===========================================================
    # Get the picture number that corresponds to each sign
    camera = Camera('E:/School/VIP/Data/LiDAR_Data/coords/coords.csv')
    for sign in sign_manager.sign_list:
        pic_num = camera.get_closest_pic(sign.centroid_longitude, sign.centroid_latitude)
        pic_num -= 2
        sign.add_pic(pic_num)
# ====================================================================================================================


# ======================================== Book keeping and output files =============================================
    sign_list_df = sign_manager.convert_signlist_to_dataframe(sign_manager.sign_list)
    sign_list_df.to_csv('sign_list_output.csv', index = False)

    points_of_signs = sign_manager.make_sign_point_dataframe(sign_manager.sign_list)
    points_of_signs.to_csv('points_of_signs.txt', sep = ' ', index = False)