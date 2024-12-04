import streamlit as st
import folium
from streamlit_folium import folium_static

# Streamlit app
st.title("Map")

# Input fields for latitude and longitude
latitude = st.text_input("Enter Latitude", placeholder = "0.00")
longitude = st.text_input("Enter Longitude", placeholder = "0.00")

if st.button("Show Location"):
    location = (int(latitude), int(longitude))
    m = folium.Map(location=location, zoom_start=13)
    folium.Marker(location, popup="Your Location").add_to(m)
    folium_static(m)
else:
    st.write("Please enter latitude and longitude to display the location.")