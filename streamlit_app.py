import streamlit as st
from streamlit_folium import st_folium
import folium
import geopandas as gpd

db_path=r'C:/Users/jshogland/John/presentation/Authoring/fy2026/BlackHills/BlackHillsData.gpkg'
lyr='sawmills'
gdf=gpd.read_file(db_path,layer=lyr)

m=gdf.explore(name='sawmills',color='yellow')
tl=folium.TileLayer(
    tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
    attr='Esri',
    name='Esri Satellite',
    overlay=True,
    control=True,
)
tl.add_to(m)
lc=folium.LayerControl()
lc.add_to(m)

st.title("Folium in Streamlit") 
col1 = st.columns(1)[0]
with col1:
    st_folium(m, width=700, height=500)


