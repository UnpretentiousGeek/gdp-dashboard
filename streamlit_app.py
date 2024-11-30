import streamlit as st
from streamlit_js_eval import streamlit_js_eval, copy_to_clipboard, create_share_link, get_geolocation
import json
from openai import OpenAI
from geopy.geocoders import Nominatim
import requests

geolocator = Nominatim(user_agent="location_finder")

# Streamlit app
st.title("City, State, and Country Finder")
client = OpenAI(api_key=st.secrets["openai_key"])


if st.checkbox("Check my location"):
    loc = get_geolocation()

if loc:
    latitude = loc['coords']['latitude']
    longitude = loc['coords']['longitude']
    st.write(latitude)
    st.write(longitude)

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

    location = city + "," + state + "," + country
    coor_message = f"""
    This is the location {location}, format it in a way so that it is accepted by 
    openweathermap API example if the location is "City of Syracuse,New York, United States"
    format it as "Syracuse, NY", if just "New York,New York,United States" format it as
    "New York City, NY" and only return the formatted location nothing else 

    """
    stream = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role":"system","content": coor_message},
                      {"role": "user", "content": location}]
        )
    
    st.write(stream.choices[0].message.content)

    if "," in location:

        location = location.split(",")[0].strip()
        st.write(location)

    urlbase = "https://api.openweathermap.org/data/2.5/"
    urlweather = f"weather?q={location}&appid={st.secrets['weather_key']}"
    url = urlbase + urlweather


    response = requests.get(url)
    data = response.json()
    st.write(data)

    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    temp_min = data['main']['temp_min']
    temp_max = data['main']['temp_max']
    humidity = data['main']['humidity']

    
    st.write(
        f"temperature: {round(temp, 2)}")