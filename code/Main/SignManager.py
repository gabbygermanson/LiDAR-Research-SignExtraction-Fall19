from Sign import *
import pandas as pd


class SignManager:
    """
    This class manages all the signs along with the algorithms to determine which clusters are signs. Each algo will
    take in a list of clusters and determine if a cluster is a sign. They will output a list of signs that will be held
    by a SignManager object.
    """
    def __init__(self):
        self.sign_list = list()


    # Add a sign to the sign manager's list
    def add_sign(self, sign: Sign):
        self.sign_list.append(sign)

# ======================================== Book keeping methods ====================================================================
    # This method creates a dataframe from the list of signs
    def convert_signlist_to_dataframe(self, sign_list):
        data = []
        for sign in sign_list:
            temp_list = []
            temp_list.append(sign_list.index(sign))  # Sign_ID - Do I need to make this a formal attribute?
            temp_list.append(sign.centroid_easting)  # centroid_easting
            temp_list.append(sign.centroid_northing)  # centroid_northing
            temp_list.append(sign.centroid_altitude)  # centroid_altitude
            temp_list.append(sign.avg_retro)  # avg_retro
            temp_list.append(sign.centroid_longitude)  # centroid_long
            temp_list.append(sign.centroid_latitude)  # centroid_lat
            temp_list.append(sign.num_of_points)  # num_of_points
            temp_list.append(sign.picture)  # pic_num

            data.append(temp_list)

        df = pd.DataFrame(data, columns=['Sign_Id', 'Easting', 'Northing', 'Altitude', 'Retro', 'Long', 'Lat', 'Num_of_Points', 'Pic_Num'])

        return df

    def make_sign_point_dataframe(self, sign_list):
        df = pd.DataFrame(columns = sign_list[0].dataframe.columns)
        for sign in sign_list:
            df = df.append(sign.dataframe)
        df.sort_values(by=['ID'])

        return df

# ==================================================================================================================================


# ============================================== Classifying Algoirhtms ============================================================

    """
    The num_points algo is very basic. If a cluster has more than 20 points, then it is classified as a sign.

    Inputs: A list of cluster objects
    Outputs: A list of sign objects
    """
    def num_points(self, cluster_list):
        sign_list = []
        # Loop through each cluster
        for cluster in cluster_list:
            if cluster.num_of_points >= 20:
                sign = Sign(cluster)
                sign_list.append(sign)
        return sign_list