import streamlit as st
import joblib
import pandas as pd

# Load the models using joblib
gb_model_path = 'C:\\Users\\amerk\\project folder\\best_gb_model.joblib'
xgb_model_path = 'C:\\Users\\amerk\\project folder\\best_xgb_model.joblib'

# Load models using joblib
gb_model = joblib.load(gb_model_path)
xgb_model = joblib.load(xgb_model_path)

# Streamlit app
st.title('Solar Power Generation Prediction')

# Dropdown to select model
model_option = st.selectbox('Select Model', ['Gradient Boosting Regressor', 'XGBoost Regressor'])

# Input parameters
distance_to_solar_noon = st.number_input('Distance to Solar Noon (radians)', format="%.4f")
temperature = st.number_input('Temperature (°C)', format="%.2f")
wind_direction = st.number_input('Wind Direction (degrees)', format="%.2f")
wind_speed = st.number_input('Wind Speed (m/s)', format="%.2f")
sky_cover = st.slider('Sky Cover (0-4)', min_value=0, max_value=4)
visibility = st.number_input('Visibility (km)', format="%.2f")
humidity = st.number_input('Humidity (%)', format="%.2f")
average_wind_speed = st.number_input('Average Wind Speed (m/s)', format="%.2f")
average_pressure = st.number_input('Average Pressure (inches of mercury)', format="%.2f")

# Prepare input data
input_data = pd.DataFrame({
    'distance_to_solar_noon': [distance_to_solar_noon],
    'temperature': [temperature],
    'wind_direction': [wind_direction],
    'wind_speed': [wind_speed],
    'sky_cover': [sky_cover],
    'visibility': [visibility],
    'humidity': [humidity],
    'average_wind_speed': [average_wind_speed],
    'average_pressure': [average_pressure]
})

# Handle missing values in input data
input_data = input_data.fillna(0)

# Predict button
if st.button('Get Prediction'):
    # Choose model based on selection
    if model_option == 'Gradient Boosting Regressor':
        model = gb_model
    else:
        model = xgb_model

    # Predict power generated
    prediction = model.predict(input_data)
    
    # Display result
    st.write(f'Predicted Power Generated: {prediction[0]:.2f} Jules for each 3 hours')
