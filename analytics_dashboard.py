import pandas as pd
import streamlit as st
import plotly.graph_objects as go

def render_analytics_dashboard():
    st.markdown("<h2>📊 Mission Analytics Dashboard</h2>", unsafe_allow_html=True)

    missions = [
        {"Mission": "MARS-2024", "Target": "Mars Exploration", "Distance": 225, "Cost": 3.5, "Crew": 6, "Success": 78},
        {"Mission": "MOON-2024", "Target": "Moon Research", "Distance": 0.38, "Cost": 2.1, "Crew": 5, "Success": 88},
        {"Mission": "ISS-2024", "Target": "Orbital Station", "Distance": 0.0004, "Cost": 1.8, "Crew": 4, "Success": 92},
        {"Mission": "EUROPA-2025", "Target": "Europa Probe", "Distance": 628, "Cost": 3.6, "Crew": 8, "Success": 65},
        {"Mission": "TITAN-2026", "Target": "Titan Research", "Distance": 1300, "Cost": 4.2, "Crew": 8, "Success": 58},
    ]
    df = pd.DataFrame(missions)

    total_missions = len(df)
    avg_success = round(df["Success"].mean(), 1)
    total_cost = df["Cost"].sum()
    total_crew = df["Crew"].sum()

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Missions", total_missions)
    with col2:
        st.metric("Average Success", f"{avg_success}%")
    with col3:
        st.metric("Total Cost", f"${total_cost:.1f}B")
    with col4:
        st.metric("Total Crew", total_crew)

    st.write("---")
    st.subheader("Mission Success Rates")
    fig1 = go.Figure([go.Bar(x=df["Mission"], y=df["Success"], marker_color="#10B981")])
    fig1.update_layout(template="plotly_dark")
    st.plotly_chart(fig1, use_container_width=True)

    st.subheader("Cost vs Crew Size")
    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=df["Mission"], y=df["Cost"], mode="lines+markers", name="Cost (B$)"))
    fig2.add_trace(go.Scatter(x=df["Mission"], y=df["Crew"], mode="lines+markers", name="Crew"))
    fig2.update_layout(template="plotly_dark")
    st.plotly_chart(fig2, use_container_width=True)

    st.subheader("Mission Database")
    st.dataframe(df)
