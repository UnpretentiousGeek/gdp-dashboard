import streamlit as st
from streamlit_js_eval import streamlit_js_eval, copy_to_clipboard, create_share_link, get_geolocation
import json

from opencage.geocoder import OpenCageGeocode
api_key = "d8c5895c69b84c54b16f3e043c02024d"
geocoder = OpenCageGeocode(api_key)

if st.checkbox("Check my location"):
    loc = get_geolocation()

if loc:
    st.title("City, State, and Country Finder")

    # Get latitude and longitude as input
    latitude = loc['coords']['latitude']
    longitude = loc['coords']['longitude']

    if latitude and longitude:
        result = geocoder.reverse_geocode(latitude, longitude)

        if result:
            # Extract the city, state, and country from the result
            city = result[0]['components'].get('city', '')
            state = result[0]['components'].get('state', '')
            country = result[0]['components'].get('country', '')

            # Display the city, state, and country
            st.write(f"City: {city}")
            st.write(f"State: {state}")
            st.write(f"Country: {country}")
        else:
            st.write("Location not found. Please check the coordinates.")
    else:
        st.write("Please enter valid coordinates.")

        