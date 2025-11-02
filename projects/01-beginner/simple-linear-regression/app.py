import streamlit as st
import numpy as np
import pandas as pd
from joblib import load
from pathlib import Path

st.set_page_config(page_title="Simple Linear Regression", layout="centered")
st.title("📈 Simple Linear Regression Demo")

st.markdown("Use the slider to generate a synthetic dataset, train a linear model, and make predictions.")

n = st.slider("Samples", 50, 1000, 300, 50)
noise = st.slider("Noise std", 0.1, 3.0, 1.2, 0.1)

rng = np.random.RandomState(42)
X = rng.rand(n, 1) * 10
y = 3.5 * X[:, 0] + 7 + rng.randn(n) * noise

st.line_chart(pd.DataFrame({"x": X[:,0], "y": y}).sort_values("x"), x="x", y="y")

if st.button("Train Model"):
    from sklearn.linear_model import LinearRegression
    m = LinearRegression().fit(X, y)
    Path("outputs").mkdir(exist_ok=True)
    import joblib
    joblib.dump(m, "outputs/linear_model.joblib")
    st.success("Model trained and saved to outputs/linear_model.joblib")

x_new = st.number_input("Predict for x=", value=5.0)

try:
    model = load("outputs/linear_model.joblib")
    pred = float(model.predict([[x_new]])[0])
    st.info(f"Prediction: {pred:.3f}")
except Exception:
    st.warning("Train the model first, then predict.")
