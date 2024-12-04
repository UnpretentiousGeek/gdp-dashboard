import streamlit as st
import folium
from streamlit_folium import folium_static

# Streamlit app
st.title("Map")

# Input fields for latitude and longitude
latitude = st.number_input("Enter Latitude", value=0.000000, format="%0.000001f")
longitude = st.number_input("Enter Longitude", value=0.000000, format="%0.000001f")

if st.button("Show Location"):
    location = (latitude, longitude)
    m = folium.Map(location=location, zoom_start=13)
    folium.Marker(location, popup="Your Location").add_to(m)
    folium_static(m)
else:
    st.write("Please enter latitude and longitude to display the location.")