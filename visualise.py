import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
import warnings
warnings.filterwarnings('ignore')
import seaborn as sns
color_pal = sns.color_palette()
import folium
from folium.plugins import HeatMap
import os

class Visualise:
    def __init__(self) -> None:
        pass

    # Plot crime location.
    def plot_crimes_outliers(self, data, title):
        plt.figure(figsize=(5,5))
        plt.scatter(data.loc[:,'Longitude'], data.loc[:,'Latitude'], s=15)
        plt.title(title, fontsize=14)
        plt.xlabel('Longitude', fontsize=14)
        plt.ylabel('Latitude', fontsize=14)
        plt.show()

    def create_crime_density_heatmap(self, data, title, output_path):
        # Create a base map centered at the mean coordinates
        base_map = folium.Map(location=[data['Latitude'].mean(), data['Longitude'].mean()], zoom_start=12)

        # Extract latitude and longitude as a list of lists
        locations = data[['Latitude', 'Longitude']].values.tolist()

        # Create HeatMap
        HeatMap(locations).add_to(base_map)

        # Save the map to the output path
        output_file = os.path.join(output_path, f'{title}_Crime_Density_Heatmap.html')
        base_map.save(output_file)
        print(f'Crime Density Heatmap saved as {output_file}')
    
    # Check if data is normally distributed or not?
    def plot_distribution(self, df, column, title):
        sns.kdeplot(data=df[column], shade=True)
        plt.title(f'Kernel Density Estimation Plot - {title}')
        plt.xlabel(title)
        plt.ylabel('Density')
        plt.show()

    # Display Time Series Analysis
    def plot_time_series_analysis(self, df):
        # Plot the time series data
        plt.figure(figsize=(10, 6))
        plt.plot(df['CMPLNT_FR_DT'], df['Crime_count'], linestyle='-') # marker='o',
        plt.title('Number of Crimes Per Day Over Time')
        plt.xlabel('Date')
        plt.ylabel('Number of Crimes')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    


