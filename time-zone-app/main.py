import streamlit as st
from datetime import datetime, time
from zoneinfo import ZoneInfo

TIME_ZONES = [
    "UTC",
    "Asia/Karachi",
    "America/New_York",  # Fixed typo in time zone
    "Europe/London",
    "Asia/Tokyo",
    "Australia/Sydney",
    "America/Los_Angeles",
    "Europe/Berlin",
    "Asia/Dubai",
    "Asia/Kolkata"   
]

st.title("Time Zone App")

# Select multiple time zones
selected_timezone = st.multiselect("Select Timezone", TIME_ZONES, default=["UTC", "Asia/Karachi"])

st.subheader("Selected Timezones:")
for tz in selected_timezone:
    current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    st.write(f"***{tz}***: {current_time}")

# Time conversion section
st.subheader("Convert Time Between TimeZones")
current_time = st.time_input("Current Time", value=datetime.now().time())

from_tz = st.selectbox("From TimeZone:", TIME_ZONES, index=0)
to_tz = st.selectbox("To TimeZone:", TIME_ZONES, index=1)

if st.button("Convert Time"):
    # Combine current date with selected time
    dt = datetime.combine(datetime.today(), current_time)
    # Attach timezone info
    dt = dt.replace(tzinfo=ZoneInfo(from_tz))
    # Convert to target timezone
    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I:%M:%S %p")

    # Show the result inside the if block
    st.success(f"Converted Time in {to_tz}: {converted_time}")
