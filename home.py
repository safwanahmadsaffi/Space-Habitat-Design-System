# pages/home.py
import streamlit as st

def render_home():
    st.markdown("""
        <style>
        /* ===== Background Layers ===== */
        body {
            background-color: #000010;
            overflow: hidden;
        }

        /* Deep starfield layers */
        .stars1, .stars2, .stars3 {
            position: fixed;
            width: 2px;
            height: 2px;
            background: white;
            border-radius: 50%;
            opacity: 0.8;
            animation: moveStars 80s linear infinite;
            z-index: 0;
        }

        .stars1 {
            box-shadow: 100px 300px white, 400px 100px white, 700px 250px white, 
                         900px 450px white, 1200px 150px white, 1400px 600px white;
            animation-duration: 120s;
            opacity: 0.3;
        }

        .stars2 {
            box-shadow: 150px 100px white, 500px 400px white, 800px 200px white, 
                         1000px 300px white, 1300px 500px white, 1600px 100px white;
            animation-duration: 80s;
            opacity: 0.5;
        }

        .stars3 {
            box-shadow: 200px 150px white, 600px 350px white, 950px 100px white, 
                         1150px 450px white, 1450px 250px white, 1750px 550px white;
            animation-duration: 60s;
            opacity: 0.7;
        }

        @keyframes moveStars {
            from {transform: translateY(0);}
            to {transform: translateY(1000px);}
        }

        /* Sun/flare effect */
        .sun {
            position: fixed;
            top: -200px;
            left: -200px;
            width: 600px;
            height: 600px;
            background: radial-gradient(circle, rgba(255,200,50,0.8), rgba(255,100,0,0.1), transparent 70%);
            border-radius: 50%;
            box-shadow: 0 0 80px rgba(255,150,50,0.8);
            z-index: 0;
            animation: pulse 6s infinite alternate ease-in-out;
        }

        @keyframes pulse {
            from { transform: scale(1); opacity: 0.8; }
            to { transform: scale(1.2); opacity: 1; }
        }

        /* Spaceship animation */
        .fighter {
            position: fixed;
            width: 120px;
            opacity: 0.9;
            z-index: 1;
            animation: flyAcross 25s linear infinite;
        }

        .fighter:nth-child(1) {
            top: 30%;
            left: -150px;
            animation-delay: 0s;
        }
        .fighter:nth-child(2) {
            top: 60%;
            left: -200px;
            animation-delay: 10s;
        }

        @keyframes flyAcross {
            from { transform: translateX(-200px) rotate(5deg); }
            to { transform: translateX(2000px) rotate(-5deg); }
        }

        /* ===== Foreground Boxes ===== */
        .feature-box {
            background: rgba(30, 30, 60, 0.75);
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.5);
            transition: 0.3s ease-in-out;
            text-align: center;
            color: white;
        }

        .feature-box:hover {
            transform: translateY(-5px);
            background: rgba(80, 80, 150, 0.85);
            box-shadow: 0 8px 25px rgba(0,0,0,0.6);
        }

        .feature-title {
            font-size: 20px;
            font-weight: bold;
            margin-bottom: 10px;
        }
        </style>

        <!-- Background Layers -->
        <div class="sun"></div>
        <div class="stars1"></div>
        <div class="stars2"></div>
        <div class="stars3"></div>
        <img class="fighter" src="https://cdn-icons-png.flaticon.com/512/3210/3210059.png">
        <img class="fighter" src="https://cdn-icons-png.flaticon.com/512/3075/3075977.png">
    """, unsafe_allow_html=True)

    # Foreground UI
    st.markdown("<h2 style='color:white; text-align:center;'>🛰 Welcome to <b>SHDS — Space-Habitat-Design-System</b></h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#ddd;'>An integrated platform for astronaut monitoring, mission analytics, and space visualization.</p>", unsafe_allow_html=True)
    st.markdown("---")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            """
            <div class='feature-box'>
                <div class='feature-title'>🩺 SHDS Dashboard</div>
                Real-time astronaut vitals and survival estimation.
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class='feature-box'>
                <div class='feature-title'>📊 Analytics Dashboard</div>
                Mission dataset analysis and AI-driven insights.
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            <div class='feature-box'>
                <div class='feature-title'>🌌 NASA Image View</div>
                Explore NASA’s Astronomy Picture of the Day.
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")
    st.image(
        "https://www.nasa.gov/sites/default/files/thumbnails/image/1-bluemarble_west.jpg",
        use_container_width=True,
        caption="🌍 The Blue Marble — Our Home Planet"
    )
