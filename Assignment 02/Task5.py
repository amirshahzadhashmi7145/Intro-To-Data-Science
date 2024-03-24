import folium
import pandas as pd

data = pd.read_csv('pak-heritage-sites.csv')

df = pd.DataFrame(data, columns=['Latitude', 'Longitude', 'Landmark'])

heritage_sites = folium.Map(location=[30.3753, 69.3451], zoom_start=5)

import csv

# Open the CSV file
with open('pak-heritage-sites.csv', 'r') as file:
    # Create a CSV reader
    csv_reader = csv.reader(file)
    
    # Iterate over each row
    for row in csv_reader:
        folium.Marker(
          location=[row[0], row[1]],
          popup=row[2],
          icon=folium.Icon(color='red', icon='info-sign')
        ).add_to(heritage_sites)
  
heritage_sites