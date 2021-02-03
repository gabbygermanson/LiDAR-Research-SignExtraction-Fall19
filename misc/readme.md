# Miscellaneous

This folder will contain all the sample outputs, intermediate files, etc. 


- output_analysis.csv analyzes by human typed input the false positives and negatives in the algorithm output by uploading output_oop.txt and V_20180816_I285_EB_run1(0)_2nd_leg.csv into CloudCompare
	- output_oop.txt is output from running SignFinder.py from repo code folder on V_20180816_I285_EB_run1(0)_2nd_leg.csv
	- V_20180816_I285_EB_run1(0)_2nd_leg.csv is all LiDAR points collected by the van of a portion of highway accessible in either Java or Python folder of this OneDrive link: https://gtvault-my.sharepoint.com/:f:/g/personal/ggermanson3_gatech_edu/EiUZGmGiMVdFjnc1EEF9mTgBdDSXNDs7X-igui8owcejUQ?e=7J8B7u
	- In CloudCompare, you must set Easting, Northing, and Altitude from V_20180816_I285_EB_run1(0)_2nd_leg.csv to X Y Z coords and Retro to Scalar and everything else to Ignore
	- It is also advisable in CloudCompare to adjust the point size of output_oop.txt to a significantly larger point size than V_20180816_I285_EB_run1(0)_2nd_leg.csv points
