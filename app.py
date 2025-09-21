import streamlit as st
import pandas as pd
import numpy as np
import pickle
import zipfile
import os
from datetime import datetime, timedelta

# ------------------ Unzip Model & Scalers ------------------ #
def unzip_file(zip_name, target_file):
    if not os.path.exists(target_file):  # only unzip if not already extracted
        with zipfile.ZipFile(zip_name, "r") as zip_ref:
            zip_ref.extractall(".")

# Unzip files (make sure you uploaded these zip files to GitHub)
unzip_file("model3.zip", "model3.pkl")
unzip_file("robust1_scaler_flight.zip", "robust1_scaler_flight.pkl")
unzip_file("robust2_scaler_flight.zip", "robust2_scaler_flight.pkl")

# ------------------ Load Model and Scalers ------------------ #
with open("model3.pkl", "rb") as f:
    model3 = pickle.load(f)

with open("robust1_scaler_flight.pkl", "rb") as f:
    scaler = pickle.load(f)

with open("robust2_scaler_flight.pkl", "rb") as f:
    scaler2 = pickle.load(f)

# ------------------ App Title ------------------ #
st.title("✈️ Flight Price Prediction")

st.header("Enter Flight Details:")

# ------------------ User Inputs ------------------ #
col1, col2 = st.columns(2)
with col1:
    source = st.selectbox("Source City", ["Chennai", "Delhi", "Hyderabad", "Kolkata", "Mumbai"])
with col2:
    destination = st.selectbox("Destination City", ["Chennai", "Delhi", "Hyderabad", "Kolkata", "Mumbai"])

# Departure
dep_date = st.date_input("Departure Date", value=datetime.today())
dep_time = st.selectbox("Departure Time", ['Early Morning', 'Morning', 'Afternoon', 'Evening', 'Night', 'Late Night'])

# Arrival
arr_date = st.date_input("Arrival Date", value=datetime.today())
arr_time = st.selectbox("Arrival Time", ['Early Morning', 'Morning', 'Afternoon', 'Evening', 'Night', 'Late Night'])

# Airline & Class
airline = st.radio("Airline", ["AirAsia", "GO FIRST", "Indigo", "SpiceJet", "StarAir", "Trujet", "Vistara"])
flight_class = st.selectbox("Class", ["economy", "Business"])

# Stops
stop = st.selectbox("Number of Stops", ["non-stop", "1-stop", "2-or-more stops"])

# ------------------ Time Slot Mapping ------------------ #
time_mapping = {
    'Early Morning': 5,   # 5 AM
    'Morning': 9,         # 9 AM
    'Afternoon': 14,      # 2 PM
    'Evening': 18,        # 6 PM
    'Night': 22,          # 10 PM
    'Late Night': 2       # 2 AM
}
stop_mapping = {"non-stop": 0, "1-stop": 1, "2-or-more stops": 2}
class_mapping = {"economy": 0, "Business": 1}

# ------------------ Calculate Duration ------------------ #
dep_datetime = datetime.combine(dep_date, datetime.min.time()) + timedelta(hours=time_mapping[dep_time])
arr_datetime = datetime.combine(arr_date, datetime.min.time()) + timedelta(hours=time_mapping[arr_time])

# Handle overnight/next-day flights
if arr_datetime < dep_datetime:
    arr_datetime += timedelta(days=1)

duration = (arr_datetime - dep_datetime).total_seconds() / 60  # minutes

# ------------------ Journey Features ------------------ #
journey_day = dep_date.day
journey_month = dep_date.month

# ------------------ One-hot Encoding ------------------ #
airlines = ['AirAsia','GO FIRST','Indigo','SpiceJet','StarAir','Trujet','Vistara']
sources = ['Chennai','Delhi','Hyderabad','Kolkata','Mumbai']
destinations = ['Chennai','Delhi','Hyderabad','Kolkata','Mumbai']

new_flight = pd.DataFrame([{
    'dep_time': list(time_mapping.keys()).index(dep_time),
    'stop': stop_mapping[stop],
    'arr_time': list(time_mapping.keys()).index(arr_time),
    'class': class_mapping[flight_class],
    **{f'airline_{a}': int(a == airline) for a in airlines},
    **{f'source_{s}': int(s == source) for s in sources},
    **{f'destination_{d}': int(d == destination) for d in destinations},
    'duration_scaled': scaler.transform(pd.DataFrame({'duration': [duration]}))[0][0],
    'journey_day_sin': np.sin(2*np.pi*journey_day/31),
    'journey_day_cos': np.cos(2*np.pi*journey_day/31),
    'journey_month_sin': np.sin(2*np.pi*journey_month/12),
    'journey_month_cos': np.cos(2*np.pi*journey_month/12)
}])

# ------------------ Prediction ------------------ #
if st.button("Predict Price"):

    if source == destination:
        st.error("⚠️ Source and Destination cannot be the same.")
    else:
        predicted_price_scaled = model3.predict(new_flight)[0]
        predicted_price_actual = scaler2.inverse_transform([[predicted_price_scaled]])[0][0]
        st.success(f"💰 Predicted Flight Price: ₹{predicted_price_actual:.2f}")
