import numpy as np
import pandas as pd
import pandas.plotting
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings('ignore')
import seaborn as sns
color_pal = sns.color_palette()
# %matplotlib inline


class Preprocess:
    def __init__(self):
        pass
    
    # Improt data.
    def data_import(self, path):
        data = pd.read_csv(path, encoding='latin-1')
        return data

    # Get sample data.
    def get_sample_data(self, df):
        start_date = '2008-01-01'
        end_date = '2009-12-31'
        # Filtering the DataFrame for the chosen date range
        sample_df = pd.DataFrame(df[(df['CMPLNT_FR_DT'] >= start_date) & (df['CMPLNT_FR_DT'] <= end_date)])
        return sample_df

    # Check any null value
    def null_values_check(self, df):
        df = df.dropna()
        return df
    
    # Remove Outliers.
    def remove_outlier(self, df):
        df = df.loc[(df['Latitude'] <= 41.0) & (df['Longitude'] >= -74.5)]
    
    # Combine date and time into a single datetime column and convert date time into DateTime format.
    def combine_datetime(self, df):
        # Convert date and time columns to datetime objects
        df['CMPLNT_FR_DT'] = pd.to_datetime(df['CMPLNT_FR_DT'])
        df['CMPLNT_FR_TM'] = pd.to_datetime(df['CMPLNT_FR_TM'])

        # Combine date and time into a single datetime column
        df['CMPLNT_DATETIME'] = df['CMPLNT_FR_DT'] + pd.to_timedelta(df['CMPLNT_FR_TM'].dt.strftime('%H:%M:%S'))
        
        # Drop the original date and time columns
        df.drop(columns=['CMPLNT_FR_TM'], inplace=True) # df.drop(columns=['CMPLNT_FR_DT', 'CMPLNT_FR_TM'], inplace=True)
        df = df[['CMPLNT_FR_DT', 'CMPLNT_DATETIME', 'Longitude', 'Latitude']] # Rearranged the columns.
        return df

    # Perform time series analysis
    def crime_count(self, df):
        time_series_data = df.groupby('CMPLNT_FR_DT').size().reset_index(name='Crime_count')
        return time_series_data
    
    # Adding some new features to Dataframe.
    def create_new_features(self, df):
        """
        Create time series features based on time series index.
        """
        new_df = df.copy()

        # Scaling Longitude and Latitude
        scaler = StandardScaler()
        new_df[['Scl_Longitude', 'Scl_Latitude']] = scaler.fit_transform(new_df[['Longitude', 'Latitude']])

        # Example: Calculate the distance from a central point
        central_longitude = new_df['Longitude'].mean()
        central_latitude = new_df['Latitude'].mean()
        new_df['Distance_From_Central_Point'] = ((new_df['Longitude'] - central_longitude)**2 + (new_df['Latitude'] - central_latitude)**2)**0.5

        new_df['Hour_of_crime'] = new_df['CMPLNT_DATETIME'].dt.hour                     # Hour of the Crime.
        new_df['Dayofweek_of_crime'] = new_df['CMPLNT_DATETIME'].dt.dayofweek           # Day of the Week of Crime. Example: Monday, Tuesday....
        new_df['Quarter_of_crime'] = new_df['CMPLNT_DATETIME'].dt.quarter               # Quarter of the Crime.
        new_df['Month_of_crime'] = new_df['CMPLNT_DATETIME'].dt.month                   # Month of the Crime.
        new_df['Year_of_crime'] = new_df['CMPLNT_DATETIME'].dt.year                     # Year of the Crime.
        new_df['Dayofyear_of_crime'] = new_df['CMPLNT_DATETIME'].dt.dayofyear           # Day of the Year of the Crime.
        new_df['Dayofmonth_of_crime'] = new_df['CMPLNT_DATETIME'].dt.day                # Day of the Month of the Crime.
        new_df['Weekofyear_of_crime'] = new_df['CMPLNT_DATETIME'].dt.isocalendar().week # Week of the Year of the Crime.

        # Rearrange columns
        new_df = new_df[['CMPLNT_FR_DT', 'CMPLNT_DATETIME', 'Longitude', 'Latitude', 'Scl_Longitude', 'Scl_Latitude', 'Hour_of_crime',  'Dayofweek_of_crime',  'Quarter_of_crime',  'Month_of_crime',  'Dayofyear_of_crime',  'Dayofmonth_of_crime',  'Weekofyear_of_crime', 'Year_of_crime', 'Distance_From_Central_Point', 'Crime_count']]
        return new_df
    

