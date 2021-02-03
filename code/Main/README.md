# VIP_LiDAR
The purpose of this project is to identify, classify, and analyze road signs using LiDAR data. Our team has collected data from multiple interstates in Georgia, USA. The data includes LiDAR scans along with pictures. Surely many goals can be achieved with this data, but the end goal is to be able to find road signs in the LiDAR data in order to analyze the deterioation rates of the signs and provide an accruate failure prediction.

# Code Organization and Flow
There are several files in the repo and can be confusing when sifting through everything. Short explanations will be given here:

### Important Files:
- SignFinder.py
  - This is a test bed where we implement different types of filtering, clustering, and classifying algorithms. The idea is to keep all the book keeping (reading in, formatting, and exporting data, pairing pictures, etc) standardized while allowing us to swap out different combinations of algorithms. In other words, SignFinder streamlines algorithm testing.
- Cluster.py
  - This class contains the code to create cluster objects, which are essentially groupings of points that correspond to entities in the real world (sign, car, rock, etc.). Each cluster maintains the points that belong to it in a dataframe. It also maintains a centroid of it's positional data.
- Sign.py
  - This class contains the code to create sign objects, which are clusters that have been analyzed and determined to be signs. They also contain the points (stored in a dataframe) that belong to a sign. It also maintains centroids of positional data along with a picture number that corresponds to the picture frame that portrays the sign in real life.
- ClusterManager.py
  - This class manages the list of clusters that we get from our clustering algorithms. The clustering algorithms are stored in this class. NOTE: Each clustering algorithm should have a dataframe as input and should output a list of clusters. 
- Signmanager.py
  - This class manages the list of signs that we get from our classifying algorithms. The classifying algorithms are stored in this class. NOTE: Each classifying algorithm should have a dataframe as input and should output a list of signs.
  
### Less Important Files:
- Camera.py
  - This class manages the pictures that we pair with a sign.
- testing.py
  - Used to try out code quickly that would be more challenging in the python terminal.
  
### Unused Files:
- Picture.py
- SignVisualizer.py
- boom.py
  - This was the old implmentation of this project.
  
## Flow
The main flow of the program is as follows:
1. Read in the LiDAR data into a pandas dataframe
2. Filter the data to get rid of bad or unecessary data
3. Pass the filtered dataframe into a clustering algorithm that turns a list of clusters.
4. Pass the list of clusters into a classifying algorithm that will determine which clusters are signs. Returns a list of signs.
5. We will pair a picture to each sign that shows the sign in the real world.
6. Write out the list of points to a .txt file
7. Write out the list of signs that we found to a .csv file.

# Running the Program
The command line arguments are quite working yet, so in order to run the program:
1. Open up SignFinder.py
2. Where the original data is read into a pandas dataframe (line 73) input the full path of the original data.
3. Where we get the picture numbers from coords.csv (line 102) input the full path to coords.csv
4. Open up cmd/terminal/bash and run the python file SignFinder.py
