'''
Last Code Update Date: 13/02/2024
Code Updated By: Pankaj Dilip Goikar
Updated Topics:

1. Imported Data (12/02/2024)
2. Create new features and scaling coordinates. (12/02/2024)
3. Combined date and time column together. (12/02/2024)
4. Visulalised Distribution of the Crime Data Points. (12/02/2024)
5. Divide data into 80% and 20% train and test dataframe. (13/02/2024)


Next Target:
1. Perform Data Preprocessing: Data stationarity check. Create count column in each DCRs.
2. lable each rectangle with their ids. 
*  If one or more datapoints are colaborating more then 50 times then change all points colors to red. So we will get very high crime areas. 
3. Sort the issue of combined_leaf_dcrs.csv, becuase here again we are getting more data points.
4. Data split process for training and testing process.
5. Perform recursively variour prediction algorithm on each DCRs.
6. Perform evaluation process.

'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
from matplotlib import path
from preprocess import Preprocess
from visualise import Visualise
from modelling import Modelling

# Created object of classes.
prp = Preprocess()
vis = Visualise()
mod = Modelling()

path = 'C:/Users/goikar/Quadtree/data/USA_Crime_2008_to_2009.csv'

# Step 1: Load crime data from csv file.
data = prp.data_import(path)
# print('Crime Data Information :------->',data.info())

# Get sample data.
data = prp.get_sample_data(data)
df = data[['CMPLNT_FR_DT', 'CMPLNT_FR_TM','Longitude','Latitude']]
# df = data[['CMPLNT_FR_DT', 'CMPLNT_FR_TM','Longitude','Latitude']].head(100)

# Check null values.
df = prp.null_values_check(df)
# print('Total Number of Null Values :------->',df.isnull().sum())

# Combine date and time into a single datetime column and convert date time into DateTime format.
df = prp.combine_datetime(df)

# # Plot crime location with outliers
# vis.plot_crimes_outliers(df, title='Crimes Data Points With Outliers')

# # Remove outliers
# df = prp.remove_outlier(df)

# # Plot crime locaiton without outliers
# vis.plot_crimes_outliers(df, title='Crimes Data Points Without Outliers.')

# # Create Crime Density Heatmap
# output_path = 'C:/Users/goikar/Quadtree/12-2-2024/output_files/'
# title = 'Crime_Density'
# vis.create_crime_density_heatmap(df, title, output_path)

# # Check Data Normalisation
# # Visualize the distribution of crime incidents over Date
# vis.plot_distribution(df, 'CMPLNT_FR_DT', 'Date')

# # Visualize the distribution of crime incidents over Time
# vis.plot_distribution(df, 'CMPLNT_FR_TM', 'Time')

# Crime Count and add new column
time_series_data = prp.crime_count(df)
df = pd.merge(df, time_series_data, on='CMPLNT_FR_DT', how='left')

# Display Time Series Analysis or Crimes per day
vis.plot_time_series_analysis(time_series_data)

# Adding some new features to Dataframe and Scaling Longitute and Latitude. 
df = prp.create_new_features(df)

# Split data into training and testing sets
train_df, test_df = mod.split_train_test(df, test_size=0.2, random_state=42)

print(train_df)
print(train_df.info())

print(test_df)
print(test_df.info())










