import streamlit as st
import pandas as pd
import joblib
import numpy as np

st.set_page_config(page_title="Crop Recommender", page_icon="🌱")

# Load the model and label encoder
@st.cache_resource
def load_model():
    try:
        model = joblib.load('crop_model_final.pkl')
        le = joblib.load('label_encoder.pkl')
        return model, le
    except FileNotFoundError:
        st.error("Model files not found. Please run main.py first to generate 'crop_model_final.pkl' and 'label_encoder.pkl'.")
        return None, None

model, le = load_model()

st.title("🌱 Crop Recommendation System")
st.write("Enter the soil and weather conditions to get a crop recommendation.")

if model is not None:
    # Input form
    with st.form("prediction_form"):
        st.subheader("Soil Parameters")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            n = st.number_input("Nitrogen (N)", min_value=0.0, max_value=500.0, value=50.0, help="Ratio of Nitrogen content in soil")
            p = st.number_input("Phosphorus (P)", min_value=0.0, max_value=500.0, value=50.0, help="Ratio of Phosphorus content in soil")
            k = st.number_input("Potassium (K)", min_value=0.0, max_value=500.0, value=50.0, help="Ratio of Potassium content in soil")
            
        with col2:
            ph = st.number_input("pH Level", min_value=0.0, max_value=14.0, value=6.5, help="pH value of the soil")
            oc = st.number_input("Organic Carbon", min_value=0.0, max_value=100.0, value=0.5, help="Organic Carbon content")
            sm = st.number_input("Soil Moisture", min_value=0.0, max_value=100.0, value=50.0, help="Soil Moisture percentage")
            
        st.subheader("Weather Parameters")
        col4, col5, col6 = st.columns(3)
        with col4:
            temp = st.number_input("Temperature (°C)", min_value=-10.0, max_value=60.0, value=25.0)
        with col5:
            humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=60.0)
        with col6:
            rain = st.number_input("Rainfall (mm)", min_value=0.0, max_value=2000.0, value=100.0)
            
        submit_button = st.form_submit_button("Predict Crop", type="primary")

    if submit_button:
        # Prepare input data
        # Feature order must match training: ['N', 'P', 'K', 'pH', 'organic_carbon', 'soil_moisture', 'temperature_c', 'humidity_pct', 'rainfall_mm']
        input_data = pd.DataFrame({
            'N': [n],
            'P': [p],
            'K': [k],
            'pH': [ph],
            'organic_carbon': [oc],
            'soil_moisture': [sm],
            'temperature_c': [temp],
            'humidity_pct': [humidity],
            'rainfall_mm': [rain]
        })
        
        # Predict
        try:
            prediction_idx = model.predict(input_data)[0]
            prediction_name = le.inverse_transform([prediction_idx])[0]
            
            st.success(f"Recommended Crop: **{prediction_name}**")
            
            # Optional: Show probabilities if supported
            if hasattr(model, "predict_proba"):
                probs = model.predict_proba(input_data)[0]
                # Get top 3
                top_3_indices = probs.argsort()[-3:][::-1]
                
                st.markdown("---")
                st.subheader("Top 3 Recommendations:")
                
                cols = st.columns(3)
                for i, idx in enumerate(top_3_indices):
                    crop_name = le.inverse_transform([idx])[0]
                    prob = probs[idx]
                    with cols[i]:
                        st.metric(label=crop_name, value=f"{prob*100:.1f}%")
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")
