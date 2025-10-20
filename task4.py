import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import HeatMap

try:
    df = pd.read_csv('US_Accidents_March23.csv')
    df['Start_Time'] = pd.to_datetime(df['Start_Time'])
    df['Hour'] = df['Start_Time'].dt.hour
except FileNotFoundError:
    print("Error: File not found! Make sure 'your_dataset.csv' is in the same folder or provide the correct path.")
    exit()

plt.figure(figsize=(12, 6))
sns.countplot(x='Hour', data=df, palette='viridis')
plt.title('Number of Accidents by Hour of the Day', fontsize=16)
plt.xlabel('Hour of the Day (0-23)')
plt.ylabel('Number of Accidents')
plt.grid(axis='y', linestyle='--')
plt.show()

if 'Weather_Condition' in df.columns:
    plt.figure(figsize=(12, 8))
    weather_counts = df['Weather_Condition'].value_counts().nlargest(15)
    sns.barplot(y=weather_counts.index, x=weather_counts.values, palette='plasma')
    plt.title('Top 15 Weather Conditions During Accidents', fontsize=16)
    plt.xlabel('Number of Accidents')
    plt.ylabel('Weather Condition')
    plt.show()

if 'Road_Condition' in df.columns:
    plt.figure(figsize=(12, 8))
    road_counts = df['Road_Condition'].value_counts().nlargest(10)
    sns.barplot(y=road_counts.index, x=road_counts.values, palette='magma')
    plt.title('Top 10 Road Conditions During Accidents', fontsize=16)
    plt.xlabel('Number of Accidents')
    plt.ylabel('Road Condition')
    plt.show()

map_center = [df['Start_Lat'].dropna().mean(), df['Start_Lng'].dropna().mean()]
accident_map = folium.Map(location=map_center, zoom_start=10)

heat_data = [[row['Start_Lat'], row['Start_Lng']] for index, row in df.dropna(subset=['Start_Lat', 'Start_Lng']).iterrows()]

HeatMap(heat_data).add_to(accident_map)

accident_map.save('accident_hotspots_map.html')

print("Analysis complete. Interactive map saved as 'accident_hotspots_map.html'.")