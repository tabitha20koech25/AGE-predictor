import streamlit as st
import joblib
import numpy as np

st.title("Child Height Prediction App")

st.write("Loading model...")

try:
    model = joblib.load("test.joblib")
    st.success("Model loaded successfully!")
except Exception as e:
    st.error("Could not load the model.")
    st.exception(e)
    st.stop()

st.write("This app predicts a child's weight based on age and height.")

age_1 = st.number_input(
    "Age (years)",
    min_value=0.0,
    max_value=18.0,
    value=6.0
)

height = st.number_input(
    "Height (cm)",
    min_value=30.0,
    max_value=200.0,
    value=100.0
)

if st.button("Predict"):
    try:
        input_features = np.array([[age_1, height]])

        prediction = model.predict(input_features)

        st.success(f"Predicted weight: {prediction[0]:.2f} kg")

    except Exception as e:
        st.error("Prediction failed.")
        st.exception(e)