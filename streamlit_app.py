import streamlit as st
from streamlit_js_eval import streamlit_js_eval, copy_to_clipboard, create_share_link, get_geolocation
import json
from geopy.geocoders import Nominatim

if st.checkbox("Check my location"):
    loc = get_geolocation()


geolocator = Nominatim(user_agent="location_finder")
if loc:
# Streamlit app
    st.title("City, State, and Country Finder")

    # Get latitude and longitude as input
    latitude = loc['coords']['latitude']
    longitude = loc['coords']['longitude']

    if latitude and longitude:
        location = geolocator.reverse((latitude, longitude), language="en")

        if location:
            address = location
            st.write(f"Address: {address}")
        else:
            st.write("Location not found. Please check the coordinates.")
    else:
        st.write("Please enter valid coordinates.")