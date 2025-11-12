import random
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
from fractions import Fraction
from groq import Groq
import os

# API Keys
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY)

def get_real_time_data():
    return {
        "Heart Rate (BPM)": random.randint(60, 120),
        "Oxygen Saturation (%)": round(random.uniform(85, 100), 1),
        "Blood Pressure (mmHg)": f"{random.randint(90, 120)}/{random.randint(60, 80)}",
        "Respiratory Rate (BPM)": random.randint(12, 20),
        "Hydration Level (%)": round(random.uniform(40, 100), 1),
        "Battery Level (%)": random.randint(10, 100),
        "Food Supply (Days)": random.randint(1, 10),
        "Water Supply (Liters)": random.randint(1, 50),
    }

def predict_survival_time(data):
    o = data["Oxygen Saturation (%)"] / 100
    h = data["Hydration Level (%)"] / 100
    b = data["Battery Level (%)"] / 100
    f = data["Food Supply (Days)"] / 10
    return round((o + h + b + f) * 10, 2)

def safe_float(value):
    first_token = str(value).split()[0]
    try:
        if "/" in first_token:
            numerator = first_token.split("/")[0]
            return float(numerator)
        return float(first_token)
    except ValueError:
        try:
            return float(Fraction(first_token))
        except (ValueError, ZeroDivisionError):
            return None

def render_arms_dashboard():
    st.markdown("<h2 style='text-align:center;'>🩺 Real-Time Astronaut Monitor</h2>", unsafe_allow_html=True)

    data = get_real_time_data()
    survival_time = predict_survival_time(data)

    st.markdown(
        f"""
        <div style='background:linear-gradient(90deg,#271c55,#2e205f); border-radius:15px; padding:25px; text-align:center;'>
            <h2 style='color:#fdd835;'>Predicted Survival Time</h2>
            <h1 style='color:#fbc02d; font-size:50px;'>{survival_time:.2f} Hours</h1>
            <p style='color:#ffb74d;'>⚠️ Warning - Monitor closely</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.subheader("Health & Resource Metrics")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("❤️ Heart Rate", f"{data['Heart Rate (BPM)']} BPM")
        st.metric("🩸 Blood Pressure", data["Blood Pressure (mmHg)"])
        st.metric("🔋 Battery Level", f"{data['Battery Level (%)']}%")
    with col2:
        st.metric("🫁 Respiratory Rate", f"{data['Respiratory Rate (BPM)']} BPM")
        st.metric("💧 Hydration Level", f"{data['Hydration Level (%)']}%")
        st.metric("🍽️ Food Supply", f"{data['Food Supply (Days)']} Days")
    with col3:
        st.metric("🧠 Oxygen Saturation", f"{data['Oxygen Saturation (%)']}%")
        st.metric("🚰 Water Supply", f"{data['Water Supply (Liters)']} L")

    if data["Oxygen Saturation (%)"] < 90 or data["Battery Level (%)"] < 20:
        st.warning("🚨 Critical Alert: Low Oxygen or Battery Detected!")

    st.write("---")
    st.subheader("Resource Overview")

    chart_rows = []
    for metric, value in data.items():
        numeric_value = safe_float(value)
        if numeric_value is not None:
            chart_rows.append({"Metric": metric, "Value": numeric_value})

    if chart_rows:
        df = pd.DataFrame(chart_rows)
        fig = go.Figure([go.Bar(x=df["Metric"], y=df["Value"], marker_color="#60A5FA")])
        fig.update_layout(template="plotly_dark", margin=dict(l=20, r=20, t=30, b=20))
        st.plotly_chart(fig, use_container_width=True)

    st.write("---")
    st.subheader("🤖 AI Advisor")

    if st.button("Get AI Recommendations"):
        try:
            res = client.chat.completions.create(
                messages=[{"role": "user", "content": "Provide astronaut survival improvement tips."}],
                model="llama-3.3-70b-versatile",
            )
            st.success(res.choices[0].message.content)
        except Exception as e:
            st.error(f"AI API Error: {e}")

