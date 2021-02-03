# Source Code Explanation

# GPS-UTM Folder
- Contains Java and Python implementations to convert GPS longitude and latitude data to UTM coordinates
- Sample input and output data is accessible via this OneDrive link: 
https://gtvault-my.sharepoint.com/:f:/g/personal/ggermanson3_gatech_edu/EiUZGmGiMVdFjnc1EEF9mTgBdDSXNDs7X-igui8owcejUQ?e=7J8B7u
	Within Python folder of OneDrive: (More accurate and actually implemented)
	- V_20180816_I285_EB_run1(0)_2nd_leg.csv is portion of road GPS sample input
	- UTMpython.csv is receptive output data
	- Requires download of utm package from: https://pypi.org/project/utm/
		- Install in the terminal by typing 'pip install utm'
		- I was using python3 so I had to type 'pip3 install utm'
	

	Within Java folder of OneDrive:
	- Uses same sample input as Java folder
	- UTMjava.csv is respective output data
	- Note: run GPStoUTM.java which will access Conversion.java


# StructureCSVforAriel Folder
- Our volunteer team member working on sign deterioration wanted historical-2.csv calculated for quartile percentiles and arranged in a certain way for easier analysis.
- historicalNew.csv is the output
- Structure.java is the script that alters and calculates new data from historical-2.csv into historicalNew.csv

# Main
- Contains the source code for the SignFinder Algorithm. The Main folder has its own readme.md for more details.
	
	
