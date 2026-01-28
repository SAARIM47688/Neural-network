import streamlit as st
import numpy as np
import tensorflow as tf

# Load trained model
model = tf.keras.models.load_model("slope_fos_model.keras")

st.title("Slope Factor of Safety (FOS) Predictor")

st.write("Enter soil and slope parameters:")
st.write("Uses an ML-based model for prediction.")

x1 = st.number_input("Slope Height (m)")
x2 = st.number_input("Slope angle (deg)")
x3 = st.number_input("Material Density (Kg/m³)")
x4 = st.number_input("Cohesion (kPa)")
x5 = st.number_input("Angle of internal friction (deg)")

x1_n = (x1-30)/20
x2_n = (x2-20)/30
x3_n = (x3-1500)/1000
x4_n = (x4-20)/40
x5_n = (x5-20)/10

if st.button("Predict FOS"):
    X = np.array([[x1_n, x2_n, x3_n, x4_n, x5_n]])
    fos = model.predict(X)
    st.success(f"Predicted Factor of Safety = {fos[0][0]:.3f}")
st.markdown("""
© 2026 Syed Saarim Ahmad. All rights reserved.
This application is for academic and research purposes only.""")