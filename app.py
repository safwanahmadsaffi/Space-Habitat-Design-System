
# # import os
# # import random
# # import pandas as pd
# # import requests
# # import streamlit as st
# # import plotly.graph_objects as go
# # from groq import Groq

# # # =========================
# # # 🔐 API KEYS (Replace or use HF Secrets)
# # # =========================
# # NASA_API_KEY = os.getenv("NASA_API_KEY", "tQ9mfp3AgyuiCfWCnvdTMBTd58J1fdWg3D2lm1Af")
# # GROQ_API_KEY = os.getenv("GROQ_API_KEY", "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")

# # client = Groq(api_key=GROQ_API_KEY)

# # # =========================
# # # 🛰️ Streamlit Config
# # # =========================
# # st.set_page_config(page_title="🚀 ARMS Mission Console", layout="wide")
# # st.sidebar.title("🔭 ARMS Navigation")
# # section = st.sidebar.radio("Choose Section:", ["🏠 Home", "🛰 ARMS Dashboard", "📊 Analytics Dashboard", "🌌 NASA Image View"])

# # st.title("🚀 ARMS: Astronaut Resource & Mission System")

# # # =========================
# # # 🌌 NASA Image Fetcher
# # # =========================
# # def get_nasa_image():
# #     try:
# #         res = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}", timeout=10)
# #         data = res.json()
# #         # APOD may return video or image; prefer hdurl for higher resolution when available
# #         media_type = data.get("media_type", "image")
# #         if media_type != "image":
# #             img = data.get("thumbnail_url") or data.get("url") or "https://nasagallery-yj7tr553ia-ue.a.run.app/random"
# #         else:
# #             img = data.get("hdurl") or data.get("url") or "https://nasagallery-yj7tr553ia-ue.a.run.app/random"
# #         title = data.get("title", "NASA Space Image")
# #         explanation = data.get("explanation", "No description available.")
# #         return img, title, explanation
# #     except Exception:
# #         return "https://nasagallery-yj7tr553ia-ue.a.run.app/random", "Fallback NASA Gallery", "No description available."

# # # =========================
# # # 🩺 ARMS (Astronaut Dashboard)
# # # =========================
# # def get_real_time_data():
# #     return {
# #         "Heart Rate (BPM)": random.randint(60, 120),
# #         "Oxygen Saturation (%)": round(random.uniform(85, 100), 1),
# #         "Blood Pressure (mmHg)": f"{random.randint(90, 120)}/{random.randint(60, 80)}",
# #         "Respiratory Rate (BPM)": random.randint(12, 20),
# #         "Hydration Level (%)": round(random.uniform(40, 100), 1),
# #         "Battery Level (%)": random.randint(10, 100),
# #         "Food Supply (Days)": random.randint(1, 10),
# #         "Water Supply (Liters)": random.randint(1, 50),
# #     }

# # def predict_survival_time(data):
# #     o = data["Oxygen Saturation (%)"] / 100
# #     h = data["Hydration Level (%)"] / 100
# #     b = data["Battery Level (%)"] / 100
# #     f = data["Food Supply (Days)"] / 10
# #     return round((o + h + b + f) * 10, 2)

# # # =========================
# # # 📊 Analytics & Recommendations
# # # =========================
# # def get_mission_recommendation(mission):
# #     """AI-generated mission insights"""
# #     prompt = (
# #         f"Given this mission data: "
# #         f"Name: {mission['Mission Name']}, "
# #         f"Target Type: {mission['Target Type']}, "
# #         f"Distance: {mission['Distance from Earth (light-years)']} light-years, "
# #         f"Cost: {mission['Mission Cost (billion USD)']} billion USD, "
# #         f"Success Rate: {mission['Mission Success (%)']}%, "
# #         f"Provide insights and suggestions for optimization."
# #     )
# #     try:
# #         res = client.chat.completions.create(
# #             messages=[{"role": "user", "content": prompt}],
# #             model="llama-3.3-70b-versatile",
# #         )
# #         return res.choices[0].message.content
# #     except Exception as e:
# #         return f"Error fetching AI insights: {e}"

# # # =========================
# # # 🎛 SECTION: HOME
# # # =========================
# # if section == "🏠 Home":
# #     st.markdown("""
# #     ### 🛰 Welcome to ARMS — Autonomous Resource Management System

# #     This integrated platform provides:
# #     - **🩺 ARMS Dashboard:** Real-time astronaut vitals and survival estimation.  
# #     - **📊 Analytics Dashboard:** Mission dataset analysis & AI insights.  
# #     - **🌌 NASA Image View:** Explore NASA’s daily astronomy images.  

# #     ---
# #     """)

# # # =========================
# # # 🎛 SECTION: ARMS DASHBOARD
# # # =========================
# # elif section == "🛰 ARMS Dashboard":
# #     st.header("🩺 Real-Time Astronaut Survival Monitor")

# #     data = get_real_time_data()
# #     survival = predict_survival_time(data)

# #     col1, col2 = st.columns(2)
# #     with col1:
# #         st.metric("Predicted Survival Time", f"{survival} Hours")
# #         st.subheader("Health & Resource Metrics")
# #         for k, v in data.items():
# #             st.metric(k, v)
# #         if data["Oxygen Saturation (%)"] < 90 or data["Battery Level (%)"] < 20:
# #             st.warning("🚨 Critical Alert: Low Oxygen or Battery!")

# #     with col2:
# #         df = pd.DataFrame({"Metric": list(data.keys()), "Value": list(data.values())})
# #         fig = go.Figure([go.Bar(x=df["Metric"], y=df["Value"], marker_color="darkcyan")])
# #         fig.update_layout(title="Astronaut Resource Overview", xaxis_title="Metric", yaxis_title="Value")
# #         st.plotly_chart(fig, use_container_width=True)

# #     st.subheader("🤖 AI Advisor Suggestions")
# #     try:
# #         res = client.chat.completions.create(
# #             messages=[{"role": "user", "content": "Give astronaut survival improvement tips."}],
# #             model="llama-3.3-70b-versatile",
# #         )
# #         st.success(res.choices[0].message.content)
# #     except Exception as e:
# #         st.error(f"Groq API Error: {e}")

# # # =========================
# # # 🎛 SECTION: ANALYTICS DASHBOARD
# # # =========================
# # elif section == "📊 Analytics Dashboard":
# #     st.header("📊 Mission Analytics & AI Recommendations")
# #     uploaded_file = st.file_uploader("Upload your mission dataset (CSV format)", type="csv")

# #     if uploaded_file:
# #         df = pd.read_csv(uploaded_file)
# #         st.write("### Dataset Preview", df.head())

# #         mission_id = st.selectbox("Select a Mission ID", df["Mission ID"].unique())

# #         if mission_id:
# #             mission = df[df["Mission ID"] == mission_id].iloc[0]
# #             st.subheader(f"Mission Details: {mission_id}")
# #             st.write(mission)

# #             if st.button("🧠 Get AI Recommendation"):
# #                 st.info("Fetching AI insights from Groq API...")
# #                 rec = get_mission_recommendation(mission)
# #                 st.success(rec)
# #     else:
# #         st.warning("Please upload a CSV file to continue.")

# # # =========================
# # # 🎛 SECTION: NASA IMAGE
# # # =========================
# # elif section == "🌌 NASA Image View":
# #     st.header("🌌 NASA Space Imagery")
# #     try:
# #         img_url, title, explanation = get_nasa_image()
# #         if img_url:
# #             st.image(img_url, caption=title, use_container_width=True)
# #             with st.expander("Description"):
# #                 st.write(explanation)
# #         else:
# #             st.warning("No NASA image available right now.")
# #     except Exception as e:
# #         st.error(f"Failed to load NASA image: {e}")
# # # =========================
# import os
# import random
# from fractions import Fraction

# import pandas as pd
# import requests
# import streamlit as st
# import plotly.graph_objects as go
# from groq import Groq

# # =========================
# # 🔐 API KEYS (Replace or use HF Secrets)
# # =========================
# NASA_API_KEY = os.getenv("NASA_API_KEY", "tQ9mfp3AgyuiCfWCnvdTMBTd58J1fdWg3D2lm1Af")
# GROQ_API_KEY = os.getenv("GROQ_API_KEY", "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")

# client = Groq(api_key=GROQ_API_KEY)

# # =========================
# # 🛰️ Streamlit Config
# # =========================
# st.set_page_config(page_title="🚀 ARMS Mission Console", layout="wide")
# st.sidebar.title("🔭 ARMS Navigation")
# section = st.sidebar.radio("Choose Section:", ["🏠 Home", "🛰 ARMS Dashboard", "📊 Analytics Dashboard", "🌌 NASA Image View"])

# # =========================
# # 🌌 NASA Image Fetcher
# # =========================
# def get_nasa_image():
#     try:
#         res = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}", timeout=10)
#         data = res.json()
#         media_type = data.get("media_type", "image")
#         if media_type != "image":
#             img = data.get("thumbnail_url") or data.get("url")
#         else:
#             img = data.get("hdurl") or data.get("url")
#         return img, data.get("title", "NASA Image of the Day"), data.get("explanation", "No description available.")
#     except Exception:
#         return "https://nasagallery-yj7tr553ia-ue.a.run.app/random", "Fallback NASA Image", "No description available."

# # =========================
# # 🩺 ARMS (Astronaut Dashboard)
# # =========================
# def get_real_time_data():
#     return {
#         "Heart Rate (BPM)": random.randint(60, 120),
#         "Oxygen Saturation (%)": round(random.uniform(85, 100), 1),
#         "Blood Pressure (mmHg)": f"{random.randint(90, 120)}/{random.randint(60, 80)}",
#         "Respiratory Rate (BPM)": random.randint(12, 20),
#         "Hydration Level (%)": round(random.uniform(40, 100), 1),
#         "Battery Level (%)": random.randint(10, 100),
#         "Food Supply (Days)": random.randint(1, 10),
#         "Water Supply (Liters)": random.randint(1, 50),
#     }

# def predict_survival_time(data):
#     o = data["Oxygen Saturation (%)"] / 100
#     h = data["Hydration Level (%)"] / 100
#     b = data["Battery Level (%)"] / 100
#     f = data["Food Supply (Days)"] / 10
#     return round((o + h + b + f) * 10, 2)


# def safe_float(value):
#     """Convert mixed string metrics (e.g., '113/79 mmHg') to floats when possible."""
#     first_token = str(value).split()[0]
#     try:
#         if "/" in first_token:
#             numerator = first_token.split("/")[0]
#             return float(numerator)
#         return float(first_token)
#     except ValueError:
#         try:
#             return float(Fraction(first_token))
#         except (ValueError, ZeroDivisionError):
#             return None

# # =========================
# # 📊 Analytics & Recommendations
# # =========================
# def get_mission_recommendation(mission):
#     prompt = (
#         f"Given this mission data: "
#         f"Name: {mission['Mission Name']}, "
#         f"Target Type: {mission['Target Type']}, "
#         f"Distance: {mission['Distance from Earth (light-years)']} light-years, "
#         f"Cost: {mission['Mission Cost (billion USD)']} billion USD, "
#         f"Success Rate: {mission['Mission Success (%)']}%, "
#         f"Provide insights and suggestions for optimization."
#     )
#     try:
#         res = client.chat.completions.create(
#             messages=[{"role": "user", "content": prompt}],
#             model="llama-3.3-70b-versatile",
#         )
#         return res.choices[0].message.content
#     except Exception as e:
#         return f"Error fetching AI insights: {e}"

# # =========================
# # 🎛 SECTION: HOME
# # =========================
# if section == "🏠 Home":
#     st.markdown("""
#     ### 🛰 Welcome to ARMS — Autonomous Resource Management System

#     This integrated platform provides:
#     - **🩺 ARMS Dashboard:** Real-time astronaut vitals and survival estimation.  
#     - **📊 Analytics Dashboard:** Mission dataset analysis & AI insights.  
#     - **🌌 NASA Image View:** Explore NASA’s daily astronomy images.  

#     ---
#     """)

# # =========================
# # 🎛 SECTION: ARMS DASHBOARD
# # =========================
# elif section == "🛰 ARMS Dashboard":
#     st.markdown("<h2 style='text-align:center; color:#F5F5F5;'>🩺 Real-Time Astronaut Monitor</h2>", unsafe_allow_html=True)

#     # --- Simulated Data ---
#     data = get_real_time_data()
#     survival_time = predict_survival_time(data)

#     # --- Survival Time Card ---
#     st.markdown("""
#         <div style='background:linear-gradient(90deg, #271c55, #2e205f); border-radius:15px; padding:25px; text-align:center;'>
#             <h2 style='color:#fdd835;'>Predicted Survival Time</h2>
#             <h1 style='color:#fbc02d; font-size:50px;'>{:.2f} Hours</h1>
#             <p style='color:#ffb74d;'>⚠️ Warning - Monitor closely</p>
#         </div>
#     """.format(survival_time), unsafe_allow_html=True)

#     st.write("")  # spacing

#     # --- Health & Resource Metrics ---
#     st.subheader("Health & Resource Metrics")

#     col1, col2, col3 = st.columns(3)
#     with col1:
#         st.metric("❤️ Heart Rate", f"{data['Heart Rate (BPM)']} BPM")
#         st.metric("🩸 Blood Pressure", data["Blood Pressure (mmHg)"])
#         st.metric("🔋 Battery Level", f"{data['Battery Level (%)']}%")
#     with col2:
#         st.metric("🫁 Respiratory Rate", f"{data['Respiratory Rate (BPM)']} BPM")
#         st.metric("💧 Hydration Level", f"{data['Hydration Level (%)']}%")
#         st.metric("🍽️ Food Supply", f"{data['Food Supply (Days)']} Days")
#     with col3:
#         st.metric("🧠 Oxygen Saturation", f"{data['Oxygen Saturation (%)']}%")
#         st.metric("🚰 Water Supply", f"{data['Water Supply (Liters)']} L")

#     if data["Oxygen Saturation (%)"] < 90 or data["Battery Level (%)"] < 20:
#         st.warning("🚨 Critical Alert: Low Oxygen or Battery Detected!")

#     st.write("---")

#     # --- Resource Overview Chart ---
#     st.subheader("Resource Overview")

#     chart_rows = []
#     for metric, value in data.items():
#         numeric_value = safe_float(value)
#         if numeric_value is not None:
#             chart_rows.append({"Metric": metric, "Value": numeric_value})

#     if chart_rows:
#         df = pd.DataFrame(chart_rows)
#         fig = go.Figure([
#             go.Bar(x=df["Metric"], y=df["Value"], marker_color="#60A5FA")
#         ])
#         fig.update_layout(
#             xaxis_title="Metric",
#             yaxis_title="Value",
#             template="plotly_dark",
#             margin=dict(l=20, r=20, t=30, b=20)
#         )
#         st.plotly_chart(fig, use_container_width=True)
#     else:
#         st.info("No numeric resource metrics available for charting.")

#     # --- AI Advisor ---
#     st.write("---")
#     st.subheader("🤖 AI Advisor")

#     if st.button("Get AI Recommendations"):
#         try:
#             res = client.chat.completions.create(
#                 messages=[{"role": "user", "content": "Provide astronaut survival improvement tips based on vitals."}],
#                 model="llama-3.3-70b-versatile"
#             )
#             st.success(res.choices[0].message.content)
#         except Exception as e:
#             st.error(f"AI API Error: {e}")

# # =========================
# # 🎛 SECTION: ANALYTICS DASHBOARD
# # =========================
# elif section == "📊 Analytics Dashboard":
#     st.markdown("<h2 style='color:#F5F5F5;'>📊 Mission Analytics Dashboard</h2>", unsafe_allow_html=True)

#     # --- Simulated Mission Data ---
#     missions = [
#         {"Mission": "MARS-2024", "Target": "Mars Exploration", "Distance": 225, "Cost": 3.5, "Crew": 6, "Success": 78},
#         {"Mission": "MOON-2024", "Target": "Moon Research", "Distance": 0.38, "Cost": 2.1, "Crew": 5, "Success": 88},
#         {"Mission": "ISS-2024", "Target": "Orbital Station", "Distance": 0.0004, "Cost": 1.8, "Crew": 4, "Success": 92},
#         {"Mission": "EUROPA-2025", "Target": "Europa Probe", "Distance": 628, "Cost": 3.6, "Crew": 8, "Success": 65},
#         {"Mission": "TITAN-2026", "Target": "Titan Research", "Distance": 1300, "Cost": 4.2, "Crew": 8, "Success": 58},
#     ]
#     df = pd.DataFrame(missions)

#     # --- Summary Stats ---
#     total_missions = len(df)
#     avg_success = round(df["Success"].mean(), 1)
#     total_cost = df["Cost"].sum()
#     total_crew = df["Crew"].sum()

#     # --- Metric Cards ---
#     col1, col2, col3, col4 = st.columns(4)
#     with col1:
#         st.markdown(
#             f"""
#             <div style='background:linear-gradient(90deg,#0F172A,#1E293B); padding:20px; border-radius:12px; text-align:center;'>
#                 <h4 style='color:#A5B4FC;'>Total Missions</h4>
#                 <h2 style='color:#60A5FA;'>{total_missions}</h2>
#             </div>
#             """, unsafe_allow_html=True)
#     with col2:
#         st.markdown(
#             f"""
#             <div style='background:linear-gradient(90deg,#022C22,#065F46); padding:20px; border-radius:12px; text-align:center;'>
#                 <h4 style='color:#A7F3D0;'>Avg Success Rate</h4>
#                 <h2 style='color:#34D399;'>{avg_success}%</h2>
#             </div>
#             """, unsafe_allow_html=True)
#     with col3:
#         st.markdown(
#             f"""
#             <div style='background:linear-gradient(90deg,#311B92,#4A148C); padding:20px; border-radius:12px; text-align:center;'>
#                 <h4 style='color:#E9D5FF;'>Total Cost</h4>
#                 <h2 style='color:#F472B6;'>${total_cost:.1f}B</h2>
#             </div>
#             """, unsafe_allow_html=True)
#     with col4:
#         st.markdown(
#             f"""
#             <div style='background:linear-gradient(90deg,#451A03,#78350F); padding:20px; border-radius:12px; text-align:center;'>
#                 <h4 style='color:#FED7AA;'>Total Crew</h4>
#                 <h2 style='color:#FB923C;'>{total_crew}</h2>
#             </div>
#             """, unsafe_allow_html=True)

#     st.write("---")

#     # --- Mission Success Chart ---
#     st.subheader("Mission Success Rates")
#     fig1 = go.Figure()
#     fig1.add_trace(go.Bar(
#         x=df["Mission"], y=df["Success"],
#         marker_color="#10B981", name="Success Rate (%)"
#     ))
#     fig1.update_layout(
#         template="plotly_dark",
#         xaxis_title="Mission",
#         yaxis_title="Success Rate (%)",
#         margin=dict(l=20, r=20, t=30, b=20)
#     )
#     st.plotly_chart(fig1, use_container_width=True)

#     # --- Cost vs Crew Chart ---
#     st.subheader("Cost vs Crew Size")
#     fig2 = go.Figure()
#     fig2.add_trace(go.Scatter(
#         x=df["Mission"], y=df["Cost"], mode="lines+markers",
#         name="Cost (Billion USD)", line=dict(color="#6366F1", width=3)
#     ))
#     fig2.add_trace(go.Scatter(
#         x=df["Mission"], y=df["Crew"], mode="lines+markers",
#         name="Crew Size", line=dict(color="#EC4899", width=3)
#     ))
#     fig2.update_layout(
#         template="plotly_dark",
#         xaxis_title="Mission",
#         yaxis_title="Value",
#         margin=dict(l=20, r=20, t=30, b=20)
#     )
#     st.plotly_chart(fig2, use_container_width=True)

#     st.write("---")

#     # --- Mission Database ---
#     st.subheader("Mission Database")
#     for _, row in df.iterrows():
#         st.markdown(
#             f"""
#             <div style='background-color:#1E1B4B; border-radius:10px; padding:15px; margin-bottom:10px;'>
#                 <h4 style='color:#60A5FA;'>{row['Mission']}</h4>
#                 <p style='color:#CBD5E1;'>{row['Target']}</p>
#                 <table style='width:100%; color:#E2E8F0;'>
#                     <tr>
#                         <td>Distance</td><td>{row['Distance']}M km</td>
#                         <td>Cost</td><td>${row['Cost']}B</td>
#                         <td>Crew</td><td>{row['Crew']}</td>
#                         <td style='color:#34D399;'>✅ {row['Success']}% Success</td>
#                     </tr>
#                 </table>
#             </div>
#             """, unsafe_allow_html=True)
# # =========================
# # 🎛 SECTION: NASA IMAGE
# # =========================
# elif section == "🌌 NASA Image View":
#     st.header("🌌 NASA Space Imagery")
#     try:
#         img_url, title, explanation = get_nasa_image()
#         if img_url:
#             st.image(img_url, caption=title, use_container_width=True)
#             with st.expander("Description"):
#                 st.write(explanation)
#         else:
#             st.warning("No NASA image available right now.")
#     except Exception as e:
#         st.error(f"Failed to load NASA image: {e}")

import streamlit as st

# Import section modules
import home
import arms_dashboard
import analytics_dashboard
import nasa_image_view

# Streamlit Config
st.set_page_config(page_title="🚀 ARMS Mission Console", layout="wide")

st.sidebar.title("🔭 ARMS Navigation")
section = st.sidebar.radio(
    "Choose Section:",
    ["🏠 Home", "🛰 ARMS Dashboard", "📊 Analytics Dashboard", "🌌 NASA Image View"]
)

# Route to section
if section == "🏠 Home":
    home.render_home()

elif section == "🛰 ARMS Dashboard":
    arms_dashboard.render_arms_dashboard()

elif section == "📊 Analytics Dashboard":
    analytics_dashboard.render_analytics_dashboard()

elif section == "🌌 NASA Image View":
    nasa_image_view.render_nasa_image()
