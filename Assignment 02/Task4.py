import folium
import pandas as pd

df = pd.read_csv('nuclear_waste_sites.csv')

# Create a map centered on the US
map_us = folium.Map(location=[37.0902, -95.7129], zoom_start=4)

# Add markers for each nuclear waste storage site
for index, row in df.iterrows():
    folium.Marker(
        location=[row['lat'], row['lon']],
        popup=row['text'],
        icon=folium.Icon(color='red', icon='info-sign')
    ).add_to(map_us)

# Display the map
map_us