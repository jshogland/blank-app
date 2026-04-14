import streamlit as st
from streamlit_folium import st_folium
import folium
import geopandas as gpd

db_path='BlackHillsData.gpkg'
lyr='sawmills'
gdf=gpd.read_file(db_path,layer=lyr)

m=gdf.explore(name='sawmills',color='yellow')

# Add button to load roads layer
if st.button("Load Roads Layer"):
    st.session_state.load_roads = True

# Load roads layer if button was clicked
if st.session_state.get('load_roads', False):
    roads_gdf = gpd.read_file(db_path, layer='roads')
    m = roads_gdf.explore(m=m, name='roads', color='blue')

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


