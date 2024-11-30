import streamlit as st
from streamlit_js_eval import streamlit_js_eval, copy_to_clipboard, create_share_link, get_geolocation
import json

from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="location_finder")

# Streamlit app
st.title("City, State, and Country Finder")

if st.checkbox("Check my location"):
    loc = get_geolocation()

if loc:
    latitude = loc['coords']['latitude']
    longitude = loc['coords']['longitude']

    if latitude and longitude:
        location = geolocator.reverse((latitude, longitude), language="en")

        if location:
            # Break the address into components
            address = location.raw.get('address', {})
            city = address.get('city', '')
            state = address.get('state', '')
            country = address.get('country', '')

            # Display the city, state, and country
            st.write(f"City: {city}")
            st.write(f"State: {state}")
            st.write(f"Country: {country}")
        else:
            st.write("Location not found. Please check the coordinates.")
    else:
        st.write("Please enter valid coordinates.")