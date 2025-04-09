import streamlit as st

# Page config must be the first Streamlit command
st.set_page_config(
    page_title="EcoWise Living Platform",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

from utils import init_app
import sys
import os

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

    # Feature completion
    st.subheader("Feature Completion")
    features = ["Transportation", "Energy", "Water", "Food", "Waste"]
    for feature in features:
        feature_progress = len(progress[progress['feature'] == feature.lower()])
        st.progress(min(1.0, feature_progress/10))
        st.caption(f"{feature}: {feature_progress*10}% complete")

    # Recent activity
    st.subheader("Recent Activity")
    if not progress.empty:
        recent = progress.sort_values('timestamp', ascending=False).head(5)
        for _, row in recent.iterrows():
            st.markdown(f"**{row['feature'].title()}**: {row['timestamp']}")

if __name__ == "__main__":
    main()