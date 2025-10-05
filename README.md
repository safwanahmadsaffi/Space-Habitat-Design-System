# 🌌 Space-Habitat-Design-System (SHDS)
**_Autonomous Resource Management System — AI-Powered Space Mission Dashboard_**


> **SHDS (Space-Habitat-Design-System)** is a real-time AI-powered space mission management system that monitors astronaut health, predicts survival time, manages mission analytics, and connects directly with NASA’s Astronomy Picture of the Day (APOD) API — all inside an immersive, interactive dashboard built with **Streamlit**.

---

## 🛰 Overview

The **Space-Habitat-Design-System (SHDS)** — also known as the **Autonomous Resource Management System (ARMS)** — provides intelligent mission support for astronauts and scientists.  
It enables **continuous monitoring, prediction, and adaptive recommendations** for safer and more efficient space missions.

### 🚀 Core Modules
- 🤖 **AI Advisor:** Provides mission-critical suggestions based on live vitals.  
- 📊 **Analytics Dashboard:** Visualizes mission and resource data.  
- 🩺 **Astronaut Dashboard:** Displays live vitals & survival predictions.  
- 🌌 **NASA APOD Integration:** Shows NASA’s Astronomy Picture of the Day.  
- 🔔 **Alerts & Notifications:** Smart alerting for emergencies and anomalies.  

---

## 🧠 System Architecture

Sensors → AI Engine → SHDS Dashboard → Alerts & Predictions

yaml
Copy code

Each sensor feeds real-time mission data (oxygen, heart rate, temperature, etc.) into the AI Engine, which then updates the dashboard visuals and triggers predictive analytics.

---

## 🌐 Application Pages

### 1️⃣ Dashboard Page  
**Purpose:** The main control hub for mission controllers and astronauts.

**Key Features:**
- Displays live vitals: 🫁 Oxygen, ❤️ Heart Rate, 🌡 Temperature, 💧 Water Supply  
- Color-coded alerts based on critical thresholds  
- Real-time survival prediction  
- Animated UI with dynamic space theme  

**User Interaction:**  
Hover over charts for detailed tooltips or manually refresh to update mission stats.

---

### 2️⃣ Analytics Page  
**Purpose:** Deep mission insights with AI-powered visualizations.

**Visuals:**
- Line charts for oxygen & temperature trends  
- Pie charts for resource usage  
- Bar charts for crew efficiency  

**Working:**  
Fetches simulated AI data, detects anomalies, and provides insight-based analytics.

---

### 3️⃣ AI Advisor  

**Purpose:** Intelligent suggestion engine.  
Analyzes all inputs and provides immediate recommendations.

---

### 4️⃣ NASA APOD Viewer
Purpose: Displays NASA’s Astronomy Picture of the Day with title & description.

API:
https://api.nasa.gov/planetary/apod?api_key=YOUR_KEY

Why: Adds visual engagement and connects mission teams to daily space discoveries.

---

### 5️⃣ Settings Panel
- Adjust live data refresh rate

- Toggle metric/imperial units

- Enable/disable sound alerts

- Connect/disconnect live sensor feeds

- All settings persist for the session.

---

### 6️⃣ Reports & Logs
- Generate daily logs in CSV or PDF

- Highlight anomalies and warnings

- Store local logs or sync to cloud (Firebase optional)

---

### 7️⃣ Alerts & Notifications
🔴 Critical Alerts: Immediate threats

🟠 Moderate Alerts: Warnings

🔵 System Alerts: AI/system anomalies

**Features:**

- Timestamped color-coded alerts

- Audio alerts

- Acknowledge or dismiss with one click

---

## ⚙️ Installation
### 1️⃣ Clone Repository
    bash
    Copy code
    git clone https://github.com/<your-username>/space-habitat-design-system.git
    cd space-habitat-design-system

---

## 2️⃣ Create Virtual Environment
    bash
    Copy code
    python -m venv venv
    source venv/bin/activate     # Windows: venv\Scripts\activate

---

## 3️⃣ Install Dependencies
    bash
    Copy code
    pip install -r requirements.txt


---
## 4️⃣ Add Environment Variables
- Create a .env file:

- bash
- Copy code
- NASA_API_KEY=your_nasa_api_key
- **⚠️ Don’t push .env to GitHub. Keep it private.**

---

### 5️⃣ Run Application
bash
Copy code

    streamlit run app.py
    
---

### 🌍 Deployment
# 🚀  Deploy on Streamlit Cloud
- Push to GitHub

- Go to streamlit.io/cloud

- Add app.py as the main file

- Configure API keys in Secrets

            Your live app → https://stellarpulse.streamlit.app

---

### 🌌 Deploy on Hugging Face Spaces
- Create a new Streamlit Space

- Upload your files or connect GitHub

- Add requirements.txt

- Add secrets (NASA_API_KEY) under “Settings”

---

## 📁 Project Structure

```bash
Space-Habitat-Design-System/
│
├── app.py                       # Main Streamlit app
│
├── pages/                       # Application pages
│   ├── dashboard.py             # Dashboard page (live vitals & stats)
│   ├── analytics.py             # AI-powered mission insights
│   ├── ai_advisor.py            # Intelligent recommendation engine
│   ├── nasa_apod.py             # NASA Astronomy Picture of the Day viewer
│   ├── alerts.py                # Alert and notification system
│   ├── reports.py               # Daily reports & log generator
│   └── settings.py              # Mission configuration panel
│
├── assets/                      # Images, animations, and visual assets
│
├── .env.example                 # Example environment variables
│
├── requirements.txt             # Python dependencies
│
└── README.md                    # Project documentation
```

### 👨‍🚀 Developer
Muhammad Safwan Ahmad Saffi
Software Engineer | AI & Space Tech Enthusiast

---

[MIT](https://choosealicense.com/licenses/mit/) © 2025 Space-Habitat-Design-System (SHDS) Project. All Rights Reserved.


            🌠 “Beyond Data. Beyond Limits. Designed for Space.”
