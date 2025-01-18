import streamlit as st
import pandas as pd
import pickle

# Load the trained RandomForest model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Streamlit app title
st.title("Gold Price Prediction")
st.write("Enter the date (Day, Month, Year) to predict the 'Close/Last' value for gold:")

# Input fields for user to enter Day, Month, and Year
day = st.number_input("Day", min_value=1, max_value=31, value=1)
month = st.number_input("Month", min_value=1, max_value=12, value=1)
year = st.number_input("Year", min_value=2000, max_value=2100, value=2024)

# Predict button
if st.button("Predict"):
    # Create a DataFrame for the user inputs
    input_data = pd.DataFrame({
        'Day': [day], 
        'Month': [month], 
        'Year': [year]
    })
    
    # Predict using the loaded Random Forest model
    try:
        prediction = model.predict(input_data)
        st.success(f"Predicted 'Close/Last' value: {prediction[0]:.2f}")
    except Exception as e:
        st.error(f"Error: {e}")

# Add instructions or footer
st.write("---")
st.write("This app predicts the 'Close/Last' gold price based on Day, Month, and Year input.")
