import streamlit as st
from utils import init_app
import sys
import os
import json


# Page config must be the first Streamlit command
st.set_page_config(
    page_title="EcoWise Living Platform",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Add the apps directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import app modules directly
from apps.app1 import main as transport_main
from apps.app2 import main as energy_main
from apps.app3 import main as water_main
from apps.app4 import main as food_main
from apps.app5 import main as waste_main

# Initialize the application
auth, model = init_app()

# Initialize session state
if 'user' not in st.session_state:
    st.session_state.user = None
if 'show_signup' not in st.session_state:
    st.session_state.show_signup = False
if 'model' not in st.session_state:
    st.session_state.model = model

def main():
    # Add this before authentication UI
    st.markdown("""
        <div style='text-align: center; padding: 20px;'>
            <h1 style='color: #1e88e5;'>🌍 Eco Action</h1>
            <p style='font-size: 1.2em; color: #ffffff;'>Make your life more efficient and sustainable</p>
        </div>
    """, unsafe_allow_html=True)

    # Authentication UI
    if not st.session_state.user:
        st.markdown("<div class='auth-container'>", unsafe_allow_html=True)
        
        if not st.session_state.show_signup:
            st.subheader("Login")
            with st.form("login_form"):
                username = st.text_input("Username")
                password = st.text_input("Password", type="password")
                submit = st.form_submit_button("Login")
                
                if submit:
                    success, message = auth.login_user(username, password)
                    if success:
                        st.session_state.user = username
                        st.success(message)
                        st.rerun()
                    else:
                        st.error(message)
            
            if st.button("Create Account"):
                st.session_state.show_signup = True
                st.rerun()
        else:
            st.subheader("Create Account")
            with st.form("signup_form"):
                new_username = st.text_input("Username")
                new_password = st.text_input("Password", type="password")
                name = st.text_input("Full Name")
                email = st.text_input("Email")
                submit = st.form_submit_button("Sign Up")
                
                if submit:
                    success, message = auth.register_user(new_username, new_password, name, email)
                    if success:
                        st.success(message)
                        st.session_state.show_signup = False
                        st.rerun()
                    else:
                        st.error(message)
            
            if st.button("Back to Login"):
                st.session_state.show_signup = False
                st.rerun()
        
        st.markdown("</div>", unsafe_allow_html=True)
        st.stop()

    # Sidebar navigation
    st.sidebar.title("🌍 EcoWise Living")
    
    # User info in sidebar
    st.sidebar.markdown(f"Welcome, {st.session_state.user}!")
    if st.sidebar.button("Logout"):
        st.session_state.user = None
        st.rerun()
    
    # Navigation
    page = st.sidebar.radio(
        "Choose Feature",
        ["Dashboard", "Transportation", "Energy", "Water", "Food", "Waste"]
    )

    # Page routing
    if page == "Dashboard":
        show_dashboard()
    elif page == "Transportation":
        transport_main(auth)
    elif page == "Energy":
        energy_main(auth)
    elif page == "Water":
        water_main(auth)
    elif page == "Food":
        food_main(auth)
    elif page == "Waste":
        waste_main(auth)

def show_dashboard():
    st.title("Your Sustainability Dashboard")
    
    # Get user progress
    progress = auth.get_user_progress(st.session_state.user)
    
    # Display metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Eco Score", "75", "+5")
    with col2:
        st.metric("Carbon Saved", "42 kg", "+3 kg")
    with col3:
        st.metric("Water Saved", "340 gal", "+15 gal")
    with col4:
        st.metric("Energy Reduced", "28 kWh", "-5%")

    # Feature completion - Updated calculation
    st.subheader("Feature Completion")
    features = ["Transportation", "Energy", "Water", "Food", "Waste"]
    for feature in features:
        feature_data = progress[progress['feature'] == feature.lower()]
        if not feature_data.empty:
            latest_data = json.loads(feature_data.iloc[-1]['data'])
            # Calculate progress based on feature-specific metrics
            if feature == "Transportation":
                eco_points = latest_data.get('eco_points', 0)
                travel_data = latest_data.get('travel_data', [])
                milestones = latest_data.get('milestones', {})
                
                # Calculate progress from multiple factors
                points_progress = min(1.0, eco_points/1000)  # Max 1000 points
                travel_progress = min(1.0, len(travel_data)/10)  # Max 10 trips
                milestone_progress = min(1.0, sum(milestones.values())/500)  # Max 500 miles total
                
                # Combined weighted progress
                feature_progress = (points_progress * 0.4 + 
                                  travel_progress * 0.3 + 
                                  milestone_progress * 0.3)
            else:
                feature_progress = len(feature_data)/10
        else:
            feature_progress = 0.0
        
        # Display progress bar and percentage
        st.progress(feature_progress)
        st.caption(f"{feature}: {int(feature_progress*100)}% complete")

if __name__ == "__main__":
    main()