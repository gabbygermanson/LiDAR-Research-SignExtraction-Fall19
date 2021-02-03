from Cluster import *
import pandas as pd

class ClusterManager:
    """
    This class manages all the clusters along with the algorithms to determine clusters. 
    Each clustering algo will take in a dataframe, which is the main dataframe with the results from the filtering section.
    Each clustering algo will output a list of signs that will be held by a SignManager object.
    """

    # Initilization
    def __init__(self):
        self.cluster_list = list()













# =================================================== Clustering Algorithms ======================================================================================
    """
    progressive_kdmean is a centroid based algorithm. It will take in the whole dataframe and go point by point. If there is a cluster whose centroid is within
    a certain distance away (threshold), then it adds it to the cluster. If no cluster exists, then it creates a new cluster and adds the points to the new cluster.
    The threshold is set a 1 meter, as I figured most signs are around about a meter or so wide.

    This method works fairly well if we are able to filter out points that probably don't belong to a sign.

    The columns for the pandas dataframe are as follows:

    ID, Easting, Northing, Altitude, Retro, Angle, Distance, UTC, Long, Lat, Pic

    Input: pandas dataframe
    Output: list of clusters 
    """
    def progressive_kdmean(self, df):
        easting_tolerance = 1.0
        northing_tolerance = 1.0
        alt_tolerance = 1.0
        retro_tolerance = 0.5

        cluster_list = []

        for index, row in df.iterrows():
            if cluster_list == []:
                c_df = pd.DataFrame(columns = df.columns)
                c = Cluster(c_df)
                c.add_point(row)
                cluster_list.append(c)
            else:
                # see if it falls within a certain range
                count = 0
                inserted = False

                while not inserted and count < len(cluster_list):
                    c = cluster_list[count] #c is a cluster

                    easting_lower_bound = c.centroid_easting - easting_tolerance
                    easting_upper_bound = c.centroid_easting + easting_tolerance
                    northing_lower_bound = c.centroid_northing - northing_tolerance
                    northing_upper_bound = c.centroid_northing + northing_tolerance
                    alt_lower_bound = c.centroid_altitude - alt_tolerance
                    alt_upper_bound = c.centroid_altitude + alt_tolerance
                    retro_lower_bound = c.avg_retro - retro_tolerance
                    retro_upper_bound = c.avg_retro + retro_tolerance

                    if easting_lower_bound <= row['Easting'] <= easting_upper_bound and northing_lower_bound <= row['Northing'] <= northing_upper_bound and \
                            alt_lower_bound <= row['Altitude'] <= alt_upper_bound and retro_lower_bound <= row['Retro'] <= retro_upper_bound:

                        c.add_point(row)
                        inserted = True
                    else:
                        count += 1

                if not inserted:
                    c_df = pd.DataFrame(columns=df.columns)
                    c = Cluster(c_df)
                    c.add_point(row)
                    cluster_list.append(c)

        return cluster_list
